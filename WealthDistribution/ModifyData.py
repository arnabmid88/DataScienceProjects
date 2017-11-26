# -*- coding: utf-8 -*-
import numpy as np
def normalize(data):
    """
    Normalizes the data set. Expects a timeseries input
    """
    data = list(data)
    norm = np.array(list(d[1] for d in data), dtype="f8")
    mean = norm.mean()
    norm /= mean
    return zip((d[0] for d in data), norm)

def delta(first, second):
    """
    Returns an array of deltas for the two arrays.
    """
    first = list(first)
    years = yrange(first)
    first = np.array(list(d[1] for d in first), dtype="f8")
    second = np.array(list(d[1] for d in second), dtype="f8")
    # Not for use in writing
    if first.size != second.size:
        first = np.insert(first, [0,0,0,0], [None, None, None,None])
    diff = first - second
    return zip(years, diff)

def yrange(data):
    """
    Get the range of years from the dataset
    """
    years = set()
    for row in data:
        if row[0] not in years:
            yield row[0]
            years.add(row[0])