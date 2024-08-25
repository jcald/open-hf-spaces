#!/usr/bin/env bash

curl -X POST https://multimodalart-flux-lora-the-explorer.hf.space/call/update_selection -s -H "Content-Type: application/json" -d '{
  "data": [
    256,
    256
]}' \
  | awk -F'"' '{ print $4}'  \
  | read EVENT_ID; curl -N https://multimodalart-flux-lora-the-explorer.hf.space/call/update_selection/$EVENT_ID
