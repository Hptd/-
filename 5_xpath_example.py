from lxml import etree
import requests
import time


class XpathGetDoubanImage(object):
    def __init__(self):
        self.url = "https://movie.douban.com/top250"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        }
        self.download_path = "F:/临时文件夹/爬虫教程/image/"

    def get_image_src(self):
        page = 2
        image_src_list = []
        for j in range(page):
            page = 25 * j
            parma = {
                "start": page,
                "filter": ""
            }
            resp = requests.get(self.url, headers=self.header, params=parma)

            main_tree = etree.HTML(resp.text)
            result_list = main_tree.xpath("/html/body/div[3]/div[1]/div/div[1]/ol/li/div/div[1]/a/img/@src")
            for src in result_list:
                image_src_list.append(src)
        return image_src_list

    def get_image(self):
        image_src_list = self.get_image_src()
        i = 1
        for src in image_src_list:
            image_resp = requests.get(src)
            image_name = src.split("/")[-1]
            with open(self.download_path + str(i) + image_name, mode="wb") as f:
                f.write(image_resp.content)
            i += 1

        print("Done.")


if __name__ == '__main__':
    XpathGetDoubanImage().get_image()
