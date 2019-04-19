#!/usr/bin/env python3
# coding: utf-8

import os

from common.Polygon import Polygon


class FactBase:

    def __init__(self, datafile):
        self.datafile = datafile

    def polygon_from_file_generator(self):
        if os.path.exists(self.datafile):
            with open(self.datafile, "r+") as file:
                for line in file:
                    line = line.rstrip('\n')
                    elem = line.split(';')
                    yield Polygon(elem[0], elem[1], elem[2], elem[3], elem[4])
            file.close()

    def find_polygon(self, polygone):
        for datapoly in self.polygon_from_file_generator():
            if datapoly == polygone:
                return datapoly
        return None

    def add_polygon(self, newpolygon):
        with open(self.datafile, "a+") as file:
            file.write(newpolygon.to_csv() + os.linesep)
        file.close()
