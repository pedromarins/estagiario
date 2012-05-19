# -*- coding: utf-8 -*-

def get_val(dt,key,org):
    return dt.get(key, getattr(org, key))

def datetime_stub(**kw):
    """A datetimestub object to replace methods and classes from 
    the datetime module. 

    Usage:
        import sys
        sys.modules['datetime'] = DatetimeStub()
    """
    import datetime as datetime_orig    
    
    class DatetimeStub(object):  
        
        class date(datetime_orig.date):
            @classmethod
            def today(cls):
                today_orig = datetime_orig.date.today()                
                year, month, day = map(lambda x: get_val(kw, x, today_orig), ['year', 'month', 'day'])
                return datetime_orig.date(year, month, day)
     
        class datetime(datetime_orig.datetime):
            @classmethod
            def now(cls):
                """Override the datetime.now()"""
                norig = datetime_orig.datetime.now()                
                y,m,d = map(lambda x: get_val(kw, x, norig), ['year', 'month', 'day'])
                hour, minute, second = map(lambda x: get_val(kw, x, norig), ['hour', 'minute', 'second'])
                return datetime_orig.datetime(y,m,d,hour,minute,second)
                
        def __getattr__(self, attr):          
            return getattr(datetime_orig, attr)
    
    return DatetimeStub()