#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Foobar.py: Description of what foobar does."""

__author__ = "Olivier Nocent"
__credits__ = ["Olivier Nocent"]


from math import *

#
# Rayon de la Terre au niveau de l'équateur (en mètres)
# a = 6378137
#
# Rayon de la Terre au niveau des pôles (en mètres)
# b = 6356752 
#
# Rayon moyen de la Terre (en mètres)
# R = (2*a+b)/3 = 6371009
#
def great_circle_distance(lat1, lon1, lat2, lon2):
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    dLon = radians(fabs(lon2-lon1))

    cosLat1 = cos(lat1)
    sinLat1 = sin(lat1)
    cosLat2 = cos(lat2)
    sinLat2 = sin(lat2)
    cosDLon = cos(dLon)
    sinDLon = sin(dLon)

    A = cosLat2*sinDLon
    B = cosLat1*sinLat2 - sinLat1*cosLat2*cosDLon

    return 6371009 * atan2(sqrt(A*A + B*B),
                     sinLat1*sinLat2 + cosLat1*cosLat2*cosDLon)
