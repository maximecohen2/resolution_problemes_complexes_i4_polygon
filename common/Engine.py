#!/usr/bin/env python3
# coding: utf-8

from common.Polygon import Polygon
from common.FactBase import FactBase
from common.RuleBase import RuleBase


class Engine:

    def __init__(self, datafile):
        self.factbase = FactBase(datafile)
        self.rulebase = RuleBase()

    def find_polygon(self, slide, angle, equal, parallel):
        newpolygon = Polygon(slide, angle, equal, parallel)
        knownpolygon = self.factbase.find_polygon(newpolygon)
        if knownpolygon is not None:
            return knownpolygon
        else:
            self.rulebase.find_polygon(newpolygon)
            self.factbase.add_polygon(newpolygon)
        return newpolygon
