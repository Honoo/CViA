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
    matcher = JobMatcher(query_path)
    print matcher.score(resume)

# Usage
# python main.py pdfs/LinkedIn JobMatcher/query.json