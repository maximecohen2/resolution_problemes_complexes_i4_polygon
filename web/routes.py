#!/usr/bin/env python3
# coding: utf-8
from common.Engine import Engine
from web import app
from flask import render_template, redirect

from web.forms import PolygonForm

DEFAULT_FILE = "data.csv"

engine = Engine(DEFAULT_FILE)


@app.route('/', methods=['GET', 'POST'])
def index_form():
    form = PolygonForm()
    if form.validate_on_submit():
        polygon = engine.find_polygon(form.slide.data, form.angle.data, form.equal.data, form.parallel.data)
        return render_template('result.html', title='Home', result=str(polygon))
    return render_template('index.html', title='Home', form=form)


