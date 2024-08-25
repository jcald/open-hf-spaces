#!/usr/bin/env bash

curl -X POST https://multimodalart-flux-lora-the-explorer.hf.space/call/run_lora -s -H "Content-Type: application/json" -d '{
  "data": [
    "Hello!!",
    1,
    1,
    true,
    0,
    256,
    256,
    0
]}' \
  | awk -F'"' '{ print $4}'  \
  | read EVENT_ID; curl -N https://multimodalart-flux-lora-the-explorer.hf.space/call/run_lora/$EVENT_ID
