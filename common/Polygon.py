#!/usr/bin/env python3
# coding: utf-8

UNKNOWN_POLYGON_NAME = "Inconnue"


class Polygon:

    def __init__(self, slide, angle, equal, parallel, name=UNKNOWN_POLYGON_NAME):
        self.slide = int(slide)
        self.angle = int(angle)
        self.equal = int(equal)
        self.parallel = int(parallel)
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Polygon):
            return NotImplemented
        return (other.slide == self.slide
                and other.angle == self.angle
                and other.equal == self.equal
                and other.parallel == self.parallel)

    def __csv__(self):
        return ";".join([str(self.slide), str(self.angle), str(self.equal), str(self.parallel), self.name])

    def __str__(self):
        return "Le polygone est un {name} possédant {slide} cotés dont {equal} égaux " \
               "et {parallel} parallèles ainsi que {angle} angles droits.".format(
                name=self.name, slide=self.slide, equal=self.equal, parallel=self.parallel, angle=self.angle)

