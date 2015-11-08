import re
import datetime
from filter import Filter

class ExperienceFilter(Filter):
    @classmethod
    def run(cls, resume_attribute, query_attribute):
        grp = re.findall('[1-2]{1}[0-9]{3}|(?<= - )current|present|now|(?<=-)current|present|now|(?<=to)current|present|now', resume_attribute, re.IGNORECASE)
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
        return float(highest-lowest)/query_attribute