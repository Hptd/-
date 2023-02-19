import requests


url = "https://fanyi.baidu.com/sug"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

input_word = input("请输入你要翻译的词语：")
data = {
    "kw": input_word  # kw >> 关键词
}

# 发送post请求：
resp = requests.post(url, headers=header, data=data)

print(resp.json())
resp.close()
