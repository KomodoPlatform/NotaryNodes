#!/usr/bin/env python3
import os
import json

script_path = os.path.realpath(os.path.dirname(__file__))


def parse_candidates(season):
    data = {
        "AR": [],
        "EU": [],
        "NA": [],
        "SH": []
    }
    headers = []
    with open(f"{script_path}/../season{season}/candidates/README.md", "r") as f:
        for line in f.readlines():
            print(line)
            if line.startswith("|") and line.find("--") == -1:

                if len(headers) == 0:
                    headers = [i.strip() for i in line.split("|")][2:]
                else:
                    line_data = [i.strip() for i in line.split("|")][2:]
                    for i in range(len(line_data)):
                        if line_data[i].find("]") > -1:
                            info = line_data[i].split("]")[
                                1].replace("(", "").replace(")", "")
                            notary = line_data[i].split("]")[
                                0].replace("[", "")
                            region = headers[i]
                            if len(notary) > 1:
                                address = info.split(" ")[1].replace('"', '')
                                print("Generating JSON for",
                                      notary, region, address)

                                base_notary = notary
                                if base_notary.endswith("2") and base_notary not in ["mx222"]:
                                    base_notary = base_notary[:-1]
                                if base_notary == "alienx":
                                    base_notary = base_notary[:-1]
                                if base_notary == "kolox":
                                    base_notary = base_notary[:-1]
                                if base_notary == "chmexvet":
                                    base_notary = "chmex"

                                data[region].append({
                                    "address": address,
                                    "candidate": notary,
                                    "qr_code": f"https://raw.githubusercontent.com/KomodoPlatform/NotaryNodes/master/season{season}/qr_codes/{notary}_{region}.png",
                                    "text": f"https://github.com/KomodoPlatform/NotaryNodes/tree/master/season{season}/candidates/{base_notary}/README.md"
                                })
    return data


if __name__ == "__main__":
    season = 8
    data = parse_candidates(season)
    json.dump(data, open(
        f"{script_path}/../season{season}/candidates.json", "w"), indent=4)
