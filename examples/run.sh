#!/usr/bin/env bash
# Run the Actor and print the rows as JSON.
curl -X POST "https://api.apify.com/v2/acts/clearfetch~tiktok-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"hashtags": ["minecraft"], "maxVideosPerSource": 5}'
