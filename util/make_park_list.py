import requests
import unicodedata
import re
import json
import configparser
from tablestripper import TableStripper

config = configparser.ConfigParser()
config.read('park_list_url.ini')

r = requests.get(config['default']['url'])

ts = TableStripper()
ts.feed(r.content.decode('shift_jis'))

parks = {}
ro = re.compile('.*-->(.*)$')

for row in ts.get_rows():
    # for 26大島小松川B
    if len(row) == 18:
        row.insert(4, "")
    # exclude non park data
    if len(row) > 18 and row[0] != '':
        park = {}
        park['id'] = int(unicodedata.normalize('NFKC', row[0]))
        match = ro.match(row[2].replace('\r\n', ''))
        if match:
            park['name'] = match.group(1)
        c = list(map(lambda s: unicodedata.normalize('NFKC', s), row[5:]))
        counts = [int(cnt) if cnt != '' else 0 for cnt in c]
        park['baseball'] = counts[0]
        park['baseball_mini'] = counts[3]
        park['tennis_hard'] = counts[6]
        park['tennis_omni'] = counts[9]
        park['soccer'] = counts[12]
        park['soccer_mini'] = counts[13]
        parks[park['id']] = park

print(json.dumps(parks, ensure_ascii=False, indent=2))
