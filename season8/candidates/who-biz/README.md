
<img src="./RAuRSFQi7UhGLda1wCgTes7TyK55BC9yn9_NA.jpg"/>


<img src="./RV6MDNZ6t3zJWhvgyZTJfzMj55LBiMsmJM_AR.jpg"/>


Region | VOTE2024 Address
|:---|:---|
**NA** | `RAuRSFQi7UhGLda1wCgTes7TyK55BC9yn9`
**AR** | `RV6MDNZ6t3zJWhvgyZTJfzMj55LBiMsmJM`

**PLEASE TREAT NA REGION AS PRIORITY FOR ELECTION**

**NA Main pubkey:** 03170d900f6d6a13002255b708f7bd27e55b5c05d1ddbaf8c25a1fc287d9f804ed

**NA 3P pubkey:** 026d5cecdee3021a80416c3d8ac68e59fd3d77a954bbe88a8eee794ade6c58f411

**AR Main pubkey:** 03057d4c00c4e18f72faa4234aada9ad17ecd4bd9455c548edef16b94befa1a087

**AR 3P pubkey:** 03a185b059983a5479e3adba44eb5dde8d899468632ba30480301a9f1bbbcbc4a8


## Introduction

**Hi, I'm [Biz](https://github.com/who-biz).**  This is my 4th year running for election as a Notary Node operator, seeking my 3rd elected position.  I placed in 5th in North America rankings both of the last 2 years. As a result, I am running for a node in AR region as well.  Desire to run a node in AR rather than EU/NA is to strengthen the Notary Network.  2nd year running for re-election.  I ran for a 2nd node in SH region last year, which I did not win.  Hoping to change that this year.

I develop software (mostly in Rust as of late, but prefer C/C++) for a lot of different blockchains across the industry.  All except for one of these (in my present workday) are KMD-related in some manner.

I spend much of my time as Lead Developer of [The Blur Network](https://blur.cash).  For the past 4 years, nearly all of my work has focused on KMD-based technology, *and particularly dPoW*.  Skills and experience are split between XMR, BTC, ZEC, and Mimblewimble blockchain architectures.

Time over the past year was split mostly between EPIC, VRSC, and CHIPS (on Verus), with my work at VRSC taking priority most recently. Right now, this work centers around bringing Z-sends to Android, with an eventual goal of rewriting ZCash SDK functionalities into a Rust library.  This Rust library will ideally replace the existing reliance on lightwalletd servers, and will also perform cryptographic operations necessary for signing txs, etc.  Been working tightly with Mike Toutonghi Sr. And Michael Toutonghi Jr. on this.


## Focus of Recent Work

### VerusCoin VRSC

Right now, this work has become priority, and centers around bringing Z-sends to Android, with an eventual goal of rewriting ZCash SDK functionalities into a Rust library.  This Rust library will ideally replace the existing reliance on lightwalletd servers, and will also perform cryptographic operations necessary for signing txs, etc.  Been working tightly with Mike Toutonghi Sr. And Michael Toutonghi Jr. on this.


### Epic Cash EPIC

This work was priority before VerusCoin.  I worked as lead maintainer of EpicCash's full node software, and command-line wallet for the past year or so. My time spent there focused on making their software a lot more stable (and much faster), as well as debugging and fixing many long-standing or unknown bugs within the codebase.  Many of these are not present even  in Grin's codebase upstream.  I also began work on integrating Ledger HW wallets, which stopped after the Ledger controversies.  That work may still be finished if funding becomes available. I also got their explorer working again after the team running it abandoned the website, and disappeared.  This is not a fully exhaustive list, but for sake of brevity that's all I'll cover.  Feel free to ask more questions, or visit their repos (https://github.com/EpicCash/epic, https://github.com/EpicCash/epic-wallet) to see the commits I've authored, release notes I've published, etc.  Spent some time working with the folks at CypherStack as well, who write the mobile wallets for Epic, and worked for a long time in the Monero community before Monero's significant administrative shifts.


### CHIPS x VRSC

CHIPS development in the last 2 years has consisted largely of a full chain migration from a legacy Bitcoin backend to one of Verus's PBaaS chains.  In doing so, I've worked tightly with Mike from Verus, sg777 (game development on CHIPS), SHossan/Alien, and Satinder Grewal throughout this process.

### BLUR-dPoW

Since April 2019, I have been working on integrating dPoW with Blur (and more broadly: all Monero-based blockchains).  This is work I hope to conclude this year, after needing to take some time off to devote to non-volunteer (paid) work.

### dPoW/Notary Network

I do my best to contribute to a better understanding of `dPoW` in general, and make it a habit to contribute code upstream in all projects I work on.  After discovering that there was a far more efficient loop design (based on `blocknotify`), [I PRed these changes to the official dPoW repository](https://github.com/KomodoPlatform/dPoW/pull/445).  I am still hopeful this more efficient design will make it into the dPoW codebase eventually. 

I openly divulged the performance boosts I was gaining, and publicly explained how I was doing it, with the goal of bringing attention to ways in which Notary Nodes can act selfishly to game the system.  The objective in doing so was to improve the fairness and design of dPoW as a cross-chain security system.  

I believe fairness and a lack of hidden optimizations to be extremely important for dPoW as a system.  The Notary Network is designed in a way that creates (and rewards) direct competition between operators.  After these (now public) codebase modifications became controversial, I rolled back these changes.  I believe this shows my desire to strengthen KMD tech, rather than behaving selfishly in sole pursuit of re-election.  

Disclosing the code I was running publicly almost certainly affected my regional rankings in a negative way, and may have cost me automatic re-election.  **Please vote for me if you value this kind of public discourse and experimentation**.

### Public-Facing Stuff

I've done a number of interviews over the years, covering everything from BLUR, to KMD, to CHIPS x VRSC (with Mike present).  You can find the VerusCoin one here: https://x.com/bizmunny/status/1661514526993309696

### Research Papers

I am currently finishing up a paper that I am coauthoring with Brandon Gooddell (Surae Noether, formerly of Monero) that investigates, compares, and contrasts all existing modifications to the MimbleWimble Architecture for Non-Interactive Transactions. That paper will hopefully be finished soon, after I hear back on peer review from folks that are smarter than me. Hoping to get Daira Hopwood and David Burkett to weigh in on some specifics. I've also sent the paper to David Chaum for review.

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

- [`Verus-Mobile`](https://github.com/who-biz/Verus-Mobile/tree/fork-edgeapp-integrations) - Verus Mobile for Android with the latest ZCash SDK integrated (modifications to make this work on Verus are not done yet).

**Prior contributions during prior seasons testnets & elections:**


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
- Placed top 5 in NA region in 1st and 2nd year as a Notary Node Operator.
- Extensive development of CHIPS on Verus, writing tooling for migration of balances to new chain and development on new blockchain.  Nearly 100% of blockchain development to make this possible is performed by me.
- Prompt with updates to my Notary Nodes. High percentage of node uptime, as shown by last years scoring.
- Dedication of equal effort to 3P Node despite being optional.


---


## Why Vote Biz?

1. **Track record of performance in last 2 seasons**

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

- Other donations to KMD ecosystem have been removed, due to complications with taxes, and spending more time actually writing code for KMD-based projects.

*Calculations will be made at the beginning of each month, for the month prior.  Server costs will be covered first, and remaining rewards will be dispersed according to schedule above.  In events where KMD price is exceptionally higher than historical levels, NN Revenues may be liquidated mid-month to cover costs in a more effective manner.*


---


## Server Specs

*Please note server specs below are from prior year. Actual server used may vary with regional availability and pricing.*

Region: NA  |  Main Server | 3P Server |
|:---|:---:|:---:|
CPU:     | 2× Intel Xeon Silver 4214 (or similar) | Intel Xeon-E 2136
Storage: | 2 x 500GB SSD NVMe | Virtual (Docker)
Memory:  | 64GB DDR4         | Virtual

Region: AR  |  Main Server | 3P Server |
|:---|:---:|:---:|
CPU:     | 2× Intel Xeon Silver 4214 (or similar) | Intel Xeon-E 2136
Storage: | 2 x 500GB SSD NVMe | Virtual (Docker)
Memory:  | 64GB DDR4         | Virtual


---


## Contact Info

Discord: [whobiz](https://discord.com/users/402649850241482752)  
Email: whobiz@protonmail.ch  
GitHub: https://github.com/who-biz  
Twitter: https://twitter.com/BizMunny
