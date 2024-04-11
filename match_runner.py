from modules.match import Matches


if __name__ == "__main__":
    print("Enter match id:")
    match_id=input()
    print("Enter name of the first participating team")
    team_a=input()
    print("Enter name of the second participating team")
    team_b=input()
    
    
    
    Matches.create_match(match_id, team_a, team_b)

    for match in Matches.get_matches():
        print(match)
    
    