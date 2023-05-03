#!/usr/bin/env python3
import os
import sys
import json
import requests

class ElectedNotaries():
    def __init__(self, season, coin):
        self.coin = coin
        self.season = season
        try:
            with open(f"../season{self.season}/elected_nn_social.json", 'r') as json_file:
                self.elected_social = json.load(json_file)
        except:
            self.elected_social = {}
        self.vote_results = requests.get(f'https://kip0001.smk.dog/api/v3/polls/{self.coin}/info').json()
        self.last_season_winners = self.vote_results['extra_info']['last_season_winners']

    def add_notary(self, notary, region):
        return {
            notary: {
                "discord": "",
                "discord_name": "",
                "email": "",
                "github": "",
                "icon": "",
                "keybase": "",
                "telegram": "",
                "twitter": "",
                "website": "",
                "youtube": "",
                "regions": {
                    region: {
                        "Main": {
                            "pubkey": ""
                        },
                        "Third_Party": {
                            "pubkey": ""
                        }
                    }
                }
            }
        }

    def add_region(self, notary, region):
        return {
            region: {
                "Main": {
                    "pubkey": ""
                },
                "Third_Party": {
                    "pubkey": ""
                }
            }
        }

    def populate_autoelected(self):
        for region in self.last_season_winners:
            for i in self.last_season_winners[region]:
                if i in ["1", "2", "3"]:
                    notary = self.last_season_winners[region][i].lower()
                    if notary not in self.elected_social:
                        self.elected_social.update(self.add_notary(notary, region))
                    elif region not in self.elected_social[notary]["regions"]:
                        self.elected_social[notary]["regions"].update(self.add_region(notary, region))
                    else:
                        notary = f"{notary}_2"
                        if notary not in self.elected_social:
                            self.elected_social.update(self.add_notary(notary, region))
                        self.elected_social[notary]["regions"].update(self.add_region(notary, region))
                        print(f">>>>>>> Duplicate notary: {notary} in {region}! <<<<<<<")


    def populate_vote_winners(self):
        election_results = {}
        for region in self.vote_results["categories"]:
            region_scores = []
            if region not in election_results:
                election_results.update({region: {}})
            for i in self.vote_results["categories"][region]["options"]:
                votes = i["votes"]
                region_scores.append(votes)
            region_scores.sort(reverse=True)
            region_scores = region_scores[:11]

            for i in self.vote_results["categories"][region]["options"]:
                notary = i["candidate"].lower()
                votes = i["votes"]
                if votes in region_scores:
                    if notary not in self.elected_social:
                        self.elected_social.update(self.add_notary(notary, region))
                    elif region not in self.elected_social[notary]["regions"]:
                        self.elected_social[notary]["regions"].update(self.add_region(notary, region))
                    else:
                        notary = f"{notary}2"
                        if notary not in self.elected_social:
                            self.elected_social.update(self.add_notary(notary, region))
                        self.elected_social[notary]["regions"].update(self.add_region(notary, region))
                        print(f">>>>>>> Duplicate notary: {notary} in {region}! <<<<<<<")



    def get_data_from_prior_seasons(self):
        # Scan prior seasons for data
        for season in [4,5,6]:
            with open(f"../season{season}/elected_nn_social.json", "r") as f:
                notary_nodes = json.load(f)
            for notary in notary_nodes:
                notary = notary.lower()
                if notary in self.elected_social:
                    for i in notary_nodes[notary]:
                        if notary_nodes[notary][i] != "" and self.elected_social[notary][i] == "":
                            self.elected_social[notary][i] = notary_nodes[notary][i]
        

if __name__ == '__main__':
    if len(sys.argv) > 1:
        elected = ElectedNotaries(7, "VOTE2023")

        if sys.argv[1] == "create":
            if os.path.exists(f"../season{elected.season}/elected_nn_social.json"):
                print(f"../season{elected.season}/elected_nn_social.json already exists! Exiting...")
                sys.exit(1)
            elected.populate_autoelected()
            elected.populate_vote_winners()
            elected.get_data_from_prior_seasons()
            nodes = 0
            for notary in elected.elected_social:
                nodes += len(elected.elected_social[notary]["regions"])
            print(f"Total nodes: {nodes}")
            elected_dict = dict(sorted(elected.elected_social.items()))
            with open(f"../season{elected.season}/elected_nn_social.json", "w") as f:
                json.dump(elected_dict, f, indent=4)
    

        if sys.argv[1] == "calc_addresses":
            for notary in elected.elected_social:
                for region in elected.elected_social[notary]["regions"]:
                    for i in ["Main", "Third_Party"]:
                        pubkey = elected.elected_social[notary]["regions"][region][i]["pubkey"]
                        if pubkey != "":
                            url = f"https://stats.kmd.io/api/tools/address_from_pubkey/?pubkey={pubkey}"
                            addresses = requests.get(url).json()["results"]
                            for j in addresses:
                                if j["coin"] == "KMD":
                                    elected.elected_social[notary]["regions"][region][i].update({"KMD address": j["address"]})
                                if j["coin"] == "LTC":
                                    elected.elected_social[notary]["regions"][region][i].update({"LTC address": j["address"]})
            with open(f"../season{elected.season}/elected_nn_social.json", "w") as f:
                json.dump(elected.elected_social, f, indent=4)


        if sys.argv[1] == "validate":
            with open(f"../season{elected.season}/elected_nn_social.json", "r") as f:
                elected_social = json.load(f)
            no_contact_info = []
            no_discord = []
            no_github = []
            no_icon = []
            no_pubkey = []
            for notary in elected_social:
                contact_info = 0
                discord_info = 0
                for i in ["discord", "discord_name", "email", "keybase", "telegram", "twitter"]:
                    if elected_social[notary][i] != "":
                        contact_info += 1
                if contact_info == 0:
                    no_contact_info.append(notary)
                for i in ["discord", "discord_name"]:
                    if elected_social[notary][i] != "":
                        discord_info += 1
                if discord_info == 0:
                    no_discord.append(notary)
                if elected_social[notary]["github"] == "":
                    no_github.append(notary)
                if elected_social[notary]["github"] == "":
                    no_icon.append(notary)
                for region in elected_social[notary]["regions"]:
                    for i in ["Main", "Third_Party"]:
                        if elected_social[notary]["regions"][region][i]["pubkey"] == "":
                            if i == "Third_Party":
                                i = "3P"
                            no_pubkey.append(f"{notary}_{region} ({i})")

            print(f"No contact info: {no_contact_info}")
            print(f"No discord: {no_discord}")
            print(f"No github: {no_github}")
            print(f"No icon: {no_icon}")
            print(f"No pubkey: {no_pubkey}")

        


            
            