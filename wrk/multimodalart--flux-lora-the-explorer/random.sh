#!/usr/bin/env bash

curl -X POST https://multimodalart-flux-lora-the-explorer.hf.space/call/get_random_value -s -H "Content-Type: application/json" -d '{
  "data": [
]}' \
  | awk -F'"' '{ print $4}'  \
  | read EVENT_ID; curl -N https://multimodalart-flux-lora-the-explorer.hf.space/call/get_random_value/$EVENT_ID
