Feature: A script that tally the score of a basketball game

As a scorer I want to be able to view the basketball match score
and tally the points of both teams


Scenario: View score
Given the I create following match:
| match_id | team_name | team_score |
| 1        | alpha     | 0          |
| 1        | beta      | 0          |
And I visit the homepage
When I input match id as "1" and team name as "alpha"
Then I see the team score of "0"

Scenario: Tally score
Given the I create following match:
| match_id | team_name | team score |
| 1        | alpha     | 0          |
| 1        | beta      | 0          |
And I visit the homepage
When I input match id as "1" team name as "alpha" and score as "2"
Then I see the team score of "2"
