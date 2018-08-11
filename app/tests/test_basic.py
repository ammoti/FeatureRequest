# app/test.py

import unittest
import app
import os
from datetime import datetime

from app import app,db
from app.models import FeatureModel

BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

class BasicTests(unittest.TestCase):
    def setUp(self):
        # app.config['TESTING'] = True
        # app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')

        self.app = app.test_client()
        db.drop_all()
        db.create_all()

  
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_home_page(self):
        response = self.app.get('/',follow_redirects=True)
        self.assertEqual(response.status_code,200)
        
    def test_feature_create(self):
        new_feature = FeatureModel(title='title',client='A',description='desc',priority=1,product_area='policy',target_date=datetime.strptime('2018-08-10', '%Y-%m-%d'))
        
        print(new_feature)
        db.session.add(new_feature)
        db.session.commit()
        features = FeatureModel.query.all()
        assert new_feature in features
        print("NUMBER OF ENTRİES:")
        print (len(features))

    def test_feature_delete(self):
        new_feature = FeatureModel(title='title',client='A',description='desc',priority=1,product_area='policy',target_date=datetime.strptime('2018-08-10', '%Y-%m-%d'))        
        db.session.add(new_feature)
        db.session.commit()

        feature_to_delete = FeatureModel.query.get(new_feature.id)
        db.session.delete(feature_to_delete)
        db.session.commit()
        
        features = FeatureModel.query.all()
        assert new_feature not in features
        print("NUMBER OF ENTRİES:")
        print (len(features))
        
if __name__ == '__main__':
    unittest.main()