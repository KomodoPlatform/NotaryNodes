# NN Season 5 Proposal for ***dathbezumniy***



Hi, I've joined Komodo team a year ago as a junior QA engineer, since this was my first tech job ever, I have to say that previous roles as a Sales or PM didn't prepare me even a tiny bit to join this brilliant team, but you have to start somewhere right? Gladly during those "white collar" years my main hobbies were coding in python which I did for countless hours in a row and ofc mining eth with GPU rigs! Honestly speaking, I dont have anything to brag about in my life before kmd happened so I decided to just tell you a story of my first year at KMD. Trying to cut it as short as possible, hopefully for your amusement or at least for an almost silent and neurotic laugh at some point =P

This is an unnescessary offtop that you can <a name="end">skip</a>, but I feel like even though marketing is always ready to talk to community, our team is mostly closed off in our tasks and duties and does not have the time to properly convey what is going on inside (and I'm not saying its unhealthy, on the opposite it is the way its supposed to be).

As a first task at KMD, I've managed to release a very very early alpha version of kmd-sync-api (https://github.com/dathbezumniy/kmd-sync-api) and kmd-sync-bot (https://github.com/dathbezumniy/kmd-sync-bot). Would love your opinion here NNOPs and please let me know if I should enrich/branch those projects out with more functionality for notaries, add security (for example) so this could be run in production... or even something else that you wish nn-tg bot should have.

Next task was to monitor electrums uptime that we use for adex GUIs. Obviously, real monitoring should be done with more sophisticated tools, so this project goal is to simply prove to users that issues they are having atm are not because of electrums downtime, but also a handy tool to check for yourself once in a while when no one is around :) [https://eyelectrumx.herokuapp.com/](https://eyelectrumx.herokuapp.com/)

And then the big game started ahah!!! [500KMD Bounty for a new Protocol integration](https://github.com/KomodoPlatform/atomicDEX-API/issues/723) into atomicDEX-API! Wow! Can I do it?! yea! Now we are in the big league boiz! :D Deploying Smart Contracts and Reaping the bounties!!!

Another day, another dollar. Now I'm the _main_ QA on the [QRC20 Swap Integration](https://github.com/KomodoPlatform/atomicDEX-API/pull/735) into atomicDEX-API. Was I scared? hell yeah. Did I read every doc imaginable about QTUM and QRC20? most probably. Did I approve the PR? hell yea, after finding a few crucial bugs ofc. pew pew. xD

So... in for a pound, in for a penny. Now I'm the _only_ QA on QRC20 mobile GUI integration (Tony's chilling on vacation) Let me tell you... if a few strategic issues weren't opened that day before release, most of mobile qrc20/qtum users would be spamming #support with a lot of confusion in their hearts!
Gladly that all got sorted out, but afterwards one thought was stuck in my and Yurii's head (our mobile team lead), and that thought was... more autotests! more autotests!!! MOAR AUTOTEZTZ!!11

The need arises and so... please welcome Sir MOAR AUTOTEZT at your service:

<img src="gifs/create.gif" width="125" height="250" />
<img src="gifs/restore.gif" width="125" height="250" />
<img src="gifs/txs1.gif" width="125" height="250" />
<img src="gifs/txs2.gif" width="125" height="250" />
<img src="gifs/txs3.gif" width="125" height="250" />
<img src="gifs/txs4.gif" width="125" height="250" />
<img src="gifs/txs5.gif" width="125" height="250" />
<img src="gifs/orderbooks.gif" width="125" height="250" />

Just a start, but from 0.4.0 onward these tests are going to run on every PR and on every mobile device that I can get my hands on, making sure nothing essential breaks down and you will always be in controll of your dexperience :D

<a href="#end">So</a>, an introduction... hehe. "Long story short" since last month I'm a junior flutter dev at kmd. For the next year will be bringing you new features on a mobile gui as well as an up-n-coming webdex.