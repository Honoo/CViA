import json, os, subprocess

DIR = os.path.dirname(__file__)
PARSER_LIB_PATH = os.path.abspath(os.path.join(DIR, '../vendor/cv-parser/parse.js'))
OUTPUT_DIR = os.path.abspath(os.path.join(DIR, '../vendor/cv-parser/compiled'))


class CVParser(object):
    def __init__(self):
        """Utility class, do not instantiate."""
        return NotImplemented

    @classmethod
    def parse(cls, path):
        """Parse a file into json and return if the parsing is successful."""
        if not os.path.exists(path):
            raise Exception("Specified file: %s does not exist" % path)
        with open(os.devnull, 'wb') as devnull:
            # discard stdout and stderr
            process = subprocess.Popen(['node', PARSER_LIB_PATH, path], stdout=devnull, stderr=devnull)
            process.communicate()
            return process.returncode == 0

    @classmethod
    def parse_and_get_content(cls, path):
        """Parse a file and return its json content."""
        result = cls.parse(path)
        if not result:
            raise Exception("Unknown error occured while processing %s" % path)
        expected_path = os.path.abspath(os.path.join(OUTPUT_DIR, os.path.basename(path) + '.json'))
        with open(expected_path, 'r') as f:
            return json.load(f)


if __name__ == '__main__':
    print CVParser.parse_and_get_content(os.path.expanduser('~/tmp2/garena.pdf'))
