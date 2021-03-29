# VOTE2021 Address (SH region):

RFmvveVYVRPo8v85J5u3Yd3PgrzSrHZP4S

I'm candidate to be Notary Node during the 2021-2022 season in order to continue to notarize, move to a better server and provider, continue to develop my current ongoing projects and launch/support new projects !

## Who am I ?

![](https://unimining.net/images/logo_unimining.png =250x)
I'm running UniMining.net mining pool with 30 - 40 altcoins since September 2017 with friends. We contributed to yiimp opensource project and we helped some coin developers. I'm working in IT since 10 years (including payment card industry) and I entered the world of cryptocurrencies in april 2017.

I've been Notary Node operator of phm87_SH and Community Contributor since 2019, I contributed to iguana/dPoW, chips and Komodo ecosystem.



## 2020-2021 Projects/milestones
- [SUCCESS] **Fix KMDLabs Notarization Network** by adding back dpowlistunspent RPC call to komodo source code (using blackjok3r implementation): 
https://github.com/KomodoPlatform/komodo/pull/380
Thank you for daemonfox for your support !
TDO: Add printscreen
- [SUCCESS] **Integration of aPoW into CHIPS**: Final cleanup and testing of the code (thank you SHossain for the help with your ASIC), successfull network hard-fork ! This integration was supported by a bounty and I received personal donations but my Notary Node was helpful to test my new CHIPS code when notarizing on the Notary Node.

https://github.com/KomodoPlatform/dPoW/pull/193
TODO: Add links + printscreens
- [DEV FINISHED] **-ac_aur=** Beginning of development of -ac_aur (see details here above)
- [DEV STOPPED] **-ac_naur=** this runtime parameter allows to have **negative active user rewards enabled for smartchains**: my code doesn't work and community demand for negative rates is low so I stopped this development until some demand exists.
TODO: Add link
- [DEV ONGOING] Beginning on the creation of a **multicurrency faucet** using AtomicDEX-API in the back-end
TODO: Update code, Add links
- Support of Komodo ecosystem on the **mining pool** (SPACE, WSB, SOULJA added)
TODO: Add printscreens
- Discuss about notarization and Komodo outside of Komodo discord
https://gist.github.com/phm87/58ed4498f8cbb77aa3771d0cc7863528
TODO: Add printscreens
- iguana contributions & tests
https://github.com/KomodoPlatform/dPoW/pull/158
https://github.com/KomodoPlatform/dPoW/pull/186
https://github.com/KomodoPlatform/dPoW/pull/187
https://github.com/KomodoPlatform/dPoW/pull/201
https://github.com/KomodoPlatform/dPoW/pull/202
- Tiny komodo contributions:
https://github.com/KomodoPlatform/komodo/pull/406
https://github.com/KomodoPlatform/komodo/pull/383


## 2021-2022 Projects/ideas

Most of these projects are ongoing. The NN earnings will be helpful to support these projects.

### AtomicDEX
- I began to work on a multicurrency **discord faucet** using AtomicDEX-API in the back-end. The lightwallet features are used but not (yet) the DEX features. Public testing will begin soon.
The withdraw function of AtomicDEX-API is used in the current implementation but we can use batch transactions to send coins to faucet users to lower fees (sendmany equivalent), I began to work to adapt AtomicDEX-API to have a new rpc call similar to sendmany but I'm very new to rust.
This **discord faucet** can be a good introduction of AtomicDEX to coins'teams. The demand for disord faucets & tipbots is increasing due to the Bubble.

- **Add and test ERC20 (and BEP20) into AtomicDEX**: I'd like to add and test some ERC20 (and BEP20 when possible) on AtomicDEX-API: 1MT and WSCRT, two ERC20 so I won't need to run any electrumx since it relies on Ethereum (or Binance Smart Chain) blockchain. 
Why 1MT ? See explanations here below (cross-chain development).
Why SCRT and WSCRT ? WSCRT is SCRT wrapped on ethereum. I know IRL a SCRT Team member so we need to integrate more our ecosystems. SCRT allows to execute private smart contracts using special hardware and HSM, their system is very interesting technologically. Maybe it can be interesting to create a bridge between SCRT and ARRR. Will we see a future bARRR/bSCRT LP farm on pancakeswap in the future ? i won't describe all SCRT features in this proposal but I think that many bridges are possible between our communities.

https://gist.github.com/phm87/e62ad935e5d55be1ec1fe9732fdf3be2

https://github.com/KomodoPlatform/coins/compare/master...phm87:patch-1

https://github.com/KomodoPlatform/atomicDEX-Desktop/compare/dev...phm87:patch-1
TODO: Add cipi remarks

- **Integration and support of coins into AtomicDEX**: When a coin is added on my mining pool, I'd like to run an electrumx for it then add it on AtomicDEX and on the discord faucet. we can't rely on KMD Team to run electrumx for many coins. This additional infrastructure will be paid with NN earnings.
Adding suport for SCRT will require more work since SCRT blockchain is a based on cosmos (and cosmos not yet supported on AtomicDEX).

- About **integration of AtomicDEX into yiimp**, since most of the code is ready, I'm planning to perform more tests, document it properly, add helpers about how to use and configure. A pull request can be done when more testing will be done.

- About **integration of LN submarive swaps into AtomicDEX**, except the BTC node on my main Notary Node, I don't have any BTC node anymore. I will run a testnet LN node and testnet BTC node to be able to work on this development. Komodo Team doesn't support LN, I don't think that a pull request will be accepted. But users'demand and network effect may be worth the work in addition to LN low fees.

### CHIPS
- The **chips-qt** needs to be fixed and enhanced (TODO: check that it is still to be done)
- Support of chips in the discord faucet (using AtomicDEX-API in the back-end)
- I'd like to **enhance some rpc calls** about cpu mining (details to be discussed with chips team)

### Cross-chain development
- I discussed on discord and slack how to **airdrop a smartchain/token to all hodlers of an ERC20 (or BEP20)** ? I'd like to do the experiment on 1MT token then later on other tokens. It is not possible to calculate the pubkey based on an ERC20/ethereum address that never sent funds nor signed a message. Using the message (or transaction) signed, we can derive the pubkey. Given current Ethereum fees, one solution discussed is to create a web3 webpage asking to sign a transaction (or message), don't broadcast it on Ethereum mainet network, then retrieve it offchain and verify the signature offchain. A CC adapted can be useful (or a CC "node" as discussed with Alright).

Why 1MT? 1MT use cases are similar to PANGEA's and CHIPS' ones (poker, gambling, online casinos). Team sizes are similar, but Chips Team is more orientated on tech side, while 1MT team is focused on marketing. 1MT is not searching to partner with CHIPS now (as no official discussion happened, projects' teams don't know each other). But if we give some tech support to 1MT (integration into AtomicDEX exchange, airdrop test using 1MT hodlers list, web3 tests on BSC using 1MT, faucet), maybe partnerships will be possible with CHIPS. Chips Team is doing a great job but the marketing skills of 1MT Team are above Chips Team. The discord presence of 1MT is important. But about tech, we can give support and help 1MT to get stronger. I think that at the end, both communities can become stronger united.

https://gist.github.com/phm87/e05912920dabbfb64f943b6a6a047d58

### Komodo enhancements/developments

- [TESTS ONGOING] **-ac_aur=** this runtime parameter allows to have **active user rewards enabled for smartchains**: the code of Komodo's active user rewards is used, I added conditions to allow it for smartchains. I tested it locally then TAUR testchain was launched in kmdlabs. i will contact TonyL to ask help to run pytests of KMD to avoid regression then I'll pull request this change to komodo source.
TODO: Add link + printscreen
https://gist.github.com/phm87/fc75d5820d232376a8256874726673b4
https://discord.com/channels/412898016371015680/497080413387489291/780873228838895626

- [TESTS ONGOING] New RPC call **validateaddressgeneric** to verify an address belonging to any coin. This rpc call is not specific to Komodo, it can be added into AtomicDEX-API but since the aim was to try to run it on the mining pool using yiimp architecture, a coin daemon is more suitable. As discussed with Alright, many other RPC calls unrelated to Komodo were added to Komodo. Maybe I'll pull request this RPC call into phm87 branch.

https://github.com/KomodoPlatform/komodo/compare/master...phm87:patch-23


### TO FINISH !!!

run komodo on ARM hardware, HSM integration for iguana & yiimp

I tested many things on my phm87_SH node during the 2019-2020 season: my notarization performances were sometimes in the top 3 and sometimes very low. Whatever many notary nodes were impressed by these performances, my node was not re-elected.

KMD Team was very kind and created recently a phm87 branch for my contirbutions to Komodo. I was very pleased to have open-mindid discussions with jl777 about Lightning Network, Komodo and some technical aspects of crypto. I was very happy to give additional support to KMDLabs, Chips, WLC21 and other projects.

Big thank you to the whole Komodo community and ecosystem. Specials thanks to jl777, blakjok3r, Alright and ca333.


phm87

# Server requirements:
Servers specifications will be fine tuned according to requirements for season 2020-2021:
- Intel Xeon E3-1245v5 - 4c/8t - 3.5 GHz/3.9 GHz
- 128GB ECC
- NVMe 1.2 To RAID

# Contact details :
Slack : @phm87
Discord : phm87#7395
Bitcointalk : https://bitcointalk.org/index.php?action=profile;u=1117726

# Past contributions and ongoing work:
Here is a part of my past contributions.

- [Fix/enhance stopcoin & pausecoin into iguana/dPoW](https://github.com/jl777/SuperNET/pull/1113)
- [Small fix to Chips](https://github.com/jl777/chips3/pull/36)
- Other small iguana enhancements
- https://github.com/DeckerSU/komodo_scripts/pull/4
- https://github.com/DeckerSU/komodo_scripts/pull/5
- Contributions to 2019 NN testnet repository
- Small fixes to Komodo (dpowconf, 

## Ongoing:
- [Add AtomicDEX support into yiimp](https://github.com/tpruvot/yiimp/compare/next...phm87:AtomicDEX): Orderbooks, manual trading, get prices ... The support of AtomicDEX will add all mm2/AtomixDEX coins into the database of each yiimp pool that merges this future PR. ca333 was very kind and he gave me some RICK and MORTY, I'm planning to let anonymous visitors use the yiimp interface to perform RICK/MORTY trades.
- Add dpowlistunspent and cleanwallettransactions to each 3P coin (Hush, VRSC, EMC2, GAME, Chips, Bitcoin), no PR yet because some issues still remain.
- https://github.com/blackjok3rtt/komodo/compare/FSM...phm87:force-rescan
- Continuation of PR 1113/1114: https://github.com/jl777/SuperNET/compare/blackjok3r...phm87:patch-10
- https://github.com/KMDLabs/StakedNotary/compare/master...phm87:patch-2
- https://github.com/jl777/SuperNET/compare/blackjok3r...phm87:ktnn
- https://github.com/jl777/SuperNET/compare/blackjok3r...phm87:phm87

## Discussions:
- https://github.com/KomodoPlatform/komodotools/compare/master...phm87:checkfork_compare-last_notahash -> https://github.com/webworker01/komodotools/commit/4fb896399f67433547161c98d9b3984237d28291
- https://github.com/KomodoPlatform/komodotools/compare/master...phm87:cronsplit-estimatesmartfee
