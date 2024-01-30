#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

oracles = {
    "initialization_attested": [ [
            "!KU( ~",
            "#c < #s",
            "priv*inv"
        ],
        [
            "inv"
        ],
        ],
    "verified_msg_is_auth": [ 
        [
            "!KU( ~",
            "#c < #s",
            "priv*inv",
        ],
        [
            "inv"
        ]   
    ],
    "default": [ 
        []
    ]
}
neg_oracles = {
    "initialization_attested": [
        ".",
    ],
    "verified_msg_is_auth": [ 
        ".",
    ],
    "default": [ 
        "!TNIC_Session_fin"
    ]
}

lines = sys.stdin.readlines()
lemma = sys.argv[1]
oracle = oracles[lemma] if lemma in oracles else oracles["default"]
neg_oracle = neg_oracles[lemma] if lemma in neg_oracles else neg_oracles["default"]

results = []
for current in oracle:
    for line in list(lines):
        for guess in current:
            if guess in ' '.join(line.split(":")[1].strip().split()):
                num = line.split(":")[0]
                results.append(num)
                lines.remove(line)
                break
for guess in neg_oracle:
    for line in list(lines):
        if not(guess in ' '.join(line.split(":")[1].strip().split()).split("@")[0]):
            num = line.split(":")[0]
            results.append(num)
            lines.remove(line)
            break

for num in results:
    print(num)