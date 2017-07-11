# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append('/Library/Python/2.7/site-packages')

import subprocess
from libs.bottle import route, run, error, post, request, redirect, default_app, template, SimpleTemplate, static_file, response, view, HTTPError, get
import os, time
import markdown, datetime


markdownDir = 'public/markdown/'
postList = {}
postTime = {}

from config import config

SimpleTemplate.defaults['keywords'] = ''
SimpleTemplate.defaults['siteName'] = config['siteName']
SimpleTemplate.defaults['bio'] = config['bio']

def getPost(f):
  global postList, postTime

  _path = markdownDir+f

  f0 = open(_path)
  md = f0.read()
  f0.close()

  post = {}

  f = f.split('_')

  ftime = datetime.datetime.strptime(f[0], "%Y-%m-%d").strftime('%b %d, %Y')

  title = f[1]
  url = '/post/'+f[1]

  Md = markdown.Markdown(extensions = ['attr_list', 'meta'])
  content = Md.convert(md)

  post = {}
  if hasattr(Md, 'Meta'):
    post = Md.Meta

  for v in post:
    if v != 'preview':
      post[v] = post[v][0]

  if post.get('preview'):
    preview = post['preview']
    preview = ''.join(preview)
    post['preview'] = Md.convert(preview)
  else:
    post['preview'] = ''

  post['content'] = content

  post = dict({
    'ftime': ftime,
    'url': url,
    'title': title,
    'content': content
  }, **post)

  postList[f[1]] = post
  postTime[f[1]] = f[0]

_map = os.listdir(markdownDir)
for f in _map:
  if os.path.isdir(markdownDir+f): continue

  # left, mid, substr, slice, splice
  if f[-4:] == '.swp': continue
  getPost(f)

postTime = sorted([(value,key) for (key,value) in postTime.items()], reverse=True)


# *****************************************
# @Router
# *****************************************
@route('/public/assets/images/<filename>')
@route('/public/assets/images/:path/<filename>')
def source(filename, path=''):
  return static_file(filename, root="public/assets/images/"+path)

@route('/public/assets/css/<filename>')
def css(filename):
  return static_file(filename, root='public/assets/css')

@route('/public/assets/javascripts/<filename>')
def javascripts(filename):
  return static_file(filename, root='public/assets/javascripts')

@route('/public/assets/font/<filename>')
def css(filename):
  return static_file(filename, root='public/assets/font')

@route('/public/tpls/inc/<filename>')
def tpls(filename):
  return static_file(filename, root='tpls/inc')



# 404
@error(404)
@view('public/tpls/404.tpl')
def error404(error):
  return config

# home
@route('/')
@view('public/tpls/index.tpl')
def index():
  _config = {
    'postList': postList,
    'postTime': postTime
  }

  return dict(config.copy(), ** _config)

# about
@route('/about/')
@route('/about')
@view('public/tpls/about.tpl')
def about():
  _config = {'title': 'About'}
  return dict(config.copy(), ** _config)



@route('/post/<id:path>/')
@route('/post/<id:path>')
@route('/post/')
@route('/post')
@view('public/tpls/post.tpl')
def mypost(id=''):
  if id in postList:
    post = postList[id]
    if post['keywords']:
      SimpleTemplate.defaults['keywords'] = post['keywords']

    return dict(config.copy(), ** post)
  else:
    return HTTPError(404, 'Page not found!')

run(host='0.0.0.0', port='3030')
