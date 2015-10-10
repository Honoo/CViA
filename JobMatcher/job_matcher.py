import re
import datetime
import os
import json

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

class JobMatcher(object):
    AVAILABLE_ATTRIBUTES = ['education', 'experience', 'skills', 'languages']

    def __init__(self):
        return NotImplemented

    # Opens and parses JSON file to Python dictionary
    @classmethod
    def load_json(cls, filepath):
        with open(filepath) as data_file:
            data = json.load(data_file)
        return data

    # Returns individual and total scores
    @classmethod
    def score(cls, resume, query):
        scores = {}
        scored_attributes = set(query.keys()).intersection(cls.AVAILABLE_ATTRIBUTES)
        for attribute in scored_attributes:
            scores[attribute] = getattr(cls, 'score_%s' % attribute)(resume[attribute], query[attribute])
        scores['total'] = sum(scores.values())
        return {
            'name': resume['name'],
            'score': scores
        }

    @classmethod
    def score_education(cls, applicant_education, educations):
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

    @classmethod
    def score_experience(cls, applicant_experience, experience):
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

    @classmethod
    def score_collection(cls, applicant_collection, collection):
        if not applicant_collection:
            return 0

        score = 0
        applicant_collection = applicant_collection.lower().split('\n')
        for language in collection:
            if language.lower() in applicant_collection:
                score += 1.0 / len(collection)
        return score

    score_skills = score_collection
    score_languages = score_collection


# Usage
if __name__ == '__main__':
    RESUME_PATH = 'resume.json'
    QUERY_PATH = 'query.json'
    resume = JobMatcher.load_json(RESUME_PATH)
    query = JobMatcher.load_json(QUERY_PATH)
    scores = JobMatcher.score(resume, query)
    print scores
