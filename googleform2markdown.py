import sys
import csv


class GuidoEntry:
    def __init__(self, timestamp, long_title, short_title=None):
        self.long_title = long_title
        self.short_title = (short_title or long_title[:5]).replace('-', '_').lower()
        self.post_id = f'{timestamp}-{self.short_title}.md'
        self.url = None
        self.desc = None
        self.img = None
        self.langs = []
        self.tags = []
        self.domain_genre = []
        self.refs_links = []

        self.timestamp = timestamp


if __name__ == '__main__':
    infile = sys.argv[1]
    # infile = './Guido Contribution Form (Responses) - Form Responses 1.tsv'
    # infile = './Guido Contribution Form (Responses) - Form Responses 1.csv'

    # oldpostpath = sys.argv[2]

    # outpath = sys.argv[3]
    outpath = 'out_test'

    old_posts = {}  # TODO

    new_posts = {}

    with open(infile) as f:
        reader = csv.reader(f)
        headers = next(reader)
        for line in reader:
            _entry = {}
            for key, value in zip(headers, line):
                _entry[key.split()[0]] = value
            date = _entry['Timestamp'].split(' ')[0].replace('/', '-')
            long_title = _entry['Title'].strip()
            short_title = _entry.get('Short')
            entry = GuidoEntry(date, long_title, short_title=short_title)
            entry.url = _entry['Guidelines']
            entry.desc = _entry['Description']
            for tag in _entry['Categories'].replace(',', '\n').split('\n'):
                entry.tags.append(tag.strip())
            for lang in _entry['Languages'].replace(',', '\n').split('\n'):
                entry.langs.append(lang.strip())
            for gen in _entry['Domains'].replace(',', '\n').split('\n'):
                entry.domain_genre.append(gen.strip())
            for ref in _entry['References,'].split('\n'):
                entry.refs_links.append(ref.strip())

            if entry.post_id not in old_posts:  # TODO: what to do for updates (with new timestamp) of an already existing scheme?
                new_posts[entry.post_id] = entry

    for post_id, entry in new_posts.items():
        filename = f'{outpath}/{post_id}'
        # TODO: check if file exists
        with open(filename, 'w') as f:
            f.write('---\nlayout: post\ntitle: ')
            f.write(entry.long_title)
            f.write('\ncategories: [')
            f.write(', '.join(entry.tags) if entry.tags else '//')
            f.write(']\n---\n\n')
            f.write('<!--- Main URL --->\n')
            f.write('[Link to Annotation Guidelines](')
            f.write(entry.url)
            f.write(')\n\n')
            f.write('<!--- Languages --->\n')
            for lang in entry.langs:
                f.write(f'* {lang}\n')
            f.write('\n')
            if entry.img is not None:
                f.write('<!-- Teaser image --->\n')
                f.write('<img src="" alt="teaser image" width="600" />\n')
            f.write('<!-- Description --->\n')
            f.write('# Description\n')
            f.write(entry.desc)
            f.write('\n\n')
            f.write('<!-- Domains and Genres --->\n')
            f.write('# Domains and Genres\n')
            for gen in entry.domain_genre:
                f.write(f'* {gen}\n')
            f.write('\n')
            f.write('\n\n')
            f.write('<!-- Any further references, links etc. --->\n')
            f.write('# References\n')
            for ref in entry.refs_links:
                f.write(f'* {ref}\n')
            f.write('\n')
