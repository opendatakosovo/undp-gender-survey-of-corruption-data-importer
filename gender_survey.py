from pymongo import MongoClient
import os
import csv

mongo = MongoClient()

db = mongo.undp

collection = db.gendersurvey
collection.remove({})
def parse():
    print "YOOOOOO"

    with open('data/undpGenderSurveyOfCorruption.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        for row in reader:

            doc = {
            	"surveyee":{
            		"gender": "male",
            		"ethnicity": "Albanian",
            		"age": {
            			"from": 20,
            			"to": 29
            		}
            		
            	},
                "q1": {
                	"question": "Which of these practices within the workplace do you think are corrupt?",
                	"answers": {
                		"a1":{
                			"text": "Accepting gifts or hospitality from a civil servant",
                			"value": convert_to_boolean(row[0]),
                		},
                		"a2":{
                			"text": "Taking supplies or materials from work for home use",
                			"value": convert_to_boolean(row[1]),
                		},
						"a3":{
							"text": "Paying or receiving rewards for keeping silent about workplace issues",
							"value": convert_to_boolean(row[2]),		
						},
						"a4":{
							"text": "Performing or receiving sexual favors in exchange for promotion or money",
							"value": convert_to_boolean(row[3]),

						},
						"a5":{
							"text": "Paying or receiving payment for a promotion or permanent job within the civil service",
							"value": convert_to_boolean(row[4]),

						},
						"a6":{
							"text": "Paying or receiving a payment for awarding contracts or positions", 
							"value": convert_to_boolean(row[5]),

						},
						"a7":{
							"text":  "Not declaring a conflict of interest when recruiting staff or awarding contracts",
							"value": convert_to_boolean(row[6]),

						},
						"a8":{
							"text": "Not working required hours",
							"value": convert_to_boolean(row[7]),

						},
						"a9":{
							"text": "Leaving work early without permission",
							"value": convert_to_boolean(row[8]),

						},
						"a10":{
							"text":  "Flirting with a colleague",
							"value": convert_to_boolean(row[9]),

						},
						"a11":{
							"text": "Asking friends who are well connected for favors to help your government work",
							"value": convert_to_boolean(row[10]),

						},
						"a12":{
							"text": "Claiming reimbursements to attend private functions hosted by a work colleague",
							"value": convert_to_boolean(row[11]),

						},
                	}
                },
               
						
                "q2": {
					
                },
                "q5": {
                },
                "q8": {
                },
                "q13": {
                },
                

                "question_2": {
                    "q2_a": convert_to_boolean(row[12]),
                    "q2_b": convert_to_boolean(row[13]),
                    "q2_c": convert_to_boolean(row[14]),
                    "q2_d": convert_to_boolean(row[15]),
                    "q2_e": convert_to_boolean(row[16]),
                    "q2_f": convert_to_boolean(row[17]),
                },
                "question_3": convert_to_boolean(row[18]),
                "question_4": convert_to_boolean(row[19]),
                "question_5": {
                     "q5_a": convert_to_boolean(row[20]),
                     "q5_b": convert_to_boolean(row[21]),
                     "q5_c": convert_to_boolean(row[22]),
                     "q5_d": convert_to_boolean(row[23]),
                     "q5_e": convert_to_boolean(row[24]),
                     "q5_f": convert_to_boolean(row[25]),
                },
                "question_6": {
                    "q6": convert_to_boolean(row[26]),
                    "q6_jo": convert_to_boolean(row[27]),
                },
				"question_7": convert_to_boolean(row[28]),
			
				"question_8":{
					"q8_a": convert_to_boolean(row[29]),
           			"q8_b": convert_to_boolean(row[30]),
           			"q8_c": convert_to_boolean(row[31]),
            		"q8_d": convert_to_boolean(row[32]),
            		"q8_e": convert_to_boolean(row[33]),
            		"q8_f": convert_to_boolean(row[34]),
				},
				"question_9":{
	 				"q9": convert_to_boolean(row35]),
           			"q9_jo": convert_to_boolean(row36]),
				},
				
            
            	"question_10":{
					"q10_a": convert_to_boolean(row37]),
				    "q10_b": convert_to_boolean(row38]),
				    "q10_c": convert_to_boolean(row39]),
				    "q10_d": convert_to_boolean(row40]),
				    "q10_e": convert_to_boolean(row41]),
				    "q10_f": convert_to_boolean(row42]),
				    "q10_g": convert_to_boolean(row43]),
					},
				"question_11":{
					"q11_a": convert_to_boolean(row44]),
				    "q11_b": convert_to_boolean(row45]),
				    "q11_d": convert_to_boolean(row46]),
				    "q11_e": convert_to_boolean(row47]),
				    "q11_f": convert_to_boolean(row48]),
				    "q11_g": convert_to_boolean(row49]),
				    "q11_h": convert_to_boolean(row50]),
				    "q11_i": convert_to_boolean(row51]),
				    "q11_j": convert_to_boolean(row52]),
				    "q11_k": convert_to_boolean(row53]),

				},
				"question_12":{
		        	'q12_a': convert_to_boolean(row[54]),
				    'q12_b': convert_to_boolean(row[55]),
				    'q12_c': convert_to_boolean(row[56]),
				    'q12_d': convert_to_boolean(row[57]),
		        },
		        "question_13":{
				    "q13_a": convert_to_boolean(row[58]),
				    "q13_b": convert_to_boolean(row[59]),
				    "q13_c": convert_to_boolean(row[60]),
				    "q13_d": convert_to_boolean(row[61]),
				    "q13_e": convert_to_boolean(row[62]),
				    "q13_f": convert_to_boolean(row[63]),
				    "q13_g": convert_to_boolean(row[64]),
				    "q13_h": convert_to_boolean(row[65]),
				    "q13_i": convert_to_boolean(row[66]),
				    "q13_j": convert_to_boolean(row[67]),
		        },
		        "question_14": convert_to_boolean(row68]),
		        "question_15":{
				    "q15": convert_to_boolean(row69]),
				    "q15_a": convert_to_boolean(row70]
		        },
		        "question_16": convert_to_boolean(row[71]),
		        "question_17": convert_to_boolean(row[72]),
		        "question_18": convert_to_boolean(row[73]),
		        "question_19": convert_to_boolean(row[74]),
		        "question_20": convert_to_boolean(row[75]),
		        "question_21": convert_to_boolean(row[76]),
		        "question_22": convert_to_boolean(row[77]),
		        "question_23": convert_to_boolean(row[78]),
		        "question_24": convert_to_boolean(row[79]),
		        "question_25": convert_to_boolean(row[80]),
		        "question_26": convert_to_boolean(row[81]),            
            }
            collection.insert(doc)   

def convert_to_boolean(data_string):

    if data_string == "Yes":
        return 1
    elif data_string == "No":
        return 0
    else:
        return data_string

parse()




