import json

class Match:
    def __init__(self, match_id, team_1, team_2):
        self.match_id = match_id
        self.team_1 = team_1
        self.team_2 = team_2

    def __str__(self):
        return f"match_id: {self.match_id}, team_1: {self.team_1}, team_2: {self.team_2}"

    def to_dict(self):
        return {
            'match_id': self.match_id,
            'team_1': self.team_1,
            'team_2': self.team_2
        }

class Matches:
    @staticmethod
    def load_matches():
        with open("data.json", "r") as file:
            data = json.load(file)
            return [Match(**match) for match in data.get("matches", [])]

    @staticmethod
    def save_matches(matches):
        match_dicts = [match.to_dict() for match in matches]
        with open("data.json", "r") as file:
            data = json.load(file)
        data["matches"] = match_dicts
        with open("data.json", "w") as file:
            json.dump(data, file)

    @staticmethod
    def create_match(match_id, team_1, team_2):
        matches = Matches.load_matches()
        matches.append(Match(match_id=match_id, team_1=team_1, team_2=team_2))
        Matches.save_matches(matches)

    @staticmethod
    def remove_match(match_id):
        matches = Matches.load_matches()
        new_matches = []
        for match in matches:
            if match.match_id != match_id:
                new_matches.append(match)
        Matches.save_matches(new_matches)

    @staticmethod
    def get_matches():
        return Matches.load_matches()
