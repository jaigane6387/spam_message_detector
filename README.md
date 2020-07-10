# spam message detection App

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [Bug / Feature Request](#bug---feature-request)
  
  ## Demo
  Link: [https://spam-blocker.herokuapp.com/](https://spam-blocker.herokuapp.com/)
  
  [![](https://github.com/jaigane6387/spam_message_detector/blob/master/demo.png)](https://spam-blocker.herokuapp.com/)

## Overview
This is a general web application which predicts whether a message is spam or not.

## Motivation
 I started to learn Data science to explore my carrier in Data world. I learned different methodologies and tools to achieve and solve real world problems. Finally it is important to work on application (real world application) to actually make a difference.

## Installation
The Code is written in Python 3.6.10. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Deployement on Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download ctl to deploy this project.

[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)

Next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web application.

## Directory Tree 
```
├── data 
│   ├──SMSSpamCollection
├── static 
│   ├── css
├── template
│   ├── home.html
│   ├── result.html
├── Procfile
├── README.md
├── Spam Classifier.ipynb
├── app.py
├── demo.png
├── requirements.txt
├── spam_classifier.pkl
├── vectorizer.pkl
```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) [<img target="_blank" src="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/python_nltk.png?w=316&ssl=1" width=150>] (https://www.nltk.org/)


## Bug / Feature Request

If you find a bug , kindly open an [issue](https://github.com/jaigane6387/spam_detector_app/issues) here by including your search query and the expected result  
