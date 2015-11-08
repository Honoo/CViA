from sources.json_data_source import JSONDataSource
from filters.education_filter import EducationFilter
from filters.experience_filter import ExperienceFilter
from filters.skills_filter import SkillsFilter
from filters.languages_filter import LanguagesFilter

class JobMatcher(object):
    def __init__(self, query, weights={}):
        self.query = query
        self.weights = weights

    # Returns individual and total scores
    def score(cls, resume):
        scores = {}
        for filter in cls.steps():
            attribute = filter.__name__.replace("Filter", "").lower()
            scores[attribute] = filter.run(resume[attribute].lower(), cls.query[attribute])
        scores = cls.weight(scores)
        scores['total'] = sum(scores.values())
        return {
            'name': resume['name'],
            'id': resume['id'],
            'score': scores
        }

    # Declarative steps of the pipeline
    def steps(cls):
        return [
            EducationFilter,
            ExperienceFilter,
            SkillsFilter,
            LanguagesFilter
        ]

    # Returns scores weighted by user-specified weights
    def weight(cls, scores):
        for attribute in scores.keys():
            if attribute in cls.weights:
                scores[attribute] = cls.weights[attribute] * scores[attribute]
        return scores
