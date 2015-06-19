import os
import sys

from flask import Flask, render_template, url_for, request, flash, redirect
from flask.ext.frozen import Freezer
from werkzeug import cached_property
from werkzeug.contrib.atom import AtomFeed
import markdown
import yaml

import requests
from datetime import datetime
from bs4 import BeautifulSoup
from time import clock

# from app import app
# from .forms import LoginForm




app = Flask(__name__)
freezer = Freezer(app)

def make_external(url):
    return urljoin(request.url_root, url)

class Post(object):
    def __init__(self, path, root_dir=''):
        self.urlpath = os.path.splitext(path.strip('/'))[0]
        self.filepath = os.path.join(root_dir, path.strip('/'))
        self._initialize_metadata()
        

    @cached_property
    def html(self):
        with open(self.filepath, 'r') as fin:
            content = fin.read().split('\n\n', 1)[1].strip()
        return markdown.markdown(content)
    
    @property
    def url(self):
        return url_for('post', path=self.urlpath)

    def _initialize_metadata(self):
        content = ''
        with open(self.filepath, 'r') as fin:
            for line in fin:
                if not line.strip():
                    break
                content += line
        self.__dict__.update(yaml.load(content))


@app.template_filter('date')
def format_date(value, format='%B %d, %Y'):
    return value.strftime(format)


# Routes

@app.route('/')
@app.route('/index')
def index():
    posts = []
    filepaths = ['hello.md', 'world.md', 'sunny.md', 'sample_blog.md']
    for filepath in filepaths:
      path = os.path.join('posts', filepath)
      post = Post(path)
      posts.append(post)
    
    return render_template('index.html', posts=posts)

@app.route('/blog/<path:path>/')
def post(path):
    post = Post(path + '.md', root_dir='posts')
    return render_template('post.html', post=post)


@app.route('/feed.atom')
def feed():
    posts = []
    filepaths = ['hello.md', 'world.md', 'sunny.md', 'sample_blog.md']
    for filepath in filepaths:
      path = os.path.join('posts', filepath)
      post = Post(path)
      posts.append(post)

    feed = AtomFeed('Recent Articles',
                    feed_url=request.url, 
                    url=request.url_root)
<<<<<<< HEAD
    posts = posts[:4]
=======
    posts = posts[:1]
>>>>>>> bc868330dbf13e5210a70e025221483e9107e0b0
    for post in posts:
        feed.add(post.title, 
            unicode(post.html),
            content_type='html',
            author=post.author,
            url=post.url,
            updated=post.date,
            published=post.date)
    return feed.get_response()





def get_url_details(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content) #.prettify()
    return soup



def make_the_tags_beautiful(url):
    pretty_link = get_url_details(url).prettify
    return pretty_link



# use this method to pass the necessay content to the view
def pass_the_necessary_content_with_soup():
    pass

link_to_crawl = "http://www.konga.com/catalogsearch/result/?cat=0&q=nokia+lumia"
link_to_crawl2 = "http://www.goal.com/en-ng/"
link_to_crawl3 = "http://lindaikeji.blogspot.com/"





@app.route('/reader')
def very_fast_soup():
    results = get_url_details(link_to_crawl3)
    print results
    return render_template('lindaing.html', year=datetime.now().year, results = results)






if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build': #To freeze our website into a file of static files with the command build
        freezer.freeze()
    else:
<<<<<<< HEAD
        app.run(debug=True)
=======
        app.run(debug=True)
>>>>>>> bc868330dbf13e5210a70e025221483e9107e0b0
