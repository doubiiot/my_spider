import urllib.request
import re
import  sys,os
import win32api,win32con,win32gui
import  random
from PIL import Image
import time
pic_folder = "D:/picture_bing/"
#入口函数，判断本日是否下载图片
def run():
    today_folder = pic_folder  + time.strftime("%Y-%m-%d")
    #print(today_folder)
    ran = random.randint(0,6)
    print("正在为您更换第%s张壁纸...\n" % ran)
    if(os.path.exists(today_folder)):
        fin_path = today_folder + '/' + str(ran) + ".bmp"
        setWallpaperFromBMP(fin_path)
    else:
        os.mkdir(today_folder)
        get_bing_backphoto(today_folder,ran)
#爬取bing上图片
def get_bing_backphoto(folder,num):
    m = 0
    if (os.path.exists('D:/picture_bing')== False):
        os.mkdir('D:/picture_bing')        #设置图片下载路径，默认是文件的当前路径
    for i in range(0,6):
        url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx='+str(i)+'&n=1&nc=1361089515117&FORM=HYLH1'
        html = urllib.request.urlopen(url).read()
        if html == 'null':
            print( 'open & read bing error!')
            sys.exit(-1)

        html = html.decode('utf-8')
        html = html.replace('/az/','http://cn.bing.com/az/')
        reg = re.compile('"url":"(.*?)","urlbase"',re.S)
        text = re.findall(reg,html)

        for imgurl in text :
            m += 1
            name = str(i) + ".jpg"
            savepath = folder + '/' +  name
            urllib.request.urlretrieve(imgurl, savepath)
            transferImg(savepath,i)
    fin_path = folder + '/' + str(num) + ".bmp"
    print(fin_path)
    setWallpaperFromBMP(fin_path)

def transferImg(imagePath,num):
    #print(imagePath)
    path = pic_folder + time.strftime("%Y-%m-%d") + '/' + str(num) + '.bmp'
    try:
        Image.open(imagePath).save(path)
        os.remove(imagePath)
    except BaseException as e:
        print(e)
        exit()

def setWallpaperFromBMP(imagepath):
    #print(imagepath)
    try:
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, imagepath, 0)
        print("壁纸更换成功！")
    except BaseException as e:
        print("设置背景失败！", e)
        exit()
if __name__=='__main__':
    run()