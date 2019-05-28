#!/usr/bin/env python3
# coding: utf-8

from flask import Flask
from web.config import Config

app = Flask(__name__)
app.config.from_object(Config)


from web import routes
