from pymongo import MongoClient
import csv

mongo = MongoClient()

db = mongo.undp

collection = db.gsc
collection.remove({})


def parse():
    print "Importing data..."

    with open('data/undpGenderSurveyOfCorruption.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # Skip the header rows
        next(reader, None)

        for row in reader:
            doc = {
                "surveyee": build_surveyee_doc(row),
                "q1": build_q1_doc(row),
                "q2": build_q2_doc(row),
                "q3": {
                    "question": "How prevalent do you believe corruption is in the civil service of your country?",
                    "answer":  row[18]
                },
                "q4": {
                    "question": "Have you ever witnessed corruption in your current workplace?",
                    "answer":  convert_to_int(row[19])
                },
                "q5": build_q5_doc(row),
                "q7": {
                    "question": "In your current workplace, have you ever been asked to participate in corrupt practices?",
                    "answer": convert_to_int(row[28])
                },
                "q8": build_q8_doc(row),
                "q13": build_q13_doc(row)
            }

            collection.insert(doc)

    print "Done."


def build_surveyee_doc(row):
    doc = {
        "gender": row[71],
        "ethnicity": row[72],
        "age": {
            "from": row[73],
            "to": row[73]
        },
        "employment": {
            "level":  row[75],
            "institution":  row[76],
            "position":  row[77],
        },
        "education":  row[78],
        "income":  row[79],
        "municipallity":  row[80],
        "region":  row[81]
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

        },
        "followup":{
            "question": "Did you report the corruption?",
            "answer":  convert_to_int(row[26]),
            "reason": row[27]
        }
    }

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

        },
        "followup": {
            "question": "Did you report the corruption described?",
            "answer":  convert_to_int(row[35]),
            "reason": row[36]
        }
    }

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


def build_q13_doc(row):
    doc = {
        "question": "In your opinion, do men and women enjoy the same working conditions within the civil service?",
        "answers": {
            "a1": {
                "text": "Women and men enjoy the same recruitment requirements (such as exam results, qualifications, age, level)",
                "value":  convert_to_int(row[58])
            },
            "a2": {
                "text": "Women and men enjoy the same salary and remuneration, including overtime",
                "value":  convert_to_int(row[59])
            },
            "a3": {
                "text": "Women and men are subject to the same promotion procedures",
                "value":  convert_to_int(row[60])
            },
            "a4": {
                "text": "Women and men work the same hours",
                "value":  convert_to_int(row[61])
            },
            "a5": {
                "text": "Women and men enjoy the same training opportunities",
                "value":  convert_to_int(row[62])
            },
            "a6": {
                "text": "Women and men enjoy the same professional development opportunities",
                "value":  convert_to_int(row[63])
            },
            "a7": {
                "text": "Women and men are subject to the same retrenchment policies / procedures",
                "value":  convert_to_int(row[64])
            },
            "a8": {
                "text": "Women and men are subject to the same retirement regulations",
                "value":  convert_to_int(row[65])
            },
            "a9": {
                "text": "Women and men are subject to the same redundancy packages",
                "value":  convert_to_int(row[66])
            },
            "a10": {
                "text": "Women and men are subject to the same disciplinary measures",
                "value":  convert_to_int(row[67])
            }
        }
    }

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

parse()
