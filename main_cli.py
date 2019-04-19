#!/usr/bin/env python3
# coding: utf-8

import argparse
from common.Engine import Engine

MIN_SLIDE = 3
DEFAULT_FILE = "data.csv"


def parse_args():
    parser = argparse.ArgumentParser(description="Reconnaissance de Polygon",
                                     usage="%(prog)s [OPTIONAL] <Cotés> <AnglesDroit> <CotésÉgaux> <CotésParralèles>")
    parser.add_argument("slide", metavar="Cotés", help="Nombre de coté du polygon", type=int)
    parser.add_argument("angle", metavar="AnglesDroit", help="Nombre d'angle droit du polygon", type=int)
    parser.add_argument("equal", metavar="CotésÉgaux", help="Nombre de coté égaux du polygon", type=int)
    parser.add_argument("parallel", metavar="CotésParallèles", help="Nombre de coté parralèle du polygon", type=int)
    parser.add_argument("--csv", help="Chemin personnalisé du fichier csv de la base de faits", action='store', default=DEFAULT_FILE)
    args = parser.parse_args()
    return args


def check_args(args):
    if args.slide < MIN_SLIDE:
        raise argparse.ArgumentTypeError("Minimum slide is " + str(MIN_SLIDE))


def main():
    args = parse_args()
    check_args(args)
    engine = Engine(args.csv)
    polygon = engine.find_polygon(args.slide, args.angle, args.equal, args.parallel)
    print(polygon)


if __name__ == '__main__':
    main()
