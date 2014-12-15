class Scorer(object):
    def __init__(self):
        self.matchs = {}

    def add_match(self, account):
        self.matchs[match.match_id] = match.team_name, match.team_score
    
    def get_team_score(self, match_id, team_name):
        return self.match.get(match_id, team_name)
    
    def add_score(self, match_id, team_name, points):
        self.match[team_score] += score
