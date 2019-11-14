import requests
from bs4 import BeautifulSoup

#计算方法，根据传入的url请求网页并计算返回网页上值的合
def calculate(url):
    headers={
        'Host':'glidedsky.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding':'gzip, deflate',
        'Referer':'http://glidedsky.com/level/crawler-basic-1',
        'Connection':'keep-alive',
        'Cookie':'XSRF-TOKEN=eyJpdiI6Im5ORlZabitEd1d3UHdMdldQT0s3VUE9PSIsInZhbHVlIjoiMDJsNjhCUUR5clhFU25cL2FJQ21MQWpyd2V2a0RDVUh5UURPZGJ2OXNLdmFMZ0N5amVZWVg0Q3FQYkZIN1RhZDMiLCJtYWMiOiI2YTljYmE4OGJlNTQ2YTFlMGI3Yzk4MTNlNmYyMzZlM2JiMmU2NjJhOThiNGVmNDQxMjVlN2MzNjI1ZDk1Yjg4In0%3D; glidedsky_session=eyJpdiI6InBwTFhZbjZLR1BOUk1tbE1wZDBPMnc9PSIsInZhbHVlIjoiMlZsVjNJbVwvWUpIRlJxWHR2YmUzNUUyUitaQ2V2VDNsSTBaVmthdkhxTDhOMnBHK0hMQk5KNjlXd2JPdEh4eUsiLCJtYWMiOiJjZjgxNGI2YmY5YWJkN2Y5NGFiN2ZhY2U3ZWEyNzBmNjZlODE4YTNkYTFjZWJlNGIzMzc4NjliNjMwN2I4OTc1In0%3D; footprints=eyJpdiI6IkNNUWpGQ3FkWFwvQWQ0bU4yRDVlREpBPT0iLCJ2YWx1ZSI6IlhLeE9DZXgwbHRGYmZYa2pmYlE3YTAwY1hzOW1JNEdjY1lKZU04bUZocTkrb3NQNUppbmU3R1wveTRFejJwbU01IiwibWFjIjoiYzg5MDBjYjllZjM5OTA3Y2UwNmM1MmExYjczZmFhYzJhZjYzN2Y5YjVhOTRiNTIzNzczOGI5YWRkYmUyNmE2MiJ9; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1573610190; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1573611039; _ga=GA1.2.157021610.1573610191; _gid=GA1.2.1296302792.1573610191; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IlwvNmJXbTR1K0lENWM2ZGZGdEJBamJnPT0iLCJ2YWx1ZSI6InJkUmE3V2ExXC9JNURpWWZZbElHVXA0aDNxdHcxOFwvR2tMUkpISzdVN1FCRjROOE9iZklcL29Lb3RBY0dmVjNOV0M5K1k4bVp3dTZvb2hiYXVDK0w5YTFFUUpEbW85b3o0UEVsUkN4UHpoSnU1Q2NKYlZCXC9UbkY3cUhqVlg1bW1hXC9wXC96SndtR3NJOVNKN3BYaXFscmhvUzhBMGNwdDNySHZidGJzUUNocFowWT0iLCJtYWMiOiIxMzE5NmE0Y2IzMmI5YmNmZjUwMGYyOGNiYTM5OGIwOTVhMGY4Y2E3MDFlMDg4Y2I5Y2VhOWZjY2Q2YzE0MWQ2In0%3D',
        'Upgrade-Insecure-Requests':'1',
        'Pragma':'no-cache',
        'Cache-Control':'no-cache'
    }
    response=requests.get(url,headers=headers)
    #生成解析器对象
    soup=BeautifulSoup(response.text,'lxml')
    #根据标签的特征获取所有满足特征的标签
    divs=soup.find_all('div',attrs={'class':'col-md-1'})
    #换成列表推导式
    nums=[int(div.text.strip()) for div in divs]
    sum_num=sum(nums)
    return sum_num

#range 方法在不指定第一个参数的情况下是返回从0开始的数字列表，然后后面指定到哪里截至
sum_num=0
for page in range(1,1001):
    url='http://glidedsky.com/level/web/crawler-basic-2?page=%s'%page
    num=calculate(url)
    sum_num+=num
print('1000页的总结果为',sum_num)