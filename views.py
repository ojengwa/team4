from run import app
import requests
from datetime import datetime
from flask import render_template
from bs4 import BeautifulSoup

from . import auth

# from flask.ext.script import Manager
# manager = Manager(app)

# from flask.ext.bootstrap import Bootstrap
# # ...
# bootstrap = Bootstrap(app)



@auth.route('/login')
def login():
	return render_template('login.html')


# @app.route('/')
@app.route('/')
@app.route('/index')
def index():
	return "Hello world"



def get_url_details(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content) #.prettify()
    return soup


# use this method to pass the necessay content to the view
def pass_the_necessary_content_with_soup():
    pass

link_to_crawl = "http://www.konga.com/catalogsearch/result/?cat=0&q=nokia+lumia"
link_to_crawl2 = "http://www.goal.com/en-ng/"

@app.route('/reader')
def very_fast_soup():
    results = get_url_details(link_to_crawl2)
    print results
    return render_template('index.html', year=datetime.now().year, results = results)



@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html' ), 404
 
@app.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html' ), 500   
