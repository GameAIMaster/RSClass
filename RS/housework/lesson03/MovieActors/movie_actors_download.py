# -*- encoding:utf-8 -*-

# 下载某个演员/导演的电影数据集
# 解析XML文本
import lxml.html
import time
# UI自动化测试
from selenium import webdriver
import pandas as pd

etree = lxml.html.etree

"""
这里我们需要使用ChromeDrvier来做模拟
Step1，打开谷歌浏览器， 在地址栏输入 chrome://version/  查看版本信息
Step2，ChromeDriver版本下载地址：http://chromedriver.storage.googleapis.com/index.html
Step3，放到Python\Lib\site-packages相应路径
"""
chrome_driver = r"E:\Programs\Anaconda\envs\py37\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

# 设置想要下载的导演数据集
director = '王宝强'
baseurl = 'https://movie.douban.com/subject_search?search_text='+director+'&cat=1002&start='

movie_actors = {}
# 下载指定页面的数据
def download(request_url):
    driver.get(request_url)
    time.sleep(1)
    html = driver.find_element_by_xpath("//*").get_attribute('outerHTML')
    html = etree.HTML(html)
    #设置电影名称，导演演员的XPATH
    movie_lists = html.xpath(
        "/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']")
    name_lists = html.xpath(
        "/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='meta abstract_2']")
    # 获取返回的数据个数
    num = len(movie_lists)

    if num > 15: #第一页会有16条数据
        # 默认第一个不是，所以去掉
        movie_lists = movie_lists[1:]
        name_lists = name_lists[1:]
    for (movie, name_list) in zip(movie_lists, name_lists):
        # 会存在数据为空的情况
        if name_list.text is None:
            continue
        # 显示下演员名称
        names = name_list.text.split('/')
        movie_actors[movie.text] = name_list.text.replace(' ','')
        # print(name_list.text.replace(' ',''))
    print('OK') # 代表这也数据下载成功
    if num >= 15:
        return True
    else:
        # 没有下一页
        return False

# 开始ID从0，每页增加15
start = 0
while start<10000: #最多抽取10000部电影
    request_url = baseurl + str(start)
    # 下载数据是否有下一页
    flag = download(request_url)
    if flag:
        start = start + 15
    else:
        break

# 将字典转成dataframe
movie_actors = pd.DataFrame(movie_actors, index=[0])
print(movie_actors.head())
# DataFrame行列转换
movie_actors = pd.DataFrame(movie_actors.values.T, index=movie_actors.columns, columns=movie_actors.index)
print('-'*100)
print(movie_actors.head())
movie_actors.index.name = 'title'
movie_actors.set_axis(['actors'], axis='columns', inplace=True)
movie_actors.to_csv('./movie_actors.csv')
