# -*- coding: utf-8 -*-

@step(u'I go to the "(.*)" URL')
def i_go_to_the_url(step, url):
    world.response = world.browser.visit(django_url(url))

@step(u'a user exists with username "(.*)"')
def a_user_exists_with_username(step, p_username):
    user = UserProfile(username=p_username, email='example@example.com')
    user.set_password('secret007')
    user.save()

@step(u'I fill in "(.*)" with "(.*)"')
def i_fill_in(step, field, value):
    world.browser.fill(field, value)

@step(u'I move focus away from the username field')
def i_move_focus_away_from_the_username_field(step):
    world.browser.fill("password", "value")
    world.browser.wait_for_xpath('//*[@id="availability" and text()="not available"]')

@step(u'I should see "(.*)"')
def i_should_see(step, text):
    assert text in world.browser.html


#python manage.py harvest --apps=users --settings=settings_lettuce
