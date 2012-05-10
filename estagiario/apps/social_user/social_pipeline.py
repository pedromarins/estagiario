# -*- coding: utf-8 -*-

def populate_user_profile(*args, **kwargs):
    response = kwargs['response']
    user = kwargs['user']
    month, day, year = [int(x) for x in response['birthday'].split('/')]
    kwargs = {
        'user': user,
        'hometown': response['hometown']['name'],
        'birthday': date(year, month, day),
    }
    try:
        profile = user.get_profile()
        profile.hometown = kwargs['hometown']
        profile.birthday = kwargs['birthday']
        profile.save()
    except Exception:
        #Profile.objects.create(**kwargs)
        pass