import requests

url = "https://movie.douban.com/j/chart/top_list"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

data = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": 30,
    "limit": 1,
}

resp = requests.get(url, headers=header, params=data)  # get():用params;post()：用data.

print(resp.json())
resp.close()