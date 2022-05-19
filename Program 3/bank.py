import json

def register(discord_uid, username, user_id):
    with open("bank.json") as jsonFile:
        dict_bank = json.load(jsonFile)
        jsonFile.close()

    if str(discord_uid) in dict_bank:
        print("User \"" + str(discord_uid) + "\" is already registered")
    else:
        dict_bank[str(discord_uid)] = {
            "discord_uid": str(discord_uid),
            "username": username,
            "user_id": user_id,
            "rank": "player",
            "money": 1000,
            "games_played": 0,
            "games_won": 0,
            "games_lost": 0,
            "games_draw": 0,
            "games_blackjack": 0,
            "money_bet": 0,
            "money_won": 0,
            "money_lost": 0
        }

        with open("bank.json", "w", encoding = "utf-8") as f:
            json.dump(dict_bank, f, ensure_ascii = False, indent = 4)
            f.close()

def money(discord_uid):
    with open("bank.json") as jsonFile:
        bank_file = json.load(jsonFile)
        jsonFile.close()
    user_info = bank_file[str(discord_uid)]
    current_money = user_info["money"]
    return current_money

def handle_bet(discord_uid, bet):
    with open("bank.json", "r", encoding = "utf-8") as jsonFile:
        bank_file = json.load(jsonFile)
        jsonFile.close()

    user_info = bank_file[str(discord_uid)]
    current_money = user_info["money"]
    up_dict = {"money":current_money - int(bet)}
    user_info.update(up_dict)

    bank_file[str(discord_uid)] = user_info

    with open("bank.json", "w", encoding = "utf-8") as f:
        json.dump(bank_file, f, ensure_ascii = False, indent = 4)
        f.close()

if __name__ == "__main__":
    pass