<img src="https://avatars.githubusercontent.com/u/37732338?v=4" width="250" height="250"/><img src="./REyFgygqWpDtYjKhz214CkA6hrA27d6cxX.jpg" width="250" height="250"/>

Region | VOTE2021 Address 
|:---|:---|
**NA** | `REyFgygqWpDtYjKhz214CkA6hrA27d6cxX`

## Introduction

**Hi, I'm [Biz](https://github.com/who-biz).**

I founded a blockchain project called [The Blur Network](https://blur.cash) in June of 2018.  I spend most of my time as Lead Developer of Blur.

Since April 2019, my work has centered around integration of Blur (and more broadly: all Monero-based blockchains) with Komodo's "Delayed Proof of Work" software.

This effort began after I was approached by jl777 and offered a period of support by KMD's notary network, in exchange for integration of Blur with dPoW.

With such an ongoing and cooperative relationship between KMD and BLUR, I believe there are unique benefits that my election as a S5 Notary Node Operator can provide to the Komodo ecosystem.

## Development Efforts in the Komodo Ecosystem

- [`dpow-blur`](https://github.com/blur-network/dpow-blur) - Upgraded version of [`blur`](https://github.com/blur-network/blur) full node software, for compatibility with KMD's dPoW.

  - This was the bulk of the last two years of work.  DPoW required rewriting existing logic into our codebase.  DPoW occurs in a separate section of the mempool called the notarization pool; allowing  100% of the notarization process to be visible to the larger network.  Data for BTC-like txs is mocked, or replaced with valid Blur (XMR-style) data.

- [`blur-api-cpp`](https://github.com/blur-network/blur-api-cpp) - A compatibility layer for interfacing with `iguana`'s API, negotiates between JSON-RPC specifications.

  - List of API calls available over `blur-api-cpp` are [available here](https://github.com/blur-network/blur-api-cpp/blob/master/INSTRUCTIONS.md#rpc-methods).

- [`blur-explorer`](https://github.com/blur-network/blur-explorer) - A testnet explorer for The Blur Network, which features new dPoW mechanics for XMR-based blockchains.

- [`blur-network/dPoW`](https://github.com/blur-network/dPoW/tree/blur-2021-testnet) - Modified `2021-testnet` dPoW with added files for notarizations of BLUR->KMD.

  - Instructions for addition of Blur as 3P coin, to existing 2021-testnet NN network [available here](https://github.com/blur-network/dpow-blur/blob/testnet/docs/kmd-2021testnet-setup.md).
  
- [`who-biz/komodo_scripts`](https://github.com/who-biz/komodo_scripts/tree/from-wif) - Modified `genkomodo.php` script, to generate litecoin keys/addresses from a user-supplied WIF

  - Used by some `2021-testnet` operators in LTC testnet.

- [`who-biz/nntools`](https://github.com/who-biz/nntools/tree/2021-testnet) - Modified `webworker01/nntools` for testnet, added `txid` column for display when running `stats`.

  - Also used by some `2021-testnet` operators for LTC testnet.

## Community Efforts

- Participant in S5 Notary Node testnet 
- Post regular updates about development progress in [#blur channel of Komodo Discord](https://discord.gg/9GJ6J5u)
- Began contributing to CHIPS development recently. I plan to continue this work, and get more involved in `lightning`-related development [[1]](https://github.com/chips-blockchain/bet/pull/202), [[2]](https://github.com/chips-blockchain/lightning/issues/9), [[3]](https://github.com/chips-blockchain/lightning/issues/11)
- Will be attending Komodo's [Notary Node Election 2021 Info Event](https://blog.komodoplatform.com/en/notary-node-election-2021-info-event/)
- Received a Certificate of Recognition from Komodo team this past year

## Why Vote Biz?

1. **I will be a technical liaison for KMD & BLUR (and future XMR-based integrations)**
 
Blur is already being integrated with the same systems run by KMD's notary network.  Being a S5 Notary Node Operator would provide me with the opportunity to work with the software I've been writing, in the most hands-on way.  This will benefit both KMD and BLUR via quicker problem-solving while integrating Blur, as well as any other XMR-based chain which DPoW may secure in the future.

2. **Notary Node rewards will allow me to focus more time on KMD ecosystem projects**

I've enjoyed working in the Komodo ecosystem for the past couple of years.  In that time, I've grown an appreciation for the community and technology at KMD.  I'd really like to build more solutions to make cross-ecosystem interoperability a reality.  Komodo seems the best and most receptive place to do so. CHIPS/lightning development also seems very interesting.

3. **You'll be guaranteed a very active Notary Node Operator**

With Blur being integrated with DPoW, much of my time will be focused on interfacing with Komodo's network.  Put simply, I'll be available and active every day.

4. **Passion for problem solving, and building new solutions**

I plan on building more bridges like the `blur-dpow` referenced above.  I'll also be active in helping KMD increase its compatibility with 3rd party blockchains.

## Server Specs

Region: NA  |  Main Server | 3P Server |
|:---|:---:|:---:|
CPU:     | AMD Epyc 7351P     | Intel Xeon-E 2136
Storage: | 2 x 500GB SSD NVMe | 2 x 500GB SSD NVMe
Memory:  | 128GB DDR4         | 32GB DDR4

## Contact Info

Discord: [Biz#0842](https://discord.com/users/402649850241482752)  
Email: whobiz@protonmail.ch  
GitHub: https://github.com/who-biz
