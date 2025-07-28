#!/bin/bash

SCENARIO=$1

if [[ -z "$SCENARIO" ]]; then
  echo "Usage: $0 <scenario_name.yaml>"
  exit 1
fi

echo "[*] Running scenario: $SCENARIO"
pumba --log-level=info run --json --config "./scenarios/$SCENARIO"
