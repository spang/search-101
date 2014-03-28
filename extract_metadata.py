import os
import re
import sys
import json
import calendar

from glob import glob

from dateutil.parser import parse as parse_date


def main():
    for filename in glob('gutentexts/*.txt'):
        print filename
        meta_filename = ''.join([filename, '.json'])
        id_ = re.match('^([0-9]+)(?:[-]\d)?.txt$',
                       os.path.basename(os.path.split(filename)[1]))\
            .groups()[0]

        text = file(filename, 'r').read()
        encoding = re.search(r'^Character set encoding: (.*)$', text,
                             flags=re.M).groups()[0].strip()
        if encoding == "ISO-646-US (US-ASCII)":
            encoding = "ascii"
        title = re.search(r'^Title: (.*)$', text,
                          flags=re.M).groups()[0].strip().decode(encoding)
        author = re.search(r'^Author: (.*)$', text,
                           flags=re.M).groups()[0].strip().decode(encoding)
        # NOTE: I can't actually figure out how to match a literal ] in a
        # Python regex, go figure. We just wildcard it instead.
        release_date = re.search(
            r'^(?:Release|Posting) Date: (.*?)(?: \[(?:[Ee](?:[Bb]ook|[Tt]ext)) #[0-9]+.*)?$',
            text,
            flags=re.M).groups()[0].strip().decode(encoding)
        if release_date is not None:
            release_date = \
                calendar.timegm(parse_date(release_date).timetuple())
        language = re.search(r'^Language: (.*)$', text,
                             flags=re.M).groups()[0].strip().decode(encoding)
        try:
            content = text.decode(encoding=encoding)
        except UnicodeDecodeError:
            # sometimes people lie
            content = text.decode(encoding='latin-1')

        d = dict(id=id_, title=title, author=author, language=language,
                 release_date=release_date, content=content)

        with open(meta_filename, 'w') as meta_file:
            json.dump(d, meta_file, encoding='utf-8')

if __name__ == '__main__':
    sys.exit(main())
