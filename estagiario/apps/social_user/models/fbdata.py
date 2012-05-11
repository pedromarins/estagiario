# -*- coding: utf-8 -*-
from datetime import date
from address.models import City, State

def parse_date(dt_str):
    try:
        month, day, year = [int(x) for x in dt_str.split('/')]
        return date(year, month, day)
    except Exception:
        return None

def get_birthday(data):
    return parse_date( data.get('birthday','') )


def get_location(data):
    city, state = None, None
    location = data.get('location', None)
    
    try:
        _state = location.split(', ')
        _state = _state[1] if len(_state)==2 else _state[0]
        state = State.objects.filter(name__iexact=_state)[0]
    except Exception:
        pass

    try:
        _state[1] # len==2:
        city = City.objects.filter(name__iexact=location.split(', ')[0]).filter(state=state)[0]
    except Exception:
        pass

    return city, state

