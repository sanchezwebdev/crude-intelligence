from datetime import date
from dateutil.parser import parse

def standardize_date(d):
    if isinstance(d, date):        
        return d
    if isinstance(d, str):
        try:
            dt = parse(d)
            return dt.date()
        except (ValueError, OverflowError):
            raise ValueError(f"Date format for '{d}' not recognized.")
    raise TypeError(f"Unsupported type {type(d)} for date parsing.")
