import os

from CVParser.cv_parser import CVParser
from JobMatcher.job_matcher import JobMatcher

resume = CVParser.parse_and_get_content(os.path.abspath('pdfs/LinkedIn/PraveenDeorani.pdf'))

print resume

# Write resume.txt to file
# f = open('resume.txt', 'w')
# f.write(str(resume))
# f.close()

print JobMatcher.score(resume, JobMatcher.load_json(os.path.abspath('JobMatcher/query.json')))