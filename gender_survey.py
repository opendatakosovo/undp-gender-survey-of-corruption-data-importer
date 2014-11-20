from pymongo import MongoClient
import os
import csv

mongo = MongoClient()

db = mongo.undp

collection = db.gendersurvey

def parse():
    print "YOOOOOO"

    with open('data/undpGenderSurveyOfCorruption.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        for row in reader:
            print row


parse()