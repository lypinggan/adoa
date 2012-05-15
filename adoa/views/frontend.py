#!/usr/bin/env python
#coding=utf-8
"""
    views: frontend.py
    ~~~~~~~~~~~~~~~~~
    :author: lypinggan@163.com
"""
import urllib
import tornado.web

from adoa.views.base import RequestHandler
from adoa.database import db
from adoa.models import Link
from adoa.extensions.routing import route
from adoa.permissions import admin
@route(r'/', name='index')
class Index(RequestHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('index.html')
        return
@route(r'/home', name='home')
class Home(RequestHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('home.html')
        return
@route(r'/todo', name='todo')
class Todo(RequestHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('todo.html')
        return
