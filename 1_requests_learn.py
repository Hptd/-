import requests


# url 的拼接搜索方式只适应在requests.get()参数
name = input("请输入要搜索的明星：")
url = f"https://sogou.com/web?query={name}"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=header)  # get()的用法只使用在网页最顶端的地址；
print(resp.text)

resp.close()