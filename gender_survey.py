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

            doc = {
                "question_1": {
                    "q1_a": row[0],
                    "q1_b": row[1],
                    "q1_c": row[2],
                    "q1_d": row[3],
                    "q1_e": row[4],
                    "q1_f": row[5],
                    "q1_g": row[6],
                    "q1_h": row[7],
                    "q1_i": row[8],
                    "q1_j": row[9],
                    "q1_k": row[10],
                    "q1_l": row[11],
                },

                "question_2": {
                    "q2_a": row[12],
                    "q2_b": row[13],
                    "q2_c": row[14],
                    "q2_d": row[15],
                    "q2_e": row[16],
                    "q2_f": row[17],
                },
                "question_3": row[18],
                "question_4": row[19],
                "question_5": {
                     "q5_a": row[20],
                     "q5_b": row[21],
                     "q5_c": row[22],
                     "q5_d": row[23],
                     "q5_e": row[24],
                     "q5_f": row[25],
                },
                "question_6": {
                    "q6": row[26],
                    "q6_jo": row[27],
                },
				"question_7": row[28],
			
				"question_8":{
					"q8_a": row[29],
           			"q8_b": row[30],
           			"q8_c": row[31],
            		"q8_d": row[32],
            		"q8_e": row[33],
            		"q8_f": row[34],
				},
				"question_9":{
	 				"q9": row[35],
           			"q9_jo": row[36],
				},
				
            
            	"question_10":{
					"q10_a": row[37],
				    "q10_b": row[38],
				    "q10_c": row[39],
				    "q10_d": row[40],
				    "q10_e": row[41],
				    "q10_f": row[42],
				    "q10_g": row[43],
					},
				"question_11":{
					"q11_a": row[44],
				    "q11_b": row[45],
				    "q11_d": row[46],
				    "q11_e": row[47],
				    "q11_f": row[48],
				    "q11_g": row[49],
				    "q11_h": row[50],
				    "q11_i": row[51],
				    "q11_j": row[52],
				    "q11_k": row[53],

				},
				"question_12":{
		        	'q12_a': row[54],
				    'q12_b': row[55],
				    'q12_c': row[56],
				    'q12_d': row[57],
		        },
		        "question_13":{
				    "q13_a": row[58],
				    "q13_b": row[59],
				    "q13_c": row[60],
				    "q13_d": row[61],
				    "q13_e": row[62],
				    "q13_f": row[63],
				    "q13_g": row[64],
				    "q13_h": row[65],
				    "q13_i": row[66],
				    "q13_j": row[67],
		        },
		        "question_14": row[68],
		        "question_15":{
				    "q15": row[69],
				    "q15_a": row[70]
		        },
		        "question_16": row[71],
		        "question_17": row[72],
		        "question_18": row[73],
		        "question_19": row[74],
		        "question_20": row[75],
		        "question_21": row[76],
		        "question_22": row[77],
		        "question_23": row[78],
		        "question_24": row[79],
		        "question_25": row[80],
		        "question_26": row[81],            
            }
            print doc
      
'''
def convert_to_boolean(num):

    if num == "Yes":
        return true
    elif == "No":
        return false
    else:
        return num
'''
parse()
