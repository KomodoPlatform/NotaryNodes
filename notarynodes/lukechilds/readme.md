<div align="center">
  <h1>Komodo Notary Node</h1>
  <img width="128" src="https://secure.gravatar.com/avatar/4af0d9a1f16bf05d1aedee5e3923d3e3?size=256" />
  <h2>lukechilds</h2>
  
  **Re-elected:** Asia (AR)
  <br>
  <br>
  **Running for Election:**<br>
  **Europe (EU)**<br>
  RV2evPRxFGk2ev7eRxUvWuzjYPWwQ2kpMC<br>
  **North America (NA)**<br>
  RLUKECH1LDSnotarynodeNAoqzRiNgrSfR<br>
</div>

## About Me

I'm an experienced software developer that's very active in the open source community and have been involved with cryptocurrencies since 2012. I've been working on open source software full time since 2016. For the last year I've been working almost exclusively on projects related to Komodo.

I've made over 1500 contributions to open source software in the last year and have lots of my own projects published on [GitHub](https://github.com/lukechilds/). My open source modules get downloaded [millions of times a month](http://npm-stats.com/lukechilds).

My open source software is used in production by small developers and large companies all round the world. Some examples of companies that are using my software are:

- GitHub
- Ethereum
- Signal
- Facebook

### Contact Details

I'm @lukechilds on Slack, [GitHub](https://github.com/lukechilds), [Twitter](https://twitter.com/lukechilds) and [Keybase](https://keybase.io/lukechilds). My personal email address is also listed on my GitHub profile. All my contact details are also on my wesbite [lukechilds.co](https://lukechilds.co).

## Why vote for me?

I was in a leading position throughout 2018 and as a result my AR node will be automatically re-elected for 2019. I would like to run for another node in the EU region and/or the NA region.

I have the experience required to run a notary node properly and securely with good performance as proven by my results last year.

If I'm elected I will be able to use the mining rewards to fund my work full time on open source and security research. I have many plans for open source projects that will benefit both the Komodo Platform and the entire cryptocurrency ecosystem as a whole.

### Contributions to The Komodo Platform

#### HyperDEX

I lead the development of [HyperDEX](https://github.com/atomiclabs/hyperdex), a GUI for Komodo's decentralised exchange network BarterDEX.

<div align="center">
  <img src="https://github.com/atomiclabs/hyperdex/blob/master/media/screenshots/exchange-view.png?raw=true" width="600" />
</div>

#### marketmaker

I've done extensive [debugging/testing/security auditing](https://github.com/search?utf8=%E2%9C%93&q=repo%3Ajl777%2FSuperNET+author%3Alukechilds&type=Issues) with `marketmaker`. The underlying daemon that powers the BarterDEX network.

#### Ledger KMD Reward Claim App

I built a [web application](https://github.com/atomiclabs/ledger-kmd-reward-claim) to allow users to claim KMD rewards held on Ledger devices.

<div align="center">
  <img src="https://github.com/atomiclabs/ledger-kmd-reward-claim/blob/master/screenshot.png?raw=true" width="600" />
</div>

This involved not only building the web application but also updating the code that runs on the Ledger for this to even be possible: https://github.com/LedgerHQ/ledger-app-btc/pull/84

#### Komodo Rewards JavaScript library

I built the [get-komodo-rewards](https://github.com/atomiclabs/get-komodo-rewards) JavaScript library to make it easier for third party developers to integrate Komodo reward claiming into their applications.

#### Locktime Support in Ledger Live

I submitted some code changes to Ledger that enables Ledger Live to set the locktime value on Komodo transactions allowing them to accrue rewards.

https://github.com/LedgerHQ/ledger-live-desktop/pull/1825

#### Security Auditing

I've discovered, responsibly disclosed, and submitted fixes for, a large number of critical security vulnerabilites existing in software in the Komodo ecosystem. If someone malicious had found some of these vulnerabilites before me, it could have lead to large loss of funds to users of the Komodo ecosystem.

##### High Severity

- [BarterDEX Daemon Insufficient Authentication Vulnerability](https://github.com/jl777/SuperNET/issues/563)
- [Agama Remote Code Execution Vulnerability](https://gist.github.com/lukechilds/34f117120611a5bfa81606501cb1ddf2)
- [Agama Insufficient Authentication Vulnerability](https://gist.github.com/lukechilds/820dde4df9b6d0c70cdbbfe2fb1bb646)

##### Medium Severity

- [Agama Weak Seed Encryption Vulnerability](https://gist.github.com/lukechilds/3b949ef63010fba9feb5a98a2c1379c9)
- [BarterDEX GUI Insecure Content Vulnerability](https://gist.github.com/lukechilds/7f7447cc51f88d2ce105aaf5e3c759a3)

### Experience

#### System Administration

I'm very experienced with system administration, I already run multiple nodes for other decentralised networks and have automated the process of running certain network services with my public Docker images. I've also run a high performing notary node for the last year.

##### Decentralised nodes

I have a proven track record of running decentralised nodes online with high uptime and high performance:

I've been running a Tor node since 2013. Due to high uptime and performance it was selected to be fallback directory mirror and is hard-coded into Tor's source code.

I also run a Vertcoin Electrum node. Likewise, this is [hardcoded](https://github.com/vertcoin-project/electrum-vtc/blob/44841d9668bd94f0a59fc311575770f29e73f6a1/lib/network.py#L57:5) into the Electrum-VTC source code as a bootstrap node due to high uptime and performance.

During excessive Vertcoin electrum traffic, all the electrum nodes went down apart from mine. My node (vtc.lukechilds.co) was single handedly processing all Vertcoin Electrum traffic and keeping everyone connected. [(proof)](https://www.reddit.com/r/vertcoin/comments/7j8l2h/working_electrum_nodes/)

##### Docker

I have published multiple public Docker images which have been downloaded over a million times.

I also built and maintain the official ElectrumX Docker image.

https://hub.docker.com/r/lukechilds/

#### Security

I also have good knowledge of network and application security. I have disclosed multiple vulnerabilities I've found in software.

##### Coinomi Mobile Wallet

I publicly disclosed the privacy issue of Coinomi leaking users wallet addresses in plain text after they ignored my multiple requests to reach out to them:

- https://cryptoinsider.com/content/coinomi-wallet-disclosure-denial-destructive-pr/index.html
- https://www.bitsonline.com/coinomi-vulnerability-respond/
- https://www.dashforcenews.com/coinomi-vulnerability-discovered-developers-react-harshly/
- https://cryptoble.win/2017/09/30/vulnerability-coinomi-devs-retaliate/

##### Buttercup Password Manager

I found and reported a vulnerability in a password manager's browser extension that would allow any website to read the entire contents of a users password store:

https://github.com/buttercup/buttercup-browser-extension/issues/92

## Server Details

### lukechilds_AR

- 16 Core CPU
- 64 GB RAM
- 1TB SSD

Will scale up as needed.

The server is hosted in Singapore in Asia.

|                       |                                                                       |
|-----------------------|-----------------------------------------------------------------------|
| **KMD Address**       | `RPxsaGNqTKzPnbm5q7QXwu7b6EZWuLxJG3`                                  |
| **BTC Address**       | `1FggVkVYrWBpibPtMwRQrNnPKy6vJEzJYf`                                  |
| **BTC Public Key**    | `031aa66313ee024bbee8c17915cf7d105656d0ace5b4a43a3ab5eae1e14ec02696`  |

### lukechilds_EU (not yet elected)

- 16 Core CPU
- 64 GB RAM
- 1TB SSD

Will scale up as needed.

The server will be hosted in the Netherlands in Europe.

|                       |                                                                       |
|-----------------------|-----------------------------------------------------------------------|
| **KMD Address**       |                                                                       |
| **BTC Address**       |                                                                       |
| **BTC Public Key**    |                                                                       |


### lukechilds_NA (not yet elected)

- 16 Core CPU
- 64 GB RAM
- 1TB SSD

Will scale up as needed.

The server will be hosted in the USA in North America.

|                       |                                                                       |
|-----------------------|-----------------------------------------------------------------------|
| **KMD Address**       |                                                                       |
| **BTC Address**       |                                                                       |
| **BTC Public Key**    |                                                                       |

## Disclosure

Some of the open source work I've done for Komodo has been funded by other community members (Pondsea), some work I've been awarded bounties for, and some work I've done for free out of the goodness of my heart :)
