from datetime import datetime
from typing import Union

from dateutil.tz import tz
from dateutil import parser

tpe_timezone = tz.gettz("Asia/Taipei")


def get_local_time():
    return datetime.now(tz=tpe_timezone)


def get_local_time_in_string():
    return get_local_time().strftime("%Y-%m-%d %H:%M:%S")


def datetime_to_iso_format(date_time: Union[datetime, str]) -> str:
    if isinstance(date_time, str):
        date_time = parser.parse(date_time)
    if isinstance(date_time, datetime):
        return date_time.replace(tzinfo=tpe_timezone).isoformat()
    else:
        raise TypeError("date_time must be datetime or str")
