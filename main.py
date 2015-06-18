import os

from flask import Flask, render_template, url_for
from werkzeug import cached_property
import markdown
import yaml

app = Flask(__name__)

class Post(object):
  def __init__(self, path, root_dir =''):
    self.urlpath = os.path.splitext(path.strip('/'))[0]
    self.filepath = os.path.join(root_dir, path.strip('/'))
    self._initialize_metadata()

  @cached_property
  def html(self):
    with open(self.filepath, 'r') as fin:
      content = fin.read().split('\n\n', 1)[1].strip() #remove the metadata from post before rendering it's HTML split(\n\n, 1).strip() array splits based on a blank line and tells it to do this once and index [1] refers to the content
    return markdown.markdown(content) #return .md file as html

  @property
  def url(self):
    return url_for('post', path = self.urlpath)



  def _initialize_metadata(self):
    content = ''
    with open(self.filepath, 'r') as fin:
      for line in fin:
        if not line.strip():
          break
        content = line
    self.__dict__.update(yaml.load(content)) #(yaml.load)converts content metadata dic into python dic and merges the attributes of the metadata function with update

# Custom Jinja Filter
@app.template_filter('date')
def format_date(value, format='%B %d, %Y'):
    return value.strftime(format)

@app.route('/')
@app.route('/index')
def index():
  posts = [Post('sample_blog.md', root_dir = 'posts')]
  return render_template ('index.html', posts = posts)

@app.route('/post/<path:path>')
def post(path):
  post = Post(path + '.md', root_dir = 'posts')
  return render_template ('post.html', post = post)


	
     
	
if __name__ == "__main__":
  app.run(debug = True)