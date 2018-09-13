# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import subprocess
from bottle import route, run, error, post, request, redirect, default_app, template, SimpleTemplate, static_file, response, view, HTTPError, get
import os, time
import markdown, datetime

from config import config

def getPosts():
  posts = []

  mdir = config['markdowndir']
  _map = os.listdir(mdir)
  for f in _map:
    if os.path.isdir(mdir + f): continue
    if f[-3:] != '.md': continue

    date, url  = f.split('_')
    date = datetime.datetime.strptime(date, "%Y-%m-%d").strftime('%b %d, %Y')
    url = '/post/' + url

    fo = open(mdir + f)
    md = fo.read()
    fo.close()

    Md = markdown.Markdown(extensions = ['attr_list', 'meta'])
    content = Md.convert(md)

    if hasattr(Md, 'Meta'):
      post = Md.Meta

    for k in post:
      if k != 'preview':
        post[k] = post[k][0]

    post['url'] = url
    post['date'] = date
    post['content'] = content

    if post.get('preview'):
      preview = post['preview']
      preview = ''.join(preview)
      post['preview'] = Md.convert(preview)
    else:
      post['preview'] = ''

    posts.append(post)

  posts = sorted(posts, key=lambda k: k['date'], reverse=True)

  return posts

# *****************************************
# @Router
# *****************************************

SimpleTemplate.defaults['online'] = False
SimpleTemplate.defaults['title'] = ''
SimpleTemplate.defaults['keywords'] = ''
SimpleTemplate.defaults['sitename'] = config['sitename']
SimpleTemplate.defaults['bio'] = config['bio']

@route('/public/images/<filename>')
@route('/public/images/:path/<filename>')
def source(filename, path=''):
  return static_file(filename, root="public/images/"+path)

@route('/public/css/<filename>')
def css(filename):
  return static_file(filename, root='public/css')

@route('/public/javascripts/<filename>')
def javascripts(filename):
  return static_file(filename, root='public/javascripts')

@route('/public/font/<filename>')
def css(filename):
  return static_file(filename, root='public/font')

@route('/tpls/inc/<filename>')
def tpls(filename):
  return static_file(filename, root='tpls/inc')

# 404
@error(404)
@view('tpls/404.tpl')
def notfound(error):
  return config

# home
@route('/')
@view('tpls/home.tpl')
def index():
  # markdowndir = config['markdowndir']
  # print markdowndir

  # _map = os.listdir(markdowndir)
  # for f in _map:
  #   if os.path.isdir(markdowndir + f): continue

  #   # left, mid, substr, slice, splice
  #   if f[-3:] != '.md': continue
  #   getPost(f)


  # postTime = sorted([(value,key) for (key,value) in postTime.items()], reverse=True)

  # _config = {
  #   'postList': postList,
  #   'postTime': postTime
  # }

  # return dict(config.copy(), ** _config)


  posts = getPosts()
  print posts
  return { "posts": posts }

# about
@route('/about/')
@route('/about')
@view('tpls/about.tpl')
def about():
  _config = {'title': 'About'}
  return dict(config.copy(), ** _config)

# post
@route('/post/<id:path>/')
@route('/post/<id:path>')
@route('/post/')
@route('/post')
@view('tpls/post.tpl')
def mypost(id=''):
  if id in postList:
    post = postList[id]
    if post['keywords']:
      SimpleTemplate.defaults['keywords'] = post['keywords']

    return dict(config.copy(), ** post)
  else:
    return HTTPError(404, 'Page not found!')

run(host='0.0.0.0', port=config['port'])
