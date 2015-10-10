import sys
import os
import collections

from CVParser.cv_parser import CVParser
from JobMatcher.job_matcher import JobMatcher

# CLI Arguments
pdf_dir = sys.argv[1]
query_path = sys.argv[2]

for filename in os.listdir(os.path.abspath(pdf_dir)):
    resume = CVParser.parse_and_get_content(os.path.abspath(pdf_dir) + "/" +filename)
    print JobMatcher.score(resume, JobMatcher.load_json(os.path.abspath(query_path)))

# Usage
# python main.py pdfs/LinkedIn JobMatcher/query.json