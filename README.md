# TikTok Scraper - Hashtags, Profiles, Sounds & Video Stats

**Run it on Apify: [apify.com/clearfetch/tiktok-scraper](https://apify.com/clearfetch/tiktok-scraper)**

Scrape TikTok without logging in: a hashtag's total views and its top videos, a profile's followers and its
latest videos, a sound's top videos, and full public stats for any video link: views, likes, shares, comments,
saves, post time, duration, hashtags, sound and author. **$1.00 per 1,000 results.** No cookies, no proxy, no
browser.

## What data you get

**Videos** (one row each, same columns every time):

- `playCount`, `diggCount` (likes), `shareCount`, `commentCount`, `collectCount` (saves), `repostCount`
- `createTimeISO`, `durationSeconds`, `text` (caption), `hashtags`, `mentions`, `textLanguage`,
  `locationCreated`, `isAd`, `isAiGenerated` (TikTok's own AI label)
- Sound: `musicTitle`, `musicAuthor`, `musicOriginal` (the creator's own audio or not), `musicUrl`
- Author: `authorUsername`, `authorNickname`, `authorFollowers`, `authorLikes`, `authorVideoCount`,
  `authorVerified`, `authorId`, `authorSecUid`
- Where it came from: `source` (hashtag, profile, sound or url), `sourceValue`, and `sourceRank`, its position
  in that list

**Hashtags**: total `viewCount` and `videoCount` across all of TikTok. **Profiles**: `followers`, `following`,
`likes`, `videoCount`, `bio`, `bioLink`, `verified`, account creation date. **Sounds**: `artist`, `videoCount`,
`title`.

## How to use

1. Add hashtags, usernames, sound links or video links, one per line (or mix them all in **startUrls**).
2. Optionally keep only recent videos (**Only videos newer than**: "7 days", "2026-09-01") or widen a niche
   with **Related hashtags to follow**.
3. Run it, then download JSON, CSV or Excel, or pull the rows through the API.

## Input

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `hashtags` | array | — | Hashtags, with or without `#`. Summary row plus the hashtag's top videos. |
| `profiles` | array | — | Usernames or profile links. Summary row plus the latest 10 videos. |
| `sounds` | array | — | Sound links or ids. Summary row plus the sound's top videos. Also `musics`. |
| `postURLs` | array | — | Video links, share links or ids. Also `urls`, `videoUrls`, `startUrls` (any mix). |
| `fetchVideoDetails` | boolean | `true` | Read each video's page for likes, shares, comments, saves, sound and author stats. Off is several times faster and keeps views, caption, cover, author and date. |
| `newerThan` | string | — | A date or an age like `"7 days"`. Older videos are left out and not charged. |
| `relatedHashtags` | integer | `0` | Also scrape this many hashtags that appear most on the videos found. |
| `maxVideosPerSource` | integer | `0` | Cap per hashtag, profile or sound. `0` means all TikTok lists. |
| `includeSummaryRows` | boolean | `true` | One row per hashtag, profile and sound alongside the videos. |
| `includeRaw` | boolean | `false` | Add TikTok's untouched objects as `raw`. |
| `maxConcurrency` | integer | `3` | Pages read in parallel. |
| `timeoutSecs` | integer | `30` | Per request. Pages without data are retried. |
| `proxyConfiguration` | object | off | Not needed. Available for very large volumes. |

## Output example

From a real run with `"postURLs": ["https://www.tiktok.com/@tiktok/video/7106594312292453675"]` (media links shortened):

```json
{
  "ok": true,
  "type": "video",
  "id": "7106594312292453675",
  "webVideoUrl": "https://www.tiktok.com/@tiktok/video/7106594312292453675",
  "text": "how many frogs did you find? 🐸 check out tiktok’s #Minecraft community today! @Gorillo",
  "createTime": 1654632929,
  "createTimeISO": "2022-06-07T20:15:29.000Z",
  "playCount": 581200,
  "diggCount": 98900,
  "shareCount": 358,
  "commentCount": 1337,
  "collectCount": 59239,
  "repostCount": 0,
  "durationSeconds": 24,
  "hashtags": [
    "minecraft"
  ],
  "mentions": [
    "gorilloyt"
  ],
  "isAd": false,
  "isAiGenerated": false,
  "locationCreated": "US",
  "textLanguage": "en",
  "musicId": "7106594280055130923",
  "musicTitle": "original sound",
  "musicAuthor": "TikTok",
  "musicOriginal": true,
  "musicUrl": "https://www.tiktok.com/music/-7106594280055130923",
  "coverUrl": "https://p16-common-sign.tiktokcdn-eu.com/tos-useast5-p-0068-tx...",
  "authorUsername": "tiktok",
  "authorNickname": "TikTok",
  "authorId": "107955",
  "authorSecUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
  "authorVerified": true,
  "authorFollowers": 96000000,
  "authorFollowing": 1,
  "authorLikes": 464000000,
  "authorVideoCount": 1494,
  "authorProfileUrl": "https://www.tiktok.com/@tiktok",
  "source": "url",
  "sourceValue": null,
  "sourceRank": null,
  "detailed": true,
  "detailError": null,
  "inputUrl": "https://www.tiktok.com/@tiktok/video/7106594312292453675",
  "scrapedAt": "2026-09-29T13:21:23.991Z"
}
```

And the hashtag's own row:

```json
{
  "ok": true,
  "type": "hashtag",
  "hashtag": "bouncingball",
  "relatedHashtag": false,
  "hashtagId": "1315136",
  "url": "https://www.tiktok.com/tag/bouncingball",
  "viewCount": 6278235673,
  "videoCount": 56944,
  "description": null,
  "videosListed": 8,
  "inputUrl": "bouncingball",
  "scrapedAt": "2026-09-24T21:22:28.790Z"
}
```

Inputs that cannot be read (a hashtag that does not exist, a deleted video, a private account, a dead share
link) come back as rows with `"ok": false` and a plain-language `error`. They are never charged.

## Pricing

**$1.00 per 1,000 results**: one charge per video, hashtag, profile or sound row written. Failed inputs,
repeats (a video listed by two hashtags is written once) and videos filtered out by `newerThan` are free.

## Use cases

- **Trend research**: which videos lead a hashtag, and how many views the hashtag has in total. Widen with
  related hashtags to map a niche in one run.
- **Competitor tracking**: schedule a daily run on a list of creators and watch their latest videos' views,
  likes and shares move.
- **Sound research**: which videos use a sound, and how big it is.
- **Enrich a list of video links** with full public stats, for reports, dashboards or influencer vetting.

## FAQ

**Do I need a proxy or cookies?** No. Everything comes from public TikTok pages that load without an account.
The proxy option exists for very large scheduled volumes only.

**How many videos per hashtag or profile?** What TikTok's embed player lists: a hashtag's top 8 videos
(its most viewed, which can be months old), a profile's latest 10, and a sound's top videos. TikTok's own
infinite-scroll feeds need signed requests, which this Actor does not forge, so it does not page further. To
go wide instead of deep, add more hashtags or turn on **Related hashtags to follow**.

**Can it search by keyword?** Not directly: TikTok's search needs a logged-in, signed request. Use hashtags
and related hashtags instead.

**Why is a listed video's date a few seconds before the post time?** With **Full stats** off, the date is
read from the video id, which TikTok stamps just before publishing. With it on, `createTimeISO` is TikTok's
own post time.

**Is it legal?** It reads only public pages, the same ones anyone sees without logging in. You are responsible
for how you use the data, including data protection rules for personal data such as usernames.

## Integrations

Run it from the Apify API or a client library, schedule it in Apify Console, or connect it to n8n, Make,
Zapier or any MCP client through Apify's integrations. Results are available as JSON, CSV, Excel and through
the dataset API.

## Changelog

- **1.0** — Hashtags, profiles, sounds and video links; full stats per video; date filter; related hashtags;
  summary rows; error rows for anything that cannot be read.
