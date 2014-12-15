from lettuce import *
from nose.tools import assert_equal, assert_in
from webtest import TestApp


@step(u'I visit the homepage')
def i_visit_the_homepage(step):
    world.browser = TestApp(app)
    world.response = world.browser.get('http://localhost:5000/')
    assert_equal(world.response.status_code, 200)

@step(u'And I input team name as "([^"]*)" and score as "([^"]*)"')
def and_i_input_team_name_as_group1_and_score_as_group2(step, group1, group2):
    form = world.response.forms['tally-form']
    form['team_name'] = team_name
    form['score'] = score
    world.form_response = form.submit()
    assert_equal(world.form_response.status_code, 200)

@step(u'I see a match score of "([^"]*)" = "([^"]*)" vs "([^"]*)" = "([^"]*)"')
def then_i_see_a_match_score_of_group1(step, expected_balance):
    assert_in ("Balance: {}".format(expected_balance),
    world.form_response.text)

@step(u'I create account "([^"]*)" with balance of "([^"]*)"')
def i_create_account_with_balance_of_group1(step, account_number, balance):
    a = Account(account_number, balance)
    BANK.add_account(a)

@step(u'I create the following match:')
def i_create_the_following_match(step):
    for row in step.hashes:
        a = Match(row['team_name1'], row['team_score1'], row['team_name2'], row['team_score2'])
        BANK.add_match(a)
