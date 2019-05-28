#!/usr/bin/env python3
# coding: utf-8

from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class PolygonForm(FlaskForm):
    slide = DecimalField("Nombre de cotés", validators=[NumberRange(min=3)], places=1)
    angle = DecimalField("Nombre d'angles droit", validators=[NumberRange(min=0)], places=1)
    equal = DecimalField("Nombre de cotés égaux", validators=[NumberRange(min=0)], places=1)
    parallel = DecimalField("Nombre de cotés parallèles", validators=[NumberRange(min=0)], places=1)
    submit = SubmitField('Search')
