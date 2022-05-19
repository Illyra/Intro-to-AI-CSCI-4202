import  json

def check(discord_uid, bet):
    with open("bank.json") as jsonFile:
        bank_file = json.load(jsonFile)
        jsonFile.close()
    user_info = bank_file[str(discord_uid)]
    current_money = user_info["money"]

    if current_money >= int(bet):
        check_bool = True
    else:
        check_bool = False
    return check_bool

if __name__ == "__main__":
    check()