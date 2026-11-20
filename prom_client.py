import httpx

def query_prometheus(base_url, promql):
    response = httpx.get(base_url + "/api/v1/query", params={"query": promql}, timeout=5)
    response.raise_for_status()
    return response.json()

def find_down_targets(result):
    down = []
    for item in result["data"]["result"]:
        instance = item["metric"]["instance"]
        value = float(item["value"][1])
        if value == 0:
            down.append(instance)
    return down

if __name__ == "__main__":
    result = query_prometheus("https://demo.promlabs.com", "up")
    print(result)
    print(find_down_targets(result))
    