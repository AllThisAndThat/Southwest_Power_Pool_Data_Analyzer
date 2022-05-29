"""
Author: Lucas Hudson
Date: 5/28/22
Goal: Parse .csv files
"""
import csv

from load_time import LOAD_TIME

def parse_year(year):
    times = []
    loads = []
    load_time = []
    months_per_year = 12
    for month in range(1 , months_per_year + 1):
        parse_month(year,month,times,loads)
    for index in range(len(times)):
        load_time.append(LOAD_TIME(times[index], loads[index]))
    
    return load_time

        
def parse_month(year,month,times,loads):
    rows = []
    FILE_NAME = '%d\HOURLY_LOAD-'%year
    SPP_MEMBER = 'OKGE'

    if month < 10:
        FILE_NAME = '%s%d0%d.csv'%(FILE_NAME,year,month)
    else:
        FILE_NAME = '%s%d%d.csv'%(FILE_NAME,year,month)
    
    with open(FILE_NAME, mode='r') as month_data:
        csvreader = csv.reader(month_data)

        # Get top fields and strips whitespace
        fields = next(csvreader)
        for field in range(len(fields)):
            fields[field] = fields[field].strip()
            

        # Format remaining data in list
        for row in csvreader:
            rows.append(row)

        # Get times
        for row in rows: 
            times.append(row[0])

        # Get SPP member load data
        SPP_MEMBER_INDEX = fields.index(SPP_MEMBER)
        for row in rows:
            loads.append(row[SPP_MEMBER_INDEX])
