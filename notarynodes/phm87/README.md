# phm87 Node info

Dear KMD community,

I'm running a mining pool with 30 - 40 altcoins since September 2017 with friends. We contributed to yiimp opensource project and we helped some coin developers.

I'd like to run a Notary Node in SH region and I expect at least as much work as a 40 altcoins mining pool requires. I joined the NN testnet of 2019 that was fun.

I had pleasure to test several ideas on testnet on altcoins and I'd like to support Komodo ecosystem by providing mining pools, block explorers for "testnet" coins and other tools (*).

## Voting Address (EU region) :

**KMD** - RUMwK3uQtWzTmKxCKit7UXY9VMySdmEfbd

## Server Specs  :

- Intel Xeon E3-1245v5 - 4c/8t - 3.5 GHz/3.9 GHz
- 64GB DDR4 ECC 2133MHz
- NVMe 1.2 To RAID

Hardware will be chosen according to requirements to run the Notary Node setup with virtualization. A dual-CPU, more RAM or a second server may also be added if load is higher than expected. On the mining pool, we are using several servers in a VPN but with a network segmentation so using several servers won't be an issue.
	
## Node details and future  :

The Notary Nodes rewards will be used to pay the servers required to operate as a Notary Node but other experiments may be conducted:
- Additional servers to provide "testnet" (*) mining pools for all KMD assetchains that have a testnet
- Additional servers to provide "testnet" (*) block explorers for all KMD assetchains that have a testnet
- Additional server for kmdlabs for testing (details to be discussed)

My experience with UniMining.net will help me to be able to maintain assetchains, KMD and BTC nodes. We are familiar with virtualization (VMware ESXi), TeamCity and coin updates. We improved automation using TeamCity and custom scripts to build and deploy coins but also to monitor blockchains. We are planning to use Docker when we will have enough experience with it (1). To improve stability, another script checks if each coin daemon is on the same chain of several block explorers.

I operate UniMining.net with friends since September 2017, my friends may help me for some tasks related to automation around NN. Now, UniMining is paying in the coin mined, including KMD. I mined 


## Relations and agreement :

No agreement and no official relation with any entity.

I have a friendly relationship with crackers of zpool, metaphilibert and ludom. I've discussed and met other persons of the KMD ecosystem at meetups and on Internet.


## Contact details  :

- Slack : @phm87
- Discord : phm87#7395
- Bitcointalk : https://bitcointalk.org/index.php?action=profile;u=1117726


(*) In this text, "testnet" doesn't mean that testnet=1 is written into the coin.conf file. As example, RKT / PIRATETEST is the "testnet" of PIRATE coin.

(1) Link to dockerfile:
https://github.com/phm87/docker-coin
