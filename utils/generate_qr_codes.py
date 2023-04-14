#!/usr/bin/env python3
import os
import pyqrcode
import png # pip3 install pypng==0.20220715.0
import pyqrcode # pip3 install PyQRCode==1.2.1

script_path = os.path.realpath(os.path.dirname(__file__))

def parse_candidates(season):
    headers = []
    with open(f"{script_path}/../season{season}/candidates/README.md", "r") as f:
        for line in f.readlines():
            print(line)
            if line.startswith("|") and line.find("--") == -1:

                if len(headers) == 0:
                    headers = [i.strip() for i in line.split("|")][3:]
                else:
                    line_data = [i.strip() for i in line.split("|")][3:]
                    for i in range(len(line_data)):
                        if line_data[i].find("]") > -1:
                            info = line_data[i].split("]")[1].replace("(", "").replace(")", "")
                            notary = line_data[i].split("]")[0].replace("[", "")
                            region = headers[i]
                            if len(notary) > 1:
                                address = info.split(" ")[1].replace('"', '')
                                qr_data = pyqrcode.create(address)
                                print("Generating QR code for", notary, region, address)
                                qr_data.png(f'{script_path}/../season{season}/qr_codes/{notary}_{region}.png', scale = 10)

if __name__ == "__main__":
    parse_candidates(7)