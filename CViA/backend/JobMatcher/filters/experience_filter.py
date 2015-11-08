import re
import datetime
from filter import Filter

class ExperienceFilter(Filter):
    @classmethod
    def run(cls, resume_attribute, query_attribute):
        if query_attribute <= 0.001 or not isinstance(query_attribute, float):
            print "Error"
            return 0.0
        grp = re.findall('[1-2]{1}[0-9]{3}|(?<= - )current|present|now|(?<=-)current|present|now|(?<=to)current|present|now', resume_attribute, re.IGNORECASE)
        highest = 0
        lowest = datetime.datetime.now().year
        print grp
        for g in grp:
            if g == 'present' or g == 'current' or g=='now':
                highest = datetime.datetime.now().year
            else:
                if int(g) < lowest:
                    lowest = int(g)
                if int(g) > highest:
                    highest = int(g)
        score = float(highest-lowest)/query_attribute
        return 1 if score < 0 else score