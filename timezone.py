'''import datetime
from pytz import timezone

south_africa = timezone('Africa/Johannesburg')
sa_time = datetime.datetime.now(south_africa)
print sa_time.strftime('%Y-%m-%d_%H-%M-%S')
'''

from datetime import datetime
import pytz

#timezone = raw_input("Enter the time zone")
localFormat = "%Y-%m-%d %H:%M:%S"

utcmoment_unaware = datetime.utcnow()
utcmoment = utcmoment_unaware.replace(tzinfo=pytz.utc)

timezones = ['America/Los_Angeles', 'Etc/GMT+1', 'Etc/Greenwich', 'UTC', 'Asia/Kolkata']

for tz in timezones:
    localDatetime = utcmoment.astimezone(pytz.timezone(tz))
    print localDatetime.strftime(localFormat), tz
