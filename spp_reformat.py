#!/usr/bin/env python
'''Take SPP data reformat and store in new file'''
__author__ = "Lucas Hudson"
__email__ = "lucaslorenhudson@gmail.com"
__status__ = "Prototype"

"""
1. Take load data
2. Take generation data
3. Save to a new file
"""

from parse_load_data import parse_year

year_range = range(2018, 2020+1)

load_times = []
for year in year_range:
    load_times.append(parse_year(year))

print(load_times)