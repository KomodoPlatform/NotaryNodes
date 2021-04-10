# Daemonfox Notary Node Proposal 2021

tldr: short explainer below

- Was self home hosted and 100% self built
- New servers and a new local DC to host in with top tier services (PRIVATE RACK)
- Base infrastructure was lifted to Micrisoft Azure/Hyper-V Server 2019 mid Season 4
- Season 5 will be new Microsoft Azure/Hyper-V Server 2019 Hybrid in new DC
- Season 4 hardware will be used as backup and dev/test
- New servers on deck at vendor for assembly when ready for Season 5 (OEM channel partnership)
- Created VOTE2021 CMDlet for Windows users. Works with Verus-Desktop binaries and komodo binaries.
- https://github.com/daemonfox/Daemonfox-Mining-Tools
- Actively testing CryptoNote notarizationof BLUR to KMD with @biz for most of Season 4
- Sent rewards to help update LABS to season 4 KMD compatibility

Discord: daemonfox#6136

## Voting Address
- Region: NA
- Address: RDAEmonF9avm7xau2pYWf3UamgHNXrkzpt

## Server Hosting and Specs

- Local DC PRIVATE hosting, no shared rack space. This is the same colo provider selling space to the companies used by most NA nodes to rent their hosting or bandwidth. I did my research and found the Canadian and New Jersey providers have a major hub in my city as well, and I am negotiating my rack rental for a year, up front, now.

- Twin (2 total) Gigabyte R162-Z10 Servers on order for drop ship and assembly upon payment.
	- Secured place in queue for these parts pending my giving approval later this month
	- AMD EPYC 7003 series Milan CPUs (7313P and 7443P)
	- 128GB (8 X 16GB) DDR4 3200+ ECC 8 channel
	- 2X 1TB M.2 NvME 5100+ Mbps drives in RAID 0
	- 4X 2TB 2.5" SAS Nvme drives in RAID 5
	- Dual 1 Gbit symmetrical connections
	- 1 Remote Management Gbit port with WebUI license
	- https://www.gigabyte.com/us/Enterprise/Rack-Server/R162-Z10-rev-A00

- Season 4 hardware will remain at home to serve as immediate backup and other related service testing

## Who am I?
By day, I am an IT Project Manager for a multi billion USD retailer and manufacturer. There, I help onboard new members to our partner network, guide them in choosing IT solutions for their markets and help them train and implement those solutions into production. Most of my focus there has been dragging the outdated and slugish into compliance, and up to date with our in house software offerings for our partners. To date, it has been over 6 years of cleaning house and growing our partner network from a handful of groups barely keeping in step, to over 5 dozen North American markets running our latest platform, representing nearly 300 retail stores nationwide. Often, my spare available time is taken up providing support to our development and administration teams, who handle the day to day escalations and brokens. When our partners need something, I find it, I document it and then drive our teams to deliver it.

By night, I play as my own private Sysadmin and Full Stack Dev. I have dabbled in blockchain since 2011, starting when I could still GPU mine BTC and slowly have added the skills needed to host near any blockchain related service I might want in the moment. I have operated a few private explorers for my own tinkering, a couple of private pools for myself and friends to test and mine, as well as participated in many blockchain projects through the years leading right up to this moment.

## What do I want from a second season?
My goal in running for season 5 is to give back what I can while growing what I was able to assemble this season. My goal going forward will be to maintain the Verus pool I created and put up a testnet pool beside it to work with the new merged mining features and the possible earnings for tokens and liquidity. I also have plans to add additional VMs to my stack to increase my participation in all komodo projects.

All mining and Notary proceeds will go towards this goal, to maintain daemoncoins.com permanently, with active pools, my shop (hopefully soon open to others), to work on creating web hooks to nSPV calls for the ERP solution, and bring online the pools needed to power a set of blockchain data structures and procedures for businesses to leverage. The plan is to build out several services that can be used singularly, or all in tandem. I will officially start this last project in season 5 when I create an AC mining and staking server.

### Project Involvement
  - 2011-2013 actively mining BTC, LTC and several alts as they came into the ecosystem
    - From Solo wallet mining, to pool mining, to running local stratum solutions for my own miners
    - Began deploying explorers to test with other developers for new coins and projects. BTC, NMC, LTC and some early SciFi coins
  - 2014-2015 experimented with many open source block explorers for BTC, scrypt coins and other emerging coins including BTCD
    - As I would mine new coins, I created one off explorers for myself, always hosted at daemoncoins.com until no longer needed
    - Also started trying different pool software, and working with several open source exchange projects
  - 2016-2018 began building my own VMs and structuring a new GPU and ASIC mine. Dedicated Komodo mining and research began
    - Partnered with friends, we built out a server rack of dense GPU miners and some ASICs to participate in Komodo and other projects for the next several years
    - Joined many Komodo projects and volunteered time and testing
    - Current participant in KMD, VRSC, LABS, DP,and am a SUPERNET holder, along with several other assets
    - I was awarded a handful of bounties to date for different contests and testing done throughout the platform
	    - Was 1 of 3 top pize winners during jl777 developing the POS64 solution, won by proving I could multi-daemon stake and gain an edge, leading to a patch
	    - Won KMDLABS POS64 contests a few times as the alpha chains were tested. Ended as 1 of the top 5 total LABS holders day of final snapshot for production launch
  - 2019 to June 2020 maintain several servers and miners participating in many Komodo based projects
    - Secured and maintained a position in the KMDLABS notary node project
    - Helped test many KMDLABS forks as well as the latest VRSC and KMD forks as they happened
    - Won a VRSC reward for my help with the initial public testing of merged mining
    - Won a KMDLABS bounty for being the first to stake the most on a new fork and prove a bug
    - Successfully tested nSPV with jl777 with many transactions on the live KMD chain all working
    - Dedicated time to helping Windows users. Specifically, helping them stake in Verus-Desktop when POS 64 coins did not have an easy way to do so
  - June 2020 to Present
    - Dedicated Notary Node operator for Season 4
    - Daily IguanaTV watcher and VM manager
    - Launch VRSC pool
    - Launch CLC pool
    - Launch a VerusPay powered shop (in private beta)

### Projects Live Now
  - Mining/Staking
    - KMD, VRSC, ARRR, DP, LABS, MCL, SPACE and CHIPS and other Komodo assets
    - Operator of daemoncoins.com, a privately used domain that will have public services once the notary node is online
  - Notary Node Experience
	- KMDLABS Notary Node since alpha testing and in current good standing
	- Season 4 KMD Notary Node operator
  - Iguana, SUPERNET and DEX GUI
    - Current participant in KMDLABS crosschain transactonal testing
    - Constant participant in BarterDEX, HyperDEX and the atomicDEX wallets
  - POS64, MGNX and KMDLABS
    - Once POS64 completed the fork, MGNX decided to launch, and we all participated. I was one of the top holders before closing my daemon to go back to KMDLABS testing
	- KMDLabs LabsAssistant since project birth
    - KMDLABS Notary Node operator for well over two years now
  - PIRATE (ARRR)
    - Holder and active participant since launch
  - Veruscoin (VRSC)
	- Early miner (many max reward, time locked blocks mined, through to current day mining and staking)
	- Volunteered for testing many times, including for the algo changes, merged mining and VerusIdentity

## Notary Addresses Season 4

MAIN
   - KMD: RWQrQd6MiuW5Eqqv9E8JE6arLQVZ4q8pSS                 -
   - BTC: 1N8fL7D585hWAqUig49B8aFea92xQozint                 -
   - PubKey: 022d6f4885f53cbd668ad7d03d4f8e830c233f74e3a918da1ed247edfc71820b3d

3P
   - KMD: RQjWkcfAoNd9pDv1oohtwSLF4gyHUzoamE-
   - BTC: 1GTKg6mtCYpakDYpLdimqv13JRWgpNmD1V-
   - PubKey: 023c7584b1006d4a62a4b4c9c1ede390a3789316547897d5ed49ff9385a3acb411
