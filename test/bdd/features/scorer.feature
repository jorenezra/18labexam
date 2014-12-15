Feature: A script that tally the score of a basketball game

As a scorer I want to be able to view the basketball match score
and tally the points of both teams


Scenario: View score
Given the I create following match:
| team_name1 | team_score1 | team_name2 | team_score2 |
| alpha      | 0           | beta       | 0           |
When I visit the homepage
Then I see the match score of "alpha" = "0" and "beta" = "0"

Scenario: Tally score
Given the I create following match:
| team_name1 | team_score1 | team_name2 | team_score2 |
| alpha      | 0           | beta       | 0           |
And I visit the homepage
When I input team name as "alpha" and score as "2"
Then I see the match score of "alpha" = "2" and "beta" = "0"