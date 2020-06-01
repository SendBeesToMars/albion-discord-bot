import requests
import json
from itertools import islice


def get_kd(player_id):
    req = requests.get(f"https://gameinfo.albiononline.com/api/gameinfo/players/{player_id}")
    rj = req.json()
    kd = {"kill_fame": rj["DeathFame"],
            "death_fame": rj["KillFame"],
            "kd": rj["FameRatio"]}
    return kd

def search(arg1=None, arg2=None):
    if arg2 == None and arg1 != None:
        req = requests.get(f"https://gameinfo.albiononline.com/api/gameinfo/search?q={arg1}")
        print(req.status_code)
        if req.status_code != 200:
            return
        return json.dumps({"players": take(req.json()["players"], 2), "guilds": take(req.json()["guilds"], 4)}, indent=4)
    elif arg2 != None:
        req = requests.get(f"https://gameinfo.albiononline.com/api/gameinfo/search?q={arg2}")
        print(req)
        if req.status_code == 200:
            if arg1 == "-p":
                # return json.dumps(take(3, req.json()["players"]), indent=4)
                player_dict = {}
                for player in req.json()["players"]:
                    player_dict[player["Name"]] = { 
                        "Id": player["Id"],
                        "GuildName": player["GuildName"],
                        "GuildId": player["GuildId"],
                        "AllianceName": player["AllianceName"],
                        "AllianceId": player["AllianceId"],
                        "KillFame": player["KillFame"],
                        "DeathFame": player["DeathFame"],
                        "FameRatio": player["FameRatio"]
                        }
                
                return json.dumps(discord_len_check(dict_filter(player_dict), 10), indent=4)
                # return json.dumps(dict_filter(player_dict), indent=4)
                # return json.dumps(player_dict, indent=4)
                # return json.dumps(req.json()["players"][0]["Id"], indent=4)
            elif arg1 == "-g":
                guild_dict = {}
                for guild in req.json()["guilds"]:
                    guild_dict[guild["Name"]] = {
                        "Id": guild["Id"],
                        "AllianceName": guild["AllianceName"],
                        "AllianceId": guild["AllianceId"],
                        "KillFame": guild["KillFame"],
                        "DeathFame": guild["DeathFame"]
                    }
                return json.dumps(discord_len_check(dict_filter(guild_dict), 10), indent=4)
                # if len(json.dumps(take(req.json()["guilds"], 10), indent=4)) < 2000:
                #     return json.dumps(take(req.json()["guilds"], 10), indent=4)
                # else:
                #     return json.dumps(take(req.json()["guilds"], 8), indent=4)

    else:
        return "shits fooked! error code: " + str(req.status_code) + ", meaning that you should try again ;)"

    # returns first i items from dict
def take(dict, i):
    return list(islice(dict, i))

    # filters out non values(0, 0.0, null, etc..) out of the dict
def dict_filter(dict):
    final_dict = {}
    for i in dict:
        items = {}
        for j in dict[i]:
            if dict[i][j]:
                items[j] = dict[i][j]
            final_dict[i] = items
    return final_dict

    # return dict if below 2000 characters (discord message limit)
def discord_len_check(dict, i):
    pairs = {k: dict[k] for k in sorted(dict.keys())[:i]}
    if len(pairs) > 2000:
        i -= 1
        discord_len_check(dict, i)
    else:
        return pairs

# print(search("-g", "band"))
# print(search("-g", "band"))
# search("-p", "winmi")