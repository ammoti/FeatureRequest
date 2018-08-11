"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, Flask,request,json,jsonify
from app import app,db
from app.models import FeatureModel

@app.route('/')
@app.route('/home')
def home():
    features = FeatureModel.query.order_by('-id').all()
    """Renders the home page."""

    return render_template('index.html',
        title = 'Home Page',
        year = datetime.now().year,
         features = features)


@app.route('/search',methods=['POST'])
def search():
    search = request.form['search']
    features = FeatureModel.query.filter_by(title=search).all()
    """Renders the search page."""
    return render_template('index.html',
        title = 'Home Page',
        year = datetime.now().year,
         features = features)

@app.route('/create_feature', methods=['GET', 'POST'])
def create():
    """Renders the create page."""
    if request.method == "GET":
        return render_template('create_feature.html',
        title='Create New Requests')
    
    elif request.method == "POST":    
        title = request.form['featureTitle']
        description = request.form['featureDescription']
        client = request.form['feautureClient']
        priority = int(request.form['priority'])
        target = datetime.strptime(request.form['target'], '%Y-%m-%d')
        area = request.form['area']
     
        # validate the received values
        if title:
            new_feature = FeatureModel(title=title,
                description=description,
                priority=priority,
                target_date=target,
                client=client,
                product_area=area)
            db.session.add(new_feature)
            reOrderPriority(priority,client)
            db.session.commit()
            return home()

@app.route('/delete/<int:feature_id>', methods=['DELETE'])
def deleteFeature(feature_id):
    if request.method == 'DELETE':
        if feature_id:
            feature_to_delete = FeatureModel.query.get(feature_id)
            db.session.delete(feature_to_delete)
            db.session.commit()
            return home()


def reOrderPriority(priority,client):
    tempPriority = priority

    features_to_update_count = FeatureModel.query.filter_by(client=client, priority=tempPriority).count()

    if features_to_update_count > 1:
        feature_to_update = FeatureModel.query.filter_by(client=client, priority=tempPriority).order_by('id').first()
        feature_to_update.priority = feature_to_update.priority + 1
        tempPriority = tempPriority + 1
        features_to_update_count = FeatureModel.query.filter_by(client=client, priority=tempPriority).count()
        db.session.commit()
        reOrderPriority(tempPriority,client)
    else:
        return