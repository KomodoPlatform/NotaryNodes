
<img src="./RGCCcjSkszZNMMfH9fRcY1MHc5CHWbt6gQ_NA.jpg"/>


<img src="./REyFgygqWpDtYjKhz214CkA6hrA27d6cxX_SH.jpg"/>


Region | VOTE2023 Address
|:---|:---|
**NA** | `RGCCcjSkszZNMMfH9fRcY1MHc5CHWbt6gQ`
**SH** | `REyFgygqWpDtYjKhz214CkA6hrA27d6cxX`

**NA Main pubkey:** 02f91a6772fe1a376e2bbe4b190008e3f878d40a8eaf92c65f1a7680b6b42ea47b

**NA 3P pubkey:** 0268d30efafc6ac84b1c8210e99fd4936e178794581d348b87f64fcbbfa8d5e73b

**SH Pubkeys will be added here, after they are securely generated (in event of my election for a 2nd node in that region).**


## Introduction

**Hi, I'm [Biz](https://github.com/who-biz).**  This is my 3rd year running for election as a Notary Node operator.  I placed in 5th in North America rankings last year, and as a result, I am running for a node in SH region as well.  Desire to run a node in SH rather than EU/NA is to strengthen the Notary Network.  First year running for re-election.

I develop software (mostly in C/C++ and Rust as of late) for a lot of different blockchains across the industry.  All except for one of these (in my present workday) are KMD-related in some manner.

I spend much of my time as Lead Developer of [The Blur Network](https://blur.cash).  For the past three years, nearly all of my work has focused on KMD-based technology, *and particularly dPoW*.  Skills and experience are split between XMR, BTC, ZEC, and Mimblewimble blockchain architectures.

Time over the past year was split mostly between CHIPS (on Verus) and BLUR development.  More recently, I've been doing work at Epic Cash (EPIC), a Mimblewimble blockchain.  I also contribute code upstream to VRSC whenever possible/worthwhile, and authored code for fully configurable block times on Verus's PBaaS chains.


## Focus of Recent Work

### CHIPS x VRSC

CHIPS development in the last 12 months has consisted largely of a full chain migration from a legacy Bitcoin backend to one of Verus's PBaaS chains.  In doing so, I've worked tightly with Mike from Verus, sg777 (game development on CHIPS), SHossan/Alien, and Satinder Grewal throughout this process.  I am also currently working on Ledger development for Epic Cash.

### BLUR-dPoW

Since April 2019, I have been working on integrating dPoW with Blur (and more broadly: all Monero-based blockchains).  This is work I hope to conclude this year, after needing to take some time off to devote to non-volunteer (paid) work.

### dPoW/Notary Network

I do my best to contribute to a better understanding of `dPoW` in general, and make it a habit to contribute code upstream in all projects I work on.  After discovering that there was a far more efficient loop design (based on `blocknotify`), [I PRed these changes to the official dPoW repository](https://github.com/KomodoPlatform/dPoW/pull/445). 

I openly divulged the performance boosts I was gaining, and publicly explained how I was doing it, with the goal of bringing attention to ways in which Notary Nodes can act selfishly to game the system.  The objective in doing so was to improve the fairness and design of dPoW as a cross-chain security system.  

I believe fairness and a lack of hidden optimizations to be extremely important for dPoW as a system.  The Notary Network is designed in a way that creates (and rewards) direct competition between operators.  After these (now public) codebase modifications became controversial, I rolled back these changes.  I believe this shows my desire to strengthen KMD tech, rather than behaving selfishly in sole pursuit of re-election.  

Disclosing the code I was running publicly almost certainly affected my regional rankings in a negative way, and may have cost me automatic re-election.  **Please vote for me if you value this kind of public discourse and experimentation**.

### Public-Facing Stuff

Most recently, I also did an hour-long interview with Seth Estrada (MineYourBiz) and Mike Toutonghi discussing the prospective Verus network upgrade, and what CHIPS is building on Verus.  This has not yet been posted online.


---


## Development Efforts in the Komodo Ecosystem

- [`chips-vrsc`](https://github.com/who-biz/komodo/tree/dealer-serviceflag) - Codebase for CHIPS PBaaS chain on Verus Testnet. 10 second block times, with a lot of functionality added to enable gamestate publishing and referencing from VerusIDs.  Game state is published to various IDs and subIDs on the verus network, where it is then referenced in a Pub/Sub manner.  For more information, see `verus-pbaas` repository below.

- [`verus-pbaas`](https://github.com/who-biz/verus-pbaas) - Reproducible workflow document for generating PBaaS chains on Verus.  Written specifically with respect to `chips10sec` blockchain, including descriptions of chosen launch parameters, etc.  Verus's tooling has solved a lot of problems for CHIPS, and the section [located here](https://github.com/who-biz/verus-pbaas#background-on-chips-blockchain) is definitely worth a read.

- [`chips-v22`](https://github.com/who-biz/chipschain/tree/nspv-develop) - Upgraded v22.0 CHIPS, fully compatible with dPoW.  NSPV partially added.

- [`chips-upgrade-review`](https://github.com/who-biz/chips-upgrade-review) - Document summarizing upgrade of CHIPS, with specific focus on KMD infrastructure & compat.

  - Accompanied by video walkthrough: [Part One](https://www.youtube.com/watch?v=qEZ6bxyKUHk) || [Part Two](https://www.youtube.com/watch?v=FlaLSGBNuag)

- [`blur`](https://github.com/blur-network/blur) - Partially upgraded BLUR codebase, with some KMD compatbility added for prospective network upgrade.

- [`dpow-blur`](https://github.com/blur-network/dpow-blur) - Upgraded version of [`blur`](https://github.com/blur-network/blur) full node software, for compatibility with KMD's dPoW.

- [`blur-api-cpp`](https://github.com/blur-network/blur-api-cpp) - A compatibility layer for interfacing with `iguana`'s API, negotiates between JSON-RPC specifications.

- [`blur-explorer`](https://github.com/blur-network/blur-explorer/tree/testnet) - A testnet explorer for The Blur Network, which features new dPoW mechanics for XMR-based blockchains.


**Prior contributions during S5 testnet & election:**


- [`blur-network/dPoW`](https://github.com/blur-network/dPoW/tree/blur-2021-testnet) - Modified `2021-testnet` dPoW with added files for notarizations of BLUR->KMD.

  - Instructions for addition of Blur as 3P coin, to existing 2021-testnet NN network [available here](https://github.com/blur-network/dpow-blur/blob/testnet/docs/kmd-2021testnet-setup.md).

- [`who-biz/komodo_scripts`](https://github.com/who-biz/komodo_scripts/tree/from-wif) - Modified `genkomodo.php` script, to generate litecoin keys/addresses from a user-supplied WIF

  - Used by some `2021-testnet` operators in LTC testnet.

- [`who-biz/nntools`](https://github.com/who-biz/nntools/tree/2021-testnet) - Modified `webworker01/nntools` for testnet, added `txid` column for display when running `stats`.

  - Also used by some `2021-testnet` operators for LTC testnet.


---


## Community Efforts

- Contributor to various projects/initiatives in extended KMD ecosystem (KMD, CHIPS, VRSC, BLUR)
- Received a Certificate of Recognition from Komodo team in 2021.
- Placed top 5 in NA region in 1st year as a Notary Node Operator.
- Extensive development of CHIPS on Verus, writing tooling for migration of balances to new chain and development on new blockchain.  Nearly 100% of blockchain development to make this possible is performed by me.
- Prompt with updates to my Notary Nodes. High percentage of node uptime, as shown by last years scoring.
- Dedication of equal effort to 3P Node despite being optional.


---


## Why Vote Biz?

1. **Track record of performance in last season**

2. **Behaviors clearly show I value software improvement and am motivated by curiousity, rather than my own self-interest**

3. **Initmately familiar with dPoW**

Almost all of my recent work has taken place within KMD's ecosystem (with a primary focus on dPoW and 3rd party integrations)

4. **Consistent desire to further strengthen my technical involvement in KMD ecosystem**

5. **I will be a technical liaison for KMD & BLUR (and future XMR-based integrations)**

Blur is already being integrated with the same systems run by KMD's notary network.  Being a S6 Notary Node Operator would provide me with the opportunity to work with the software I've been writing, in the most hands-on way.  This will benefit both KMD and BLUR via quicker problem-solving while integrating Blur, as well as any other XMR-based chain which DPoW may secure in the future.

6. **Notary Node rewards will allow me to focus more time on KMD ecosystem projects**

7. **You'll be guaranteed a very active Notary Node Operator**

Put simply, I'll be available and active every day, as I've been since 2018.


---


## KMD Ecosystem Contributions

A total of **9%** of Notary Node Rewards (in excess of server costs) will be donated back into KMD ecosystem projects.

- **9%** to Blur & Blur-dPoW development

Prior year's proposed contributions of 3% to Tokel have been removed due to inactivity at that project.

Prior year's proposed contributions of 3% to Chips development have been removed due to my increased amount of time spent working on CHIPS software.

*Calculations will be made at the beginning of each month, for the month prior.  Server costs will be covered first, and remaining rewards will be dispersed according to schedule above.  In events where KMD price is exceptionally higher than historical levels, NN Revenues may be liquidated mid-month to cover costs in a more effective manner.*


---


## Server Specs

*Please note server specs below are from prior year. Actual server used may vary with regional availability and pricing.*

Region: NA  |  Main Server | 3P Server |
|:---|:---:|:---:|
CPU:     | 2× Intel Xeon Silver 4214 (or similar) | Intel Xeon-E 2136
Storage: | 2 x 500GB SSD NVMe | 2 x 500GB SSD NVMe
Memory:  | 96-128GB DDR4         | 32GB DDR4

Region: SH  |  Main Server | 3P Server |
|:---|:---:|:---:|
CPU:     | 2× Intel Xeon Silver 4214 (or similar) | Intel Xeon-E 2136
Storage: | 2 x 500GB SSD NVMe | 2 x 500GB SSD NVMe
Memory:  | 96-128GB DDR4         | 32GB DDR4

**3rd party server may be virtualized instead, if this is deemed a better route by KMD Admins for upcoming notary season.  Main server resources will be increased as necessary.**


---


## Contact Info

Discord: [Biz#0842](https://discord.com/users/402649850241482752)  
Email: whobiz@protonmail.ch  
GitHub: https://github.com/who-biz
Twitter: https://twitter.com/BizMunny
