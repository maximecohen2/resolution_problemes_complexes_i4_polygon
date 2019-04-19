#!/usr/bin/env python3
# coding: utf-8


from common.Polygon import Polygon


class RuleBase:

    def find_polygon(self, polygon):
        if polygon.slide == 3:
            self.find_triangle(polygon)
        elif polygon.slide == 4:
            self.find_quadrilateral(polygon)
        else:
            polygon.name = "Polygon"

    def find_triangle(self, polygon):
        if polygon.equal == 3:
            polygon.name = "Triangle Équilatéral"
        elif polygon.equal == 2 and polygon.angle == 1:
            polygon.name = "Triangle Rectangle Isocèle"
        elif polygon.equal == 2:
            polygon.name = "Triangle Isocèle"
        elif polygon.angle == 1:
            polygon.name = "Triangle Rectangle"
        else:
            polygon.name = "Triangle"

    def find_quadrilateral(self, polygon):
        if polygon.angle == 4 and polygon.equal == 4 and polygon.parallel == 2:
            polygon.name = "Carré"
        elif polygon.angle == 4 and polygon.equal == 2 and polygon.parallel == 2:
            polygon.name = "Rectangle"
        elif polygon.equal == 4 and polygon.parallel == 2:
            polygon.name = "Losange"
        elif polygon.equal == 2 and polygon.parallel == 2:
            polygon.name = "Parallélogramme"
        elif polygon.parallel == 2:
            polygon.name = "Trapèze"
        elif polygon.equal == 2:
            polygon.name = "Cerf-volant"
        else:
            polygon.name = "Quadrilatère"