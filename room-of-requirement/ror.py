'''
args:
    year month day time duration
    alternatively: 
        use rn for now and add duration 
        use td for today and add time and duration
    example:
    python3 ror.py 2024 03 20 8 2   // find me a classroom at 8 am on march 20th 2024 that I can use for 2 hours
    python3 ror.py rn 4              // -||- right now that I can use for 4 hours
    python3 ror.py td 10 6           // -||- today that I can use for 6 hours

'''

from ics import Calendar
import sys
import requests
from datetime import datetime, timedelta
from itertools import zip_longest

def parse_events(calendar, desired_time, duration):
    occupied_classrooms = set()
    desired_end_time = desired_time + duration
    for event in calendar.events:
        event_start = event.begin.datetime.replace(tzinfo=None)
        event_end = event.end.datetime.replace(tzinfo=None)
        if (event_start < desired_end_time) and (event_end > desired_time):
            occupied_classrooms.update(map(str.strip, event.location.split(',')))
    return occupied_classrooms

url = "https://cloud.timeedit.net/kth/web/stud02/ri.ics?sid=7&p=4&objects=353305.4%2C353278%2C353279%2C411281%2C353280%2C353274%2C353275%2C353276%2C373913%2C446809%2C353281%2C353283%2C353264%2C353272%2C353304%2C353269%2C353267%2C353266%2C353268%2C-1%2C353270.4%2C353271%2C353303%2C353299%2C353298%2C353347%2C353344%2C353343%2C353342%2C353382%2C353380%2C353384%2C353383%2C353381%2C353385%2C353386%2C353387%2C353388%2C353389%2C353397%2C-1%2C353396.4%2C353409%2C353399%2C353400%2C353402%2C353401%2C353398%2C353405%2C353407%2C353406%2C353408%2C353412%2C353414%2C353411%2C353413%2C399482%2C399465%2C399466%2C399472%2C399474%2C-1%2C399481.4%2C353326%2C353327%2C353328%2C353331%2C353333%2C353330%2C353340%2C353341%2C353339%2C353338%2C387925%2C387922%2C387929%2C387927&l=sv&e=2403&ku=19900&k=578E00997A5AF366F7BA048002F061A78E"
calendar = Calendar(requests.get(url).text)

if sys.argv[1] == "rn": 
    desired_time = datetime.now()
elif sys.argv[1] == "td":
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    hour = int(sys.argv[2])
    desired_time = datetime(year, month, day, hour, 0)
else:
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    day = int(sys.argv[3])
    hour = int(sys.argv[4])
    desired_time = datetime(year, month, day, hour, 0)

duration = timedelta(hours=float(sys.argv[-1]))

occupied_classrooms = parse_events(calendar, desired_time, duration)

all_classrooms = [
    "D1", "D2", "D3", "D31", "D32", "D33", "D34", "D35", "D36", "D37", "D41", "D42",
    "E1", "E2", "E3", "E31", "E32", "E33", "E34", "E35", "E36", "E51", "E52", "E53",
    "K1", "K2", "K53", "K51", "Q1", "Q11", "Q13", "Q15", "Q17", "Q2", "Q21", "Q22", 
    "Q24", "Q26", "Q31", "Q33", "Q34", "Q36", "U1", "U2", "U31", "U41", "U51", "U61", 
    "V1", "V11", "V12", "V21", "V22", "V23", "V32", "V33", "V34", "V35", "V37", "W37", 
    "W38", "W42", "W43", "M1", "M2", "M23", "M24", "M3", "M31", "M32", "M33", 
    "M35", "M36", "M37", "M38"
]

free_classrooms = [room for room in all_classrooms if room not in occupied_classrooms]

grouped_classrooms = {}
for room in free_classrooms:
    letter = room[0]
    grouped_classrooms.setdefault(letter, []).append(room)

for rooms in zip_longest(*grouped_classrooms.values(), fillvalue=""):
    print("\t".join(rooms))