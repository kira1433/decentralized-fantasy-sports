from modules.match import Matches


if __name__ == "__main__":
    match_id=input()
    team_a=input()
    team_b=input()
    
    
    
    Matches.create_match(match_id, team_a, team_b)

    for match in Matches.get_matches():
        print(match)
    
    