#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

count = 0;
for person in enron_data:
    if enron_data[person]["poi"] == True:
        count = count + 1

print str(enron_data["PRENTICE JAMES"]["total_stock_value"])
print str(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print str(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

most_money = 0;
user = "";
for person in enron_data:
    if enron_data[person]["total_payments"] > most_money:
        most_money = enron_data[person]["total_payments"]
        user = person

print most_money
print user

print enron_data["LAY KENNETH L"]["total_payments"]
print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["FASTOW ANDREW S"]["total_payments"]

import math
import numpy as np

salary = 0;
email = 0;
for person in enron_data:
    if np.isnan(enron_data[person]["email_address"]) == False:
        email = email + 1
    if np.isnan(enron_data[person]["salary"]) == False:
        salary = salary + 1

print str(salary)
print str(email)

print str(count)
