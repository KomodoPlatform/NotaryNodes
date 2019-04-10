# vote2018
Notary Nodes candidates proposals

## to verify results 

git clone -b jl777 https://github.com/jl777/komodo.git

build it 

cd src

./komodod (sync KMD from scratch 6-8H)

edit `notarystats.py` so that:
  `stopheight = 1307200`

./notarystats.py 

to get KMD results edit notarystats.py 

from this `if obj['chain'] == 'KMD':` to this `if obj['chain'] != 'KMD':`

and `startheight =  821657 #Second time filter for assetchains (block 821657) for KMD its 814000` 

change that to `startheight =  814000`

all the code is there feel free to check it. 
