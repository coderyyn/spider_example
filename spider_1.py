import requests
from bs4 import BeautifulSoup
url='http://glidedsky.com/level/web/crawler-basic-1'
headers={
    'Host':'glidedsky.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding':'gzip, deflate',
    'Referer':'http://glidedsky.com/level/crawler-basic-1',
    'Connection':'keep-alive',
    'Cookie':'XSRF-TOKEN=eyJpdiI6ImNrWHNhYk5aQzNrdXBiQ0pSY2dNakE9PSIsInZhbHVlIjoiZHRzeGkzZ1wvaUpoOXM2VVVralpzbFB4bXh6OVdIWnNad2txXC9jWFB0ZFA3dDlUY2Vvcis2RnJ3WlFqRUhqOXI3IiwibWFjIjoiNDI1NWYxZGVhMjUxNTZmOTNmZDQ1MmQ4YzYzMDIwYTllNTc5YzI2ZmIyMTMzN2IyZGRlMmRmMGIwYTVkZmU3ZiJ9; glidedsky_session=eyJpdiI6InNJZ1J4WGplOUNXbFlqU29ndzc4WFE9PSIsInZhbHVlIjoiSVdhY3ZQOCt1Z0psVWNDR0dLSzAyaVg3NHdBUndWZTJmUExmekpTOEUrNDhqXC9GVWFvVVhCSEwzR1REbm54WWsiLCJtYWMiOiJhZTQ2OGE1OTVmYTlkODViZGI0NDEyNDNiZmJmOWI3YzE3Y2I3Y2Q5OGY5M2ZlMjY5Y2U4NDU3MWIzODliOGMxIn0%3D; footprints=eyJpdiI6ImpuR2xMRVRualwvS0lhS2NtTTFLOWJBPT0iLCJ2YWx1ZSI6IlwvUEYrWWJnRWRCQ09mS2ZXY2EwZ0FodFFXdUNsTkVSZHRmUWxoZ0xIQXBLSHQwMGpsenZISFVXRkxnandydkZLIiwibWFjIjoiZWRhMzU2NTU0ZmRlNzMxM2ZhOWVmN2VlMzBhODNiNGM2MmMzMWMxYzIyZGFhMjQzMzcyODVmZjFmYTdiZDc4ZCJ9; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1573543327; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1573548587; _ga=GA1.2.1195179388.1573543328; _gid=GA1.2.165778833.1573543328',
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
print(sum_num)