from prom_client import find_down_targets

fake = {
    "data": {
        "result": [
            {"metric": {"instance": "a:1"}, "value": [0, "1"]},
            {"metric": {"instance": "b:2"}, "value": [0, "0"]},
        ]
    }
}

print(find_down_targets(fake))