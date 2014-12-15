"""This is the main app"""
from flask import Flask, render_template, request
from scorer.match import Match
from scorer.scorer import Scorer

app = Flask(__name__) #pylint: disable=C0103
SCORER = Scorer()

@app.route('/')
def hello_world():
    """Function for retrieving team score in a match"""
    match_id = request.args.get('match_id')
    team_name = request.args.get('team_name')
    team_score = SCORER.get_team_score(match_id, team_name)
    return render_template('index.html', team_score=team_score)

def hello_world2():
    """Function for tallying score"""
    match_id = request.args.get('match_id')
    team_name = request.args.get('team_name')
    score = request.args.get('score')
    team_score = SCORER.add_score(match_id, team_name, score)
    return render_template('index.html', team_score=team_score)

if __name__ == '__main__':
    import cProfile

    match = Match('1', 'alpha', 0) #pylint: disable=C0103
    SCORER.add_match(match)
    cProfile.run('app.run(debug=True)')
