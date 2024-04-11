import json

if __name__ == '__main__':
    with open("data.json", "w") as file:
        json.dump({"transactions": [], "users": [], "matches": []}, file)
    input()
    with open("data.json", "w") as file:
        json.dump({"transactions": [], "users": [], "matches": []}, file)