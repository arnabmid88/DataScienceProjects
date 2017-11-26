# -*- coding: utf-8 -*-
import csv
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter
from itertools import groupby
def getDataSetUsingCSV(path, country="United States"):
    """Extract the data for the country provided. Default is United States."""
    with open(path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        if country:
            for row in filter(lambda row: row['Country']==country, reader):
                yield row
        else:
            for row in reader:
                yield row
def getDataSetUsingDictReader(path, include):
    column = 'Average income per tax unit'
    with open(path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        key = itemgetter('Country')
        # Use groupby: memory efficient collection by country
        for key, values in groupby(reader, key=key):
            # Only yield countries that are included
            if key in include:
                yield key, [(int(value['Year']),float(value[column])) for value in values if value[column]]
                
def timeseries(data, column):
    """Creates a year based time series for the given column."""
    for row in filter(lambda row: row[column], data):
        yield (int(row["Year"]), row[column])

def extract_years(data):
    for country in data:
        for value in country[1]:
            yield value[0]

def extract_series(data, years):
    for country, cdata in data:
        cdata = dict(cdata)
        series = [cdata[year] if year in cdata else None for year in years]
        yield {
                'name': country,
                'data': series,
                }
