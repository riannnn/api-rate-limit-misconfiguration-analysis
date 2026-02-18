#!/bin/bash

for i in {1..50}; do
  curl -s -o /dev/null -w "Request $i: %{http_code}\n" \
  "https://example.com/api"
done
