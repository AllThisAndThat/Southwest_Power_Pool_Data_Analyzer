"""
Author: Lucas Hudson
Date: 5/28/22
Goal: To learn and review python
Task: Collect data from SPP and do something
    Parse load data for review
        Take every csv file from the year 2022
            test with manually downloaded files
            python needs to access website
        Take the time column once. 
        Take the OKGE column for every file
        Compile data
    Plot data
    Make best fit

Brainstorm
    1. Collect data from .csv or website to plot information
    2. Take load data and make my own best fit (even if horribly wrong)
    3. Use wind data to make future wind production predictions
    4. Learn fault and distances to fault calculations

"""
from parse_load_data import parse_year
# import parse_load_data

def main():
    load_19 = parse_year(2019)

    for data in load_19:
        data.load_print()
        pass


if __name__ == "__main__":
   main()