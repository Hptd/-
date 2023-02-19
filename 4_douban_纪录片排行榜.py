import requests
import re
import openpyxl


class DoubanJilupianList(object):
    def __init__(self):
        self.url = "https://movie.douban.com/top250"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        }

        self.save_excel_path = "F:/临时文件夹/爬虫教程/"

    def get_my_text(self):
        movie_name_list = []
        for num in range(0, 5):
            page = num*25
            param = {
                "start": page,
                "filter": ""
            }
            resp = requests.get(self.url, headers=self.header, params=param)
            # print(resp.text)
            html_text = resp.text
            resp.close()

            # 这种写法适用于提取一句话内若干个内容；
            re_text_1 = re.compile(r'<li>.*?<div class="item">.*?'
                                   r'<span class="title">(?P<movie_name>.*?)</span>.*?'
                                   r'<span class="playable">(?P<if_play>.*?)</span>.*?'
                                   r'<div class="star">.*?<span>(?P<people_num>.*?)</span>.*?'
                                   r'<span class="inq">(?P<special_text>.*?)</span>', re.S)

            # 适用在分梯队提取关键词，然后二次过滤关键词提取；
            re_text_2 = re.compile(r'<ol class="grid_view">(?P<first_chose>.*?)</ol>', re.S)
            re_text_3 = re.compile(r'<li>.*?<span class="title">(?P<movie_name>.*?)</span>', re.S)

            first_chose_text = re_text_2.finditer(html_text)
            text_1 = None
            for iter_1 in first_chose_text:
                text_1 = iter_1.group("first_chose")

            sec_chose_text = re_text_3.finditer(text_1)
            for iter_2 in sec_chose_text:
                text_2 = iter_2.group("movie_name")
                movie_name_list.append(text_2)

        return movie_name_list

    def print_as_excel(self):
        work_book = openpyxl.Workbook()
        work_book.create_sheet("Sheet1")
        sheet = work_book.active

        name = self.get_my_text()
        i = 0
        for hang in range(1, len(name)+1):
            for lie in "A":
                cell_name = str(lie) + str(hang)
                cell = sheet[cell_name]
                cell.value = name[i]
            i += 1

        work_book.save(self.save_excel_path + "Douban_Movie_Top250_10.xlsx")
        print("Done")


if __name__ == '__main__':
    DoubanJilupianList().print_as_excel()
