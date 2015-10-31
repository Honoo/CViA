import os

from CVParser.cv_parser import CVParser
from JobMatcher.job_matcher import JobMatcher

resume = CVParser.parse_and_get_content(os.path.abspath('../../pdfs/sample2.pdf'))
print resume
print JobMatcher.score(resume, JobMatcher.load_json(os.path.abspath('JobMatcher/query.json')))