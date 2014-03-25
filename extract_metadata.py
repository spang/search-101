import re
import sys
import json

from glob import glob


def main():
    for filename in glob('gutentexts/*.txt'):
        print filename
        meta_filename = '_'.join([filename, 'meta.json'])
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
            r'^(?:Release|Posting) Date: (.*?)(?: \[(?:EBook|Etext) #[0-9]+.*)?$',
            text, flags=re.M).groups()[0].strip().decode(encoding)
        language = re.search(r'^Language: (.*)$', text,
                             flags=re.M).groups()[0].strip().decode(encoding)

        d = dict(title=title, author=author, language=language,
                 release_date=release_date, encoding=encoding)

        with open(meta_filename, 'w') as meta_file:
            json.dump(d, meta_file, encoding='utf-8')

if __name__ == '__main__':
    sys.exit(main())
