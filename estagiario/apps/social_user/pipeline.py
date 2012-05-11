# -*- coding: utf-8 -*-
from models import UserProfile, fill_profile_from_fb

def populate_user_profile(*args, **kwargs):
    #print 'response'
    response = kwargs['response']
    #print response
    #print kwargs
    user = kwargs['user'] # contrib.auth.User
    # print 'user'
    # print type(user)
    # print user
    # print dir(user)
    print 'user.id'
    print user.id
    
    #print kwargs.keys()#['username', 'uid', 'request', 'is_new', 'auth', 'facebook', 'user', 'social_user', 'backend', 'response', 'details']

    #print 'response.keys()'
    #print response.keys() #[u'username', 'access_token', u'first_name', u'last_name', u'middle_name', u'name', u'locale', u'gender', u'work', 'expires', u'email', u'languages', u'updated_time', u'birthday', u'link', u'location', u'verified', u'timezone', u'education', u'id']
    #print response
    # kwargs = {
    #     'user': user,
    #     'hometown': response['hometown']['name'],
    #     'birthday': date(year, month, day),
    # }

    # u'education': [{u'with': [{u'id': u'100000520254552', u'name': u'Elizia Moraes'}, {u'id': u'100000188938516', u'name': u'Bia Azevedo'}], u'school': {u'id': u'148870398519809', u'name': u'Col\xe9gio Santa M\xf4nica'}, u'type': u'High School'}, {u'school': {u'id': u'110300132332993', u'name': u'UNIRIO'}, u'type': u'College', u'concentration': [{u'id': u'170024726376463', u'name': u'Inform\xe1tica'}], u'year': {u'id': u'143018465715205', u'name': u'2000'}}, {u'school': {u'id': u'109896575694939', u'name': u'Universidade Federal do Estado do Rio de Janeiro'}, u'type': u'College', u'year': {u'id': u'143641425651920', u'name': u'2014'}}], 

    try:
        profile = user.get_profile()
        #profile.birthday = kwargs['birthday']
        #profile.save()
        print 'has profile'
    except Exception:
        profile = UserProfile.objects.create(user=user)
        profile = fill_profile_from_fb(user, profile, response)
        profile.save()
        pass




# u'work': [
#     {   u'position': {u'id': u'131116140260932', u'name': u'Co-Founder, Director'},
#         u'start_date': u'2011-08', 
#         u'location': {u'id': u'110346955653479', u'name': u'Rio de Janeiro, Rio de Janeiro'}, 
#         u'employer': {u'id': u'126036997497012', u'name': u'SparkIT'}
#     }, 

#     {   u'from': {u'id': u'1534023828', u'name': u'Tiago Veloso'}, 
#         u'with': [{u'id': u'1534023828', u'name': u'Tiago Veloso'}], 
#         u'employer': {u'id': u'172835506073645', u'name': u'Uniriotec Consultoria'}
#     }
# ], 


# u'email': u'contato@victorfontes.com', 
# 
# u'updated_time': u'2012-05-10T01:52:55+0000', 
# u'verified': True, 
# u'link': u'http://www.facebook.com/codigofontes', 
# u'location': {u'id': u'110346955653479', u'name': u'Rio de Janeiro, Rio de Janeiro'}, 
# u'timezone': -3, 
# u'education': [{u'with': [{u'id': u'100000520254552', u'name': u'Elizia Moraes'}, {u'id': u'100000188938516', u'name': u'Bia Azevedo'}], u'school': {u'id': u'148870398519809', u'name': u'Col\xe9gio Santa M\xf4nica'}, u'type': u'High School'}, {u'school': {u'id': u'110300132332993', u'name': u'UNIRIO'}, u'type': u'College', u'concentration': [{u'id': u'170024726376463', u'name': u'Inform\xe1tica'}], u'year': {u'id': u'143018465715205', u'name': u'2000'}}, {u'school': {u'id': u'109896575694939', u'name': u'Universidade Federal do Estado do Rio de Janeiro'}, u'type': u'College', u'year': {u'id': u'143641425651920', u'name': u'2014'}}], 
# u'id': u'578128614'}

# >>> User.objects.all()[0].id
# 1
# >>> u = User.objects.all()[0]
# >>> u.social_auth.all()
# [<UserSocialAuth: codigofontes>]
# >>> uu = u.social_auth.all()[0]
# >>> uu.uid
# u'578128614'
# >>> uu.extra_data
# >>> uu.id

# {'username': u'codigofontes', 'uid': u'578128614', 'request': <WSGIRequest    










#response.keys()
