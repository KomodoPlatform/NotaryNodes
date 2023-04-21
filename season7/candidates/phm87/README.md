# phm87 

## Season 7

I'm candidate to be Notary Node during the 2023-2024 season in order to continue to notarize and support projects using Komodo tech !

## Voting Address ##


| SH region |
| --- |
| ```RYBMXPrMQGw21bdc3MHNh2ZBwmBiPhitsh``` |

- Thank you -
```

## Who am I ?

<table style="border: 0px;">
  <tr>
    <td>
      <img src="https://unimining.net/images/logo_unimining.png" alt="drawing" style="float: right;" />
    </td>
    <td>
I'm running UniMining.net mining pool since September 2017 with friends. We contributed to yiimp opensource project and we helped some coin developers. I'm working in IT since 10 years (including payment card industry, insurances and logistics) and I entered the world of cryptocurrencies in april 2017.
    </td>
  </tr>
</table>
I've been Notary Node operator since 2019-2020 season (phm87_SH and phit_SH) and Community Contributor, I contributed to iguana/dPoW, Chips and Komodo ecosystem.

Thank you to Komodo Team for open-minded discussions, sharing knowledges about Komodo tech and other projects.

Big thank you to the whole Komodo community and ecosystem. Specials thanks to jl777, metaphilibert, Ludom, SHossain, blakjok3r, Alright and ca333.


phm87

# Server requirements:
- Intel Xeon E3-1245v5 - 4c/8t - 3.5 GHz/3.9 GHz
- 64GB ECC
- NVMe 1.2 To RAID

# Pledges for season 6

After servers payment (and taxes over donations, if any), a total of **14%** of Notary Node mining rewards will be donated as support to projects:
- 8% to non-profit russian-ukrainian association
- 3% to CHIPS
- 3% to Biz for past and future projects (if Biz is not elected as Notary Node)

Donations will be performed at the beginning of each month, for the month prior. Server costs will be covered first (and taxes over donations, if any) and remaining rewards will be sent according to allocations defined here above.

## 2021-2022 Projects/milestones

Ongoing preparation of presentations (and meetup) of Bitcoin and cryptocurrencies (using Komodo technologies).

Projects under NDA for now, sorry. I hope public exposure soon.


## 2020-2021 Projects/milestones

### Integration of aPoW into CHIPS
- <span style="color:green">[SUCCESS]</span> **Integration of aPoW into CHIPS**: Final cleanup and testing of the code (thank you SHossain for the help with your ASIC), successfull network hard-fork ! This integration was supported by a bounty and I received personal donations but my Notary Node was helpful to test my new CHIPS code when notarizing on the Notary Node.

https://github.com/chips-blockchain/chips/pull/2

https://github.com/chips-blockchain/chips/pull/3

https://github.com/chips-blockchain/chips/pull/4

https://github.com/KomodoPlatform/dPoW/pull/193

<img src="chips_apow_HF.png" alt="drawing" width="80%" height="80%" />

<img src="https://user-images.githubusercontent.com/31578435/88123868-14be3c80-cbcc-11ea-8a74-73252f918359.png" alt="drawing" width="90%" height="90%" />

<img src="https://user-images.githubusercontent.com/31578435/88123895-21429500-cbcc-11ea-8a13-bccbf05050b0.png" alt="drawing" width="90%" height="90%" />

### -ac_aur : new parameter to enable active user rewards for smartchains !
- [DEV FINISHED] **-ac_aur=** this new parameter allows to have **active user rewards enabled for smartchains**: the code of Komodo's active user rewards is used, I added conditions to allow it for smartchains. I tested it locally then TAUR testchain was launched in KMDLabs. I will contact TonyL to ask help to run pytests of KMD to avoid regression then I'll pull request this change to komodo source.

Please feel free to review https://github.com/KomodoPlatform/komodo/compare/master...phm87:ac_aur

Update 2022: Core changes in code of Active User Rewards will need to rebase and align the branch before submitting again the PR.

<img src="TAUR_help.png" alt="drawing" width="90%" height="90%" />

https://gist.github.com/phm87/fc75d5820d232376a8256874726673b4

https://discord.com/channels/412898016371015680/497080413387489291/780873228838895626

<img src="TAUR_getinfo.png" alt="drawing" width="60%" height="60%" />

### -ac_naur
- [DEV STOPPED] **-ac_naur=** this runtime parameter allows to have **negative active user rewards enabled for smartchains**: my code doesn't work and community demand for negative rates is low so I stopped this development until some demand exists.

<img src="TNAUR_test.png" alt="drawing" width="60%" height="60%" />

https://github.com/phm87/komodo/tree/ac_naur

### Fix KMDLabs Notarization Network
- [SUCCESS] **Fix KMDLabs Notarization Network** by adding back dpowlistunspent RPC call to komodo source code (using blackjok3r implementation): 

https://github.com/KomodoPlatform/komodo/pull/380

Thank you to the whole KMDLabs Team and special thanks to daemonfox !

<img src="KMDLabs_notarizations_fixed.png" alt="KMDLabs_nota_success" width="60%" height="60%" />

- iguana contributions & tests

https://github.com/KomodoPlatform/dPoW/pull/158

https://github.com/KomodoPlatform/dPoW/pull/186

https://github.com/KomodoPlatform/dPoW/pull/187

https://github.com/KomodoPlatform/dPoW/pull/201

https://github.com/KomodoPlatform/dPoW/pull/202

- Tiny komodo contributions:

https://github.com/KomodoPlatform/komodo/pull/406

https://github.com/KomodoPlatform/komodo/pull/383


### Raise awareness about dPoW and KMD tech (outside of KMD Discord)
- Support of Komodo ecosystem on the **mining pool** (SPACE, WSB, SOULJA added)

- Discuss about notarization outside of Komodo discord

https://gist.github.com/phm87/58ed4498f8cbb77aa3771d0cc7863528

<img src="KMD_love_outside_of_KMD_discord.png" alt="drawing" width="60%" height="60%" />

- Discuss on discord about features of KMD tech

<img src="KMD_tech.png" alt="drawing" width="90%" height="90%" />


## 2019-2020 Projects/milestones
Here is a part of my past contributions.

- [Fix/enhance stopcoin & pausecoin into iguana/dPoW](https://github.com/jl777/SuperNET/pull/1113)
- [Small fix to Chips](https://github.com/jl777/chips3/pull/36)
- Other small iguana enhancements
- https://github.com/DeckerSU/komodo_scripts/pull/4
- https://github.com/DeckerSU/komodo_scripts/pull/5
- Contributions to 2019 NN testnet repository
- Small fixes to Komodo (dpowconf, 

- Add dpowlistunspent and cleanwallettransactions to each 3P coin (Hush, VRSC, EMC2, GAME, Chips, Bitcoin), no PR yet because some issues still remain.
- https://github.com/blackjok3rtt/komodo/compare/FSM...phm87:force-rescan
- Continuation of PR 1113/1114: https://github.com/jl777/SuperNET/compare/blackjok3r...phm87:patch-10
- https://github.com/KMDLabs/StakedNotary/compare/master...phm87:patch-2
- https://github.com/jl777/SuperNET/compare/blackjok3r...phm87:ktnn
- https://github.com/jl777/SuperNET/compare/blackjok3r...phm87:phm87

Discussions:
- https://github.com/KomodoPlatform/komodotools/compare/master...phm87:checkfork_compare-last_notahash -> https://github.com/webworker01/komodotools/commit/4fb896399f67433547161c98d9b3984237d28291
- https://github.com/KomodoPlatform/komodotools/compare/master...phm87:cronsplit-estimatesmartfee

# Relations and agreement :
No agreement and no official relation with any entity. I'm friend with d4v who runs UniMining.net with me.

I have a friendly relationship with crackers of zpool, metaphilibert and Ludom.

I am not part of KMD Team but I am iguana/dPoW & komodo contributor.

# Contact details :

Slack : @phm87

Discord : phm87#7395

Bitcointalk : https://bitcointalk.org/index.php?action=profile;u=1117726
