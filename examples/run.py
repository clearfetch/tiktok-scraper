"""Run the Actor with the Apify client and print a few fields per row."""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("clearfetch/tiktok-scraper").call(run_input={"hashtags": ["minecraft"], "maxVideosPerSource": 5})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("type"), item.get("webVideoUrl") or item.get("url"), item.get("playCount") or item.get("viewCount"))
