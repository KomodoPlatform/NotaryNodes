# gcharang - Notary Node Proposal 2023 (Season 7)

## Regions and Voting Addresses

| Region | Address |
|--------|---------|
| SH  | RTWgfK47pbhyHWcqEMQUyEK6dtf7VpBYYB |
| AR  | RUbzhiGcGNeY2Nffi3NfH4pfjcjmhRcAiv |

<p align="center">
<table>
<tr ><td align="center"><strong>SH</strong></td><td align="center"><strong>AR</strong></tr>
<tr>
    <td align="center"><img src="../../qr_codes/gcharang_SH.png" width="50%" height="50%"></td>
    <td align="center"><img src="../../qr_codes/gcharang_AR.png" width="50%" height="50%"></td>
</tr>
</table>
</p>


## Who am I?

I graduated with a B.Tech in Engineering Physics and love solving problems. When I find an interesting problem, I scour all the available information for possible solutions and don't rest till I either solve it or know that people with more time and smarts than me have tried and failed :D . I first learned about Cryptocurrencies (Bitcoin specifically) in 2014, but didn't think much of it other than "Interesting tech!". Later, in 2018 I came across an article about the Mt. Gox hack and how Centralised Exchanges are security holes. Then I started reading about alternative solutions and came across Atomic Swaps and DEX's which obviously led me to Komodo. After discussing the Atomic Swap tech with the team and community for several days, I was convinced this was the real deal and left it at that. A few days later, I came across a discussion about the `51%` attack problem and there was Komodo once again, having solved it through `dPoW`. I was very fascinated and came back to the Komodo live chat server (Slack at that time) and started asking more questions and links to documentation.

While I was reading the documentation, I found that while the tech was cutting edge and most of it documented properly, it was scattered across Github wikis of multiple repositories and various websites. When I complained about this difficulty in access, I was offered the task of improving it :smiley: , which I gladly accepted and completed. I was offered the job to maintain and add to the documentation a few days later (around May 2018).

Since then, I was a part of the Komodo Team and helped in various ways including testing, documenting new tech, end user support, maintaining backend infra for various websites, implementing new sites that are responsive and SEO optimized etc. While Web Development, Support remain my major tasks today, I also created various tools that make testing and introduction to Komodo easier.

Some of them are:

- a playground for testing wasm version of atomicdex: https://atomicdex-play.lordofthechains.com/ Source: https://github.com/gcharang/react-atomicdex-wasm
- a directory of scripts(based on decker's omni installer) to install an explorer for a single smart chain https://github.com/gcharang/komodo-install-explorer
- a patch for the default insight explorer (decker's) that displays dPoW status and an ecosystem info banner https://github.com/gcharang/explorer-notarized
- a directory of scripts to create and manage a new Smart Chain using a single node https://github.com/gcharang/create-smartchain (it can also install an explorer)
- created two npm packages for accessing `komodod`'s RPC using browser and nodejs. https://github.com/gcharang/komodo-rpc-js , https://github.com/gcharang/node-komodo-rpc
- a bot that auto bans impersonators of people with roles in our Discord server; it also has some commands to ban mass joining bots
- a website to display notary testnet's stats: https://2023.notarytestnet.lordofthechains.com/ (Source repo: https://github.com/gcharang/notary-testnet-stats-ui)
- the script used to collect and save the notary testnet stats: https://github.com/gcharang/notary-stats-server
- I maintain pbca26's hw wallet tool at https://wallet.kmd.io

I was elected as a Notary Node for KMD for the first time in S4

I currently operate a DEV node: `gcharang_DEV`.

I was also a KMDLabs Notary Node operator and participated in Documenting most of the Komodo tech like Smart Chain creation(various launch parameters), Antara modules, nSPV, dexp2p, AtomicDEX-API etc.,

## Why Vote `gcharang`?

- The Komodo Notary Network needs reliable operators who will constantly monitor their own node and the network. They also need to update and upgrade their nodes on a daily basis to keep it healthy. I believe I can be one such operator based on my proven track record of being there for the community during the last `5` years as a team member and as a Notary Node since season 4.
- Creation of update documents for any change to the dPoW network. Example: Updating coins, adding a new coin, removing coins from the dPoW network etc.,
- Implementation of awesome new designs for our websites that are responsive/SEO optimized
- Misc scripts/packages/utilities/sites that make development on KMD and AtomicDEX easier

## Server Specifications (Main)

- CPU: Intel Xeon E3-1245v5 - 4c/8t - 3.5GHz /3.9GHz
- RAM: 64GB DDR4
- SSD: SoftRaid 2x450GB SSD NVMe

## Disclosure

- I am currently operating one NotaryNode in the SH region
- I was a Notary Node in the SH region with stats in the top 7 in Season 4
- I currently operate a DEV node
- I am a Komodo Team Member
- I ran a LABS Notary Node

## PGP Key

[My PGP Key](./my-pgp-key.txt)

## Contact details

- Discord handle: `gcharang#6833` (id: `423176312354635779`)
- Username on most platforms online: `gcharang`

## Keys for Season 7

```cpp
// mainnet
static const char *notaries_elected[NUM_KMD_SEASONS][NUM_KMD_NOTARIES][2] =
{
// ...
    {
        {"gcharang_SH", "02cb445948bf0d89f8d61102e12a5ee6e98be61ac7c2cb9ba435219ea9db967117"}, // RGcGxTnVbaVUBVoh5yxDqscLFWgfdeWALS
        {"gcharang_DEV", "033b82b5791c65477dd11095cf33332013df6d2bcb7aa06a6dae5f7b22b6959b0b"}, // RGcG4Ei5mPCHaGYvHfmqXLg9wBk7PFb8Co
        {"gcharang_AR", "030de3d833ba049da08231ca6b622c77c7f96b26269963291d9604706bb94031a5"}, // RGcGyeSRf3pjE7Lf872TXPAdAjEkcoiGb7
    },
// ...    
}
// 3p
static const char *notaries_elected[NUM_KMD_SEASONS][NUM_KMD_NOTARIES][2] =
{
// ...
    {
        {"gcharang_SH", "0321868e0eb39271330fa2c3a9f4e542275d9719f8b87773c5432448ab10d6943d"}, // RGcGe9dxpc4m6DqXge9wQr7sqVoyAs1Vho
        {"gcharang_DEV", "03a3878af1152f648e6084fd3fbe697a26b1c2e92d407dd96c375f45f7d3ca13bf"}, // RGcG9DNHKWVbjXm2GPMKMU9hkYvJWwweFo
        {"gcharang_AR", "039e01651c0afa1fc80b620301ff1981dd1db0f6c6b637b8f2f0fd986e9f5ece59"}, // RGcGW9C7kETbhaRr6jN8Nds2pk4FaQVr7L
    },
// ...    
```
