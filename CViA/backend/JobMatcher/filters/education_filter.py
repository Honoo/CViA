from filter import Filter

class EducationFilter(Filter):
    @classmethod
    def run(cls, resume_attribute, query_attribute):
        query_attribute = map(lambda e: e.lower(), query_attribute)

        corpus = {
            'bachelors': ['bachelor', 'bsc', 'bs'],
            'masters': ['master', 'msc', 'ms'],
            'phd': ['postdoc', 'phd']
        }
        score = 0
        for education in query_attribute:
            if (corpus[education] is not None) & (any(word in resume_attribute for word in corpus[education])):
                score += 1.0 / len(query_attribute)
        return score