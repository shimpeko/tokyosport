import requests
import unicodedata
from tablestripper import TableStripper

r = requests.get('https://yoyaku.sports.metro.tokyo.jp/web/html/kouenichiran110201.htm')
ts = TableStripper()
ts.feed(r.content.decode('shift_jis'))
for row in ts.get_rows():
    if len(row) == 18:
        row.insert(4, "")
    if len(row) > 18:
        print(row[5:])
        print(row[0] + row[4])
