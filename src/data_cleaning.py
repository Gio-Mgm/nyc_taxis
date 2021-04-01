#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Foobar.py: Description of what foobar does."""

__author__ = "Antoine,  Giovanny"
__copyright__ = "Copyright 2021, The Taxi Project"
__credits__ = ["Antoine,  Giovanny"]
__version__ = "1.0"
__status__ = "Production"

#Import des lirairies
import pandas as pd 
import numpy as np
import sys
from gpsutils import *


sys.path.append("../NYC-Taxi")

# Import Data
df = pd.read_csv("./data/01_raw/train.csv", index_col = 0)

print("Data import : check")

# Remove useless columns
df = df.drop(["store_and_fwd_flag","passenger_count"], axis=1)

# Create 'Day of week' column
df['pickup_dayofweek']= pd.DatetimeIndex(df.pickup_datetime).dayofweek

# Create 'part4h' column
df['pickup_part4h']= pd.DatetimeIndex(df.pickup_datetime).hour
df['pickup_part4h']= df.apply(lambda x: x.pickup_part4h // 4, axis=1)

print("Set colomns : check")
print("Calculated columns  : 33%")

# Create 'distance' column
df["distance"] = df.apply(
    lambda x: round(
        great_circle_distance(
            x.pickup_latitude, x.pickup_longitude, x.dropoff_latitude, x.dropoff_longitude
    )), axis=1
)
print("Calculated columns  : 66%")

#Create columns distancepertime
df["distancepertime"] = df.apply(
    lambda x: round(
        x.distance/x.trip_duration*3.6
    ), axis=1
)

# Remove outliers
df = df.drop(df[df.distancepertime > 150].index)
df = df.drop(df[df.distance > 100000].index)
df = df.drop(df[df.trip_duration > 70000].index)
    
print("Calculated columns  : check")

#Save data to CSV
df.to_csv('./data/02_intermediate/dirty_train.csv', encoding='utf-8')

print("Save Ready in /data folder")
