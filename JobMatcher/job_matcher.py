import re
import datetime
import os
import json

RESUME_PATH = '/Users/yosriady/CViA/JobMatcher/resume.json'
QUERY_PATH = '/Users/yosriady/CViA/JobMatcher/query.json'

# Opens and parses JSON file to Python dictionary
def load_json(filepath):
    filepath = os.path.expanduser(filepath)
    with open(filepath) as data_file:
        data = json.load(data_file)
    return data

# Returns individual and total scores
def score(resume, query):
    scores = {
        'skills': score_skills(resume['skills'].lower(), query['skills']),
        'education': score_education(resume['education'], query['education']),
        'experience': score_experience(resume['experience'], query['experience'])
    }
    scores['total'] = sum(scores.values())
    return scores

def score_skills(applicant_skills, skills):
    score = 0
    for skill in skills:
        if skill.lower() in applicant_skills:
            score += 1.0 / len(skills)
    return score

def score_education(applicant_education, educations):
    applicant_education = applicant_education.lower()
    educations = map(lambda e: e.lower(), educations)

    corpus = {
        'bachelors': ['bachelor', 'bsc', 'bs'],
        'masters': ['master', 'msc', 'ms'],
        'phd': ['postdoc', 'phd']
    }
    score = 0
    for education in educations:
        if (corpus[education] is not None) & (any(word in applicant_education for word in corpus[education])):
            score += 1.0 / len(educations)
    return score

def score_experience(applicant_experience, experience):
    grp = re.findall('[1-2]{1}[0-9]{3}|(?<= - )current|present|now|(?<=-)current|present|now|(?<=to)current|present|now', applicant_experience.lower(), re.IGNORECASE)
    highest = 0
    lowest = datetime.datetime.now().year
    for g in grp:
        if g == 'present' or g == 'current' or g=='now':
            highest = datetime.datetime.now().year
        else:
            if int(g) < lowest:
                lowest = int(g)
            if int(g) > highest:
                highest = int(g)

    return float(highest-lowest)/experience

# Usage
resume = load_json(RESUME_PATH)
query = load_json(QUERY_PATH)
scores = score(resume, query)
print scores