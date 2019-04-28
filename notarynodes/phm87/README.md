# phm87 Node info

Dear KMD community,

I'm running UniMining.net mining pool with 30 - 40 altcoins since September 2017 with friends. We contributed to yiimp opensource project and we helped some coin developers. I'm working in IT since 10 years and I entered the world of cryptocurrencies in april 2017.

I'd like to run a Notary Node in SH region and I expect at least as much fun, work and pleasure as I had to run a 40 altcoins mining pool. I joined the NN testnet of 2019 that was very interesting. I contributed a little bit (1). Komodo ecosystem is new for me but I'd like to take part and help as much as I can in this amazing community.

I had pleasure to test several ideas on testnet on altcoins and I'd like to support Komodo ecosystem by providing mining pools, block explorers for assetchains that could need it and other tools.

## Voting Address (SH region) :

**KMD** - RUMwK3uQtWzTmKxCKit7UXY9VMySdmEfbd

## Server Specs  :

- Intel Xeon E3-1245v5 - 4c/8t - 3.5 GHz/3.9 GHz
- 64GB DDR4 ECC 2133MHz
- NVMe 1.2 To RAID

Hardware will be chosen according to requirements to run the Notary Node setup with virtualization. A dual-CPU, more RAM or a second server may also be added if load is higher than expected. On the mining pool, we are using several servers in a VPN but with a network segmentation so using several servers won't be an issue.

Server location will be in Sydney, Australia. I'd like to discuss and eventually test ideas to enhance SH region connectivity such as having another server in Asian region to run other nodes (same AC, different wallets) and use a fast private network between the NN server in Sydney and Asian region.


## Reward sharing  :

15% of KMD earnings will be given to KMDLabs
15% of KMD earnings will be given to CHIPS

These donations won't stop after first year if auto re-elected. These donations will be performed in addition to the servers described in the next section.


## Node details and future  :

The Notary Nodes rewards will be used to pay the servers required to operate as a Notary Node but other experiments may be conducted:
- Additional servers to provide mining pools for all assetchains that could need it
- Additional servers to provide block explorers for all assetchains that could need it (2)
- Additional server for KMDLabs for testing (details to be discussed)
- Other tools to support KMD ecosystem such as stats, BartexDEX, CHIPS, KSB and CHIPS into yiimp (3). By stats, I mean servers to have more stats about KMD and each assetchain (count of transactions per day, graphs).

My experience with UniMining.net will help me to be able to maintain assetchains, KMD and BTC nodes. We are familiar with virtualization (VMware ESXi), TeamCity and coin updates. We improved automation using TeamCity and custom scripts to build and deploy coins but also to monitor blockchains. We are planning to use Docker when we will have enough experience with it (4). To improve stability, another script checks if each coin daemon is on the same chain of several block explorers.

I operate UniMining.net with friends since September 2017, my friends may help me for some tasks related to automation around NN. Now, UniMining is paying in the coin mined, including KMD. Other features are possible such as to pay in another coin. I think it can be interesting to pay in KMD and in KSB.


## Relations and agreement :

No agreement and no official relation with any entity.

I have a friendly relationship with crackers of zpool, metaphilibert and ludom. I've discussed and met other persons of the KMD ecosystem at meetups and on Internet. I'm active on CryptoFr slack and in yiimp community.


## Contact details  :

- Slack : @phm87
- Discord : phm87#7395
- Bitcointalk : https://bitcointalk.org/index.php?action=profile;u=1117726


(1) During testnet 2019 of NN, I was able to contribute a little bit. These contributions were possible thanks to other persons who explained.
https://github.com/jl777/komodo/pull/1416

https://github.com/Alrighttt/2019NNtestnet/pull/40
https://github.com/Alrighttt/2019NNtestnet/pull/43
https://github.com/Alrighttt/2019NNtestnet/pull/46

(2) I heard that a new block explorer can be useful to support CHIPS : https://chips.unimining.net/ (it should work from about the 10th May 2019)

(3) As CHIPS can be used with c-lightning's jl777 fork, if commands of c-lightning were kept, my testnet usecase of c-lightning should work:
https://github.com/tpruvot/yiimp/pull/292

(4) Link to dockerfile:
https://github.com/phm87/docker-coin
