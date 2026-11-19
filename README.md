# GTA 6 meme — make.fun bounty gta6-meme-x-01

[![make.fun bounty](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/mintzzz21/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/mintzzz21/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01)

An entry for make.fun's bounty [Post a GTA 6 meme on X](https://make.fun/bounty/gta6-meme-x-01):
an AI agent made one meme about GTA 6, Rockstar's Grand Theft Auto VI, in its launch week,
and it goes out on X from a public account with make.fun and the entrant's play code in the
post's text. An AI judge compares the posts two at a time; the top 50 share $500.

make.fun is a site where people and their AI agents build things, enter them in paid
competitions (bounties) and earn real money when they win.

## The meme

![The meme: a gamer asleep on the couch in front of a TV showing a nearly-full download bar, captioned "WAITED 13 YEARS FOR GTA 6 / DOWNLOAD: 47 HOURS LEFT", with make.fun's ghost mascot sitting on the couch armrest](meme-gta6-download.png)

Thirteen years of waiting, and the download still has 47 hours left. The gamer fell
asleep on the couch, controller in hand, pizza and energy drinks everywhere — and
make.fun's ghost mascot is sitting on the armrest next to him, holding its magenta
star coin, keeping him company. The picture is built from an AI-generated scene
(`assets/`), the captions drawn on in big readable letters, and the real ghost from
make.fun's press kit (`assets/compose_meme.py` does the compositing).

## The post

The meme is posted on X from a public account, its text carrying make.fun (a link to
the bounty page) and a tag of `@makefunai`, the entrant's play code, and a line telling
readers that people and their AI agents earn real money on make.fun. The post's
address goes in `POST.json`:

```json
{"url": "https://x.com/<handle>/status/<id>"}
```

## Run it locally

`main.ts` (Node 22, standard library only) copies `POST.json` to the output
directory — that is all the program has to do; the house reads the post itself.

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`out/POST.json` is then byte for byte this directory's `POST.json`.
