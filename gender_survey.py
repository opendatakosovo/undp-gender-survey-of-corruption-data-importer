from pymongo import MongoClient
import csv
import re

mongo = MongoClient()

db = mongo.undp

collection = db.gsc
collection.remove({})


def parse():
    print "\nImporting data..."

    with open('data/undpGenderSurveyOfCorruption.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # Skip the header rows
        next(reader, None)

        doc_count = 0
        for row in reader:
            doc = {
                "surveyee": build_surveyee_doc(row),
                "q1": build_q1_doc(row),
                "q2": build_q2_doc(row),
                "q3": build_q3_doc(row),
                "q4": build_q4_doc(row),
                "q5": build_q5_doc(row),
                "q6": build_q6_doc(row),
                "q7": build_q7_doc(row),
                "q8": build_q8_doc(row),
                "q9":  build_q9_doc(row),
                "q10": build_q10_doc(row),
                "q11": build_q11_doc(row),
                "q12": build_q12_doc(row),
                "q13": build_q13_doc(row),
                "q14": build_q14_doc(row),
                "q15": build_q15_doc(row),
            }

            collection.insert(doc)

            doc_count = doc_count + 1

    print "Done. Imported %i surveys.\n" % doc_count


def build_surveyee_doc(row):
    age_range = row[74]
    age = {}

    if age_range == '60+':
        age = { "from" : 60 }

    else:
        age_range = row[74].split(' ')[0]
        age = {
            "label": row[74], 
            "from" : int(age_range.split('-')[0]),
            "to" : int(age_range.split('-')[1]),
        }


    income_range = re.findall(r'\d+', row[80])
    income = {}

    if row[80] != "No answer / Refuse":

        if len(income_range) == 1 and row[80].startswith("Less"):
            income = {
                "label": row[80],
                "from" : int(income_range[0])
            }
        elif len(income_range) == 1:
            income = {
                "label": row[80],
                "to" : int(income_range[0]),
            }
        else:
            income = {
                "label": row[80],
                "from" : int(income_range[0]),
                "to" : int(income_range[1]),
            }
    else:
        income = { 
            "label": row[80]
        }

    doc = {
        "gender": row[72],
        "ethnicity": row[73],
        "age": age,
        "maritalstatus": row[75],
        "employment": {
            "level":  row[76],
            "institution":  row[77],
            "position":  row[78],
        },
        "education":  row[79],
        "income": income,
        "municipality":  row[81],
        "region":  row[82]
    }

    return doc


def build_q1_doc(row):
    doc = {
        "question": "Which of these practices within the workplace do you think are corrupt?",
        "answers": {
            "a1": {
                "text": "Accepting gifts or hospitality from a civil servant",
                "value":  convert_to_int(row[0]),
            },
            "a2": {
                "text": "Taking supplies or materials from work for home use",
                "value":  convert_to_int(row[1]),
            },
            "a3": {
                "text": "Paying or receiving rewards for keeping silent about workplace issues",
                "value":  convert_to_int(row[2]),
            },
            "a4": {
                "text": "Performing or receiving sexual favors in exchange for promotion or money",
                "value":  convert_to_int(row[3]),

            },
            "a5": {
                "text": "Paying or receiving payment for a promotion or permanent job within the civil service",
                "value":  convert_to_int(row[4]),

            },
            "a6": {
                "text": "Paying or receiving a payment for awarding contracts or positions",
                "value":  convert_to_int(row[5]),

            },
            "a7": {
                "text": "Not declaring a conflict of interest when recruiting staff or awarding contracts",
                "value":  convert_to_int(row[6]),

            },
            "a8": {
                "text": "Not working required hours",
                "value":  convert_to_int(row[7]),

            },
            "a9": {
                "text": "Leaving work early without permission",
                "value":  convert_to_int(row[8]),

            },
            "a10": {
                "text": "Flirting with a colleague",
                "value":  convert_to_int(row[9]),

            },
            "a11": {
                "text": "Asking friends who are well connected for favors to help your government work",
                "value":  convert_to_int(row[10]),

            },
            "a12": {
                "text": "Claiming reimbursements to attend private functions hosted by a work colleague",
                "value":  convert_to_int(row[11]),

            },
        }
    }

    return doc


def build_q2_doc(row):
    doc = {
        "question": "What forms of corruption do you believe exist across the entire civil service in your country?",
        "answers": {
            "a1": {
                "text": "Embezzlement, theft (including time theft not working required hours) and fraud",
                "value":  convert_to_int(row[12]),
            },
            "a2": {
                "text": "Extortion (including sexual extortion)",
                "value":  convert_to_int(row[13]),
            },
            "a3": {
                "text": "Nepotism, favoritism and patronage",
                "value":  convert_to_int(row[14]),
            },
            "a4": {
                "text": "Bribery",
                "value":  convert_to_int(row[15]),
            },
            "a5": {
                "text": "Abuse of discretionary powers",
                "value":  convert_to_int(row[16]),
            },
            "a6": {
                "text": "Trading in influence",
                "value":  convert_to_int(row[17]),
            },

        },
    }

    return doc


def build_q3_doc(row):
    doc = {
        "question": "How prevalent do you believe corruption is in the civil service of your country?",
        "answers":  {
            "a1": {
                "text": "Not prevalent",
                "value":  0,
            },
            "a2": {
                "text": "A bit prevalent",
                "value":  0,
            },
            "a3": {
                "text": "Somewhat prevalent",
                "value":  0,
            },
            "a4": {
                "text": "Prevalent",
                "value":  0,
            },
            "a5": {
                "text": "Very prevalent",
                "value":  0,
            }
        }
    }

    answer_key = "a" + row[18]
    doc['answers'][answer_key]['value'] = 1

    return doc


def build_q4_doc(row):
    doc = {
        "question": "Have you ever witnessed corruption in your current workplace?",
        "answers": {
            "a1": {
                "text": "No",
                "value":  0,
            },
            "a2": {
                "text": "Yes",
                "value":  0,
            }
        }
    }

    answer = convert_to_int(row[19])
    doc['answers']['a' + str(answer + 1)]['value'] = 1

    return doc


def build_q5_doc(row):
    doc = {
        "question": "What best describes the corruption you witnessed?",
        "answers": {
            "a1": {
                "text": "Embezzlement, theft (including time theft not working required hours) and fraud",
                "value":  convert_to_int(row[20]),
            },
            "a2": {
                "text": "Extortion (including sexual extortion)",
                "value":  convert_to_int(row[21]),
            },
            "a3": {
                "text": "Nepotism, favoritism and patronage",
                "value":  convert_to_int(row[22]),
            },
            "a4": {
                "text": "Bribery",
                "value":  convert_to_int(row[23]),
            },
            "a5": {
                "text": "Abuse of discretionary powers",
                "value":  convert_to_int(row[24]),
            },
            "a6": {
                "text": "Trading in influence",
                "value":  convert_to_int(row[25]),
            },

        }
    }

    return doc


def build_q6_doc(row):
    doc = {
        "question": "Did you report the corruption described?",
        "answers": {
            "a1": {
                "text": "No",
                "value":  0,
            },
            "a2": {
                "text": "Yes",
                "value":  0,
            },
            "a3": {
                "text": "Choose not to answer",
                "value":  0,
            },
        }
    }

    answer = convert_to_int(row[26])
    if answer != 'n/a':
        doc['answers']['a' + str(answer + 1)]['value'] = 1

        if answer == 0:
            doc['followup'] = build_followup_question_doc(row[27])

    else:
        doc['answers']['a3']['value'] = 1

    return doc


def build_q7_doc(row):
    doc = {
        "question": "In your current workplace, have you ever been asked to participate in corrupt practices?",
        "answers": {
            "a1": {
                "text": "No",
                "value":  0,
            },
            "a2": {
                "text": "Yes",
                "value":  0,
            }
        }
    }

    answer = convert_to_int(row[28])
    doc['answers']['a' + str(answer + 1)]['value'] = 1

    return doc


def build_q8_doc(row):
    doc = {
        "question": "What best describes the type of corruption you participated in?",
        "answers": {
            "a1": {
                "text": "Embezzlement, theft (including time theft not working required hours) and fraud",
                "value":  convert_to_int(row[29]),
            },
            "a2": {
                "text": "Extortion (including sexual extortion)",
                "value":  convert_to_int(row[30]),
            },
            "a3": {
                "text": "Nepotism, favoritism and patronage",
                "value":  convert_to_int(row[31]),
            },
            "a4": {
                "text": "Bribery",
                "value":  convert_to_int(row[32]),
            },
            "a5": {
                "text": "Abuse of discretionary powers",
                "value":  convert_to_int(row[33]),
            },
            "a6": {
                "text": "Trading in influence",
                "value":  convert_to_int(row[34]),
            },

        }
    }

    return doc


def build_q9_doc(row):
    doc = {
        "question": "Did you report the corruption described?",
        "answers": {
            "a1": {
                "text": "No",
                "value":  0,
            },
            "a2": {
                "text": "Yes",
                "value":  0,
            },
            "a3": {
                "text": "Choose not to answer",
                "value":  0,
            },
        }
    }

    answer = convert_to_int(row[35])
    if answer != 'n/a':
        doc['answers']['a' + str(answer + 1)]['value'] = 1

        if answer == 0:
            doc['followup'] = build_followup_question_doc(row[36])

    else:
        doc['answers']['a3']['value'] = 1

    return doc


def build_q10_doc(row):
    doc = {
        "question": "How does the civil service encourage men and women to speak out against corruption or a lack of transparency in management?",
        "answers": {
            "a1": {
                "text": "It has an established and functional workplace grievance mechanism",
                "value":  convert_to_int(row[37]),
            },
            "a2": {
                "text": "Information is available on laws and policies relating to corruption, accountability and good governance equally for men",
                "value":  convert_to_int(row[38]),
            },
            "a3": {
                "text": "Has a senior management team that is equally  supportive of men and women  employees",
                "value":  convert_to_int(row[39]),
            },
            "a3": {
                "text": "Gender equality considerations are included in all workplace policies",
                "value":  convert_to_int(row[40]),
            },
            "a4": {
                "text": "Has a gender responsive anti-corruption policy",
                "value":  convert_to_int(row[41]),
            },
            "a5": {
                "text": "Men and women employees that report corruption are protected from reprisals",
                "value":  convert_to_int(row[42]),
            },
            "a6": {
                "text": "Has established relationships with non-government organizations and government organizations working to fight against corrupti",
                "value":  convert_to_int(row[43]),
            },

        },
    }

    return doc

def build_q11_doc(row):
    doc = {
        "question": "Have workplace policies relating to your employment been made available to you?",
        "answers": {
            "a1": {
                "text": "Recruitment policies and requirements (such as exam results, qualifications, age, level)",
                "value":  convert_to_int(row[44]),
            },
            "a2": {
                "text": "Salary and remuneration policies including overtime",
                "value":  convert_to_int(row[45]),
            },
            "a3": {
                "text": "Promotion policies",
                "value": convert_to_int(row[46]),
            },
            "a3": {
                "text": "Working hours policies",
                "value": convert_to_int(row[47]),
            },
            "a4": {
                "text": "Training or professional development opportunities",
                "value": convert_to_int(row[48]),
            },
            "a5": {
                "text": "Retrenchment policies",
                "value": convert_to_int(row[49]),
            },
            "a6": {
                "text": "Retirement policies",
                "value": convert_to_int(row[50]),
            },
            "a7": {
                "text": "Redundancy policies",
                "value": convert_to_int(row[51]),
            },
            "a8": {
                "text": "Disciplinary measures",
                "value": convert_to_int(row[52]),
            },
            "a9": {
                "text": "Code of conduct",
                "value": convert_to_int(row[53]),
            },
            "a10": {
                "text":  "Anti-corruption policies",
                "value": convert_to_int(row[54]),
            }
        }
    }

    return doc

def build_q12_doc(row):
    doc = {
        "question": "How would you described the information provided in the policies and regulations?",
        "answers": {
            "a1": {
                "text": "The information provided was relevant to my situation",
                "value": convert_to_int(row[55]),
            },
            "a2": {
                "text": "The information was provided in a timely manner",
                "value": convert_to_int(row[56]),
            },
            "a3": {
                "text": "The information provided was accurate",
                "value": convert_to_int(row[57]),
            },
            "a4": {
                "text": "I could easily understand the information",
                "value": convert_to_int(row[58]),
            }
        }
    }

    return doc


def build_q13_doc(row):
    doc = {
        "question": "In your opinion, do men and women enjoy the same working conditions within the civil service?",
        "answers": {
            "a1": {
                "text": "Women and men enjoy the same recruitment requirements (such as exam results, qualifications, age, level)",
                "value":  convert_to_int(row[59])
            },
            "a2": {
                "text": "Women and men enjoy the same salary and remuneration, including overtime",
                "value":  convert_to_int(row[60])
            },
            "a3": {
                "text": "Women and men are subject to the same promotion procedures",
                "value":  convert_to_int(row[61])
            },
            "a4": {
                "text": "Women and men work the same hours",
                "value":  convert_to_int(row[62])
            },
            "a5": {
                "text": "Women and men enjoy the same training opportunities",
                "value":  convert_to_int(row[63])
            },
            "a6": {
                "text": "Women and men enjoy the same professional development opportunities",
                "value":  convert_to_int(row[64])
            },
            "a7": {
                "text": "Women and men are subject to the same retrenchment policies / procedures",
                "value":  convert_to_int(row[65])
            },
            "a8": {
                "text": "Women and men are subject to the same retirement regulations",
                "value":  convert_to_int(row[66])
            },
            "a9": {
                "text": "Women and men are subject to the same redundancy packages",
                "value":  convert_to_int(row[67])
            },
            "a10": {
                "text": "Women and men are subject to the same disciplinary measures",
                "value":  convert_to_int(row[68])
            }
        }
    }

    return doc

def build_q14_doc(row):
    doc = {
        "question": "Do discretionary powers exist within the public administration whereby management can grant additional pay or benefits to certain employees?",
        "answers": {
            "a1": {
                "text": "No",
                "value":  0,
            },
            "a2": {
                "text": "Yes",
                "value":  0,
            }
        }
    }

    answer = convert_to_int(row[69])
    doc['answers']['a' + str(answer + 1)]['value'] = 1

    return doc

def build_q15_doc(row):
    doc = {
        "question": "If you answered yes to the previous question, is the criteria for granting additional pay and benefits made available to all staff?",
        "answers": {
            "a1": {
                "text": "No",
                "value":  0,
            },
            "a2": {
                "text": "Yes",
                "value":  0,
            },
            "a3": {
                "text": "Choose not to answer",
                "value":  0,
            },
        }
    }

    answer = convert_to_int(row[70])
    if answer != 'n/a':
        doc['answers']['a' + str(answer + 1)]['value'] = 1
    else:
        doc['answers']['a3']['value'] = 1

    doc['followup'] = build_followup_question_15_doc(row[71])

    return doc


def  convert_to_int(data_string):
    if data_string == "Yes":
        return 1
    elif data_string == "No":
        return 0
    elif data_string == "No, I did not report it because":
        return 0
    else:
        return "n/a"


def convert_followup_answer_to_key_index(answer):
    if answer == "Afraid of retaliation":
        return 1

    elif answer == "Did not want to get involved":
        return 2

    elif answer == "Does not work":
        return 3

    elif answer == "The risk of losing my job":
        return 4

    elif answer == "Do not know":
        return 5

    else:
        return 6


def build_followup_question_doc(answer):

    doc = {
        "question": "No, I did not report it because",
        "answers": {
            "a1": {
                "text": "Afraid of retaliation",
                "value":  0,
            },
            "a2": {
                "text": "Did not want to get involved",
                "value":  0,
            },
            "a3": {
                "text": "Does not work",
                "value":  0,
            },
            "a4": {
                "text": "The risk of losing my job",
                "value":  0,
            },
            "a5": {
                "text": "Do not know",
                "value":  0,
            },
            "a6": {
                "text": "Choose not to answer",
                "value":  0,
            }
        }
    }

    followup_key_index = convert_followup_answer_to_key_index(answer)
    doc['answers']['a' + str(followup_key_index)]['value'] = 1

    return doc


def build_followup_question_15_doc(answer):
    doc = {
        "question": "Do you think they are equally accessible for women and men?",
        "answers": {
            "a1": {
                "text": "No",
                "value":  0,
            },
            "a2": {
                "text": "Yes",
                "value":  0,
            },
            "a3": {
                "text": "Choose not to answer",
                "value":  0,
            },
        }
    }

    answer_index = convert_to_int(answer) 
    if answer_index != 'n/a':
        doc['answers']['a' + str(answer_index + 1)]['value'] = 1
    else:
        doc['answers']['a3']['value'] = 1

    return doc

parse()
