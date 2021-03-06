from filter import Filter

class CollectionFilter(Filter):
    @classmethod
    def run(cls, resume_attribute, query_attribute):
        if isinstance(query_attribute, basestring):
            query_attribute = [x.strip() for x in query_attribute.split(',')]

        if not resume_attribute:
            return 0

        score = 0
        resume_attribute = resume_attribute.split('\n')
        for element in query_attribute:
            if element.lower() in resume_attribute:
                score += 1.0 / len(query_attribute)
        return score