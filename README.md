[![Build Status](https://travis-ci.org/ammoti/BriteCore.FeatureRequests.svg?branch=master)](https://travis-ci.org/ammoti/BriteCore.FeatureRequests)

# BriteCore.FeatureRequests

FeatureRequest is the best tool which can create feature-request aroun the world.

## Tech Stack

This project was built using the following technologies:

* Server-Side: Python 3.6
* Microframework: Flask
* ORM: Sql-Alchemy (SQLLite)
* Front-End: Bootstrap.
* JavaScript: KnockoutJS
* Continuous Integration: Travis-CI
* Host : Heroku
* Test : Unittest

## Folder Structure
    .
    ├── app                     # assets of the projects (Javascript or CSS)
    │   ├── templates           # application templates
    │   ├── tests               # Integration tests
    │   ├── models.py           # FeatureModel define here
    │   └── views.py            # We can call it our routers
    ├── .travis.yml             # Travis-CI settings
    ├── app.py                  # Starting our dev server
    └── config.py               # Our configuration file

### Prerequisites

You have to just sure your that on local machine has python 3.6

### Installing

For the run in your local project

First clone the repository

```
git clone https://github.com/ammoti/BriteCore.FeatureRequests.git
```

After that install the requirements via pip

```
pip install -r requirements.txt
```

If everything goes smooth all you have to do run below command in project root;

```
python app.py
```

You will see that some information project and host and port number (most probably like that  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit))
When you open a browser and type 127.0.0.0.1:5000 you will see the project running.

## Running the tests

In this project I use the unittest for automated testing and you can see in tests folder. For the running; just run this command ;

```
python -m unittest discover
```
You can see the results whether test OK or FAIL.

## Deployment

For Continuous Integration I have used [travis-ci](https://travis-ci.org/) and for the host I use [Heroku](https://heroku.com/) (free plan). If the commit passing all automated test on travis it's directly deploying on Heroku platform

## Live 

You can also experience this project in live at https://britecore-featurerequest.herokuapp.com (sometimes heroku will shutdown the server please inform me at this moments).


## Authors

* **Vahap Yigit** - *Initial work* - [ammoti](https://github.com/ammoti)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
