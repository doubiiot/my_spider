import requests
import lxml
from bs4 import BeautifulSoup
import os
index = 0
headers = {'referer': 'http://jandan.net/', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}
os.mkdir(r'D:\mmpic')
# 保存图片
def save_jpg(res_url):
    global index
    html = BeautifulSoup(requests.get(res_url, headers=headers).text,"lxml")
    for link in html.find_all('a', class_ = "view_img_link"):
        #print(link.get('href'))
        with open("D:\mmpic\{}.jpg".format(index), 'wb') as jpg:
            img_url = "http:" + link.get('href')
            jpg.write(requests.get(img_url).content)
        print("number:%s" % index)
        index += 1

if __name__ == '__main__':
    url = 'http://jandan.net/ooxx'
    print("start")
    for i in range(0, 50):
        save_jpg(url)
        mark_up = requests.get(url, headers=headers).text
        html = BeautifulSoup(mark_up,"lxml")
        url = html.find('a', class_ = "previous-comment-page").get('href')