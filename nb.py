import requests
from bs4 import BeautifulSoup
Youtube_trending_url="https://www.youtube.com/feed/trending"
#Requests does not execute java script
r=requests.get(Youtube_trending_url)
print('Status_code',r.status_code)
print('if returns 200->successful',r.status_code==200)
#print(r.text[:5000])
with open('trending.html','w')as f:
  f.write(r.text)

doc=BeautifulSoup(r.text,'html.parser')
print('page-title',doc.title)
print('Page Title text',doc.title.text)
#To find video divs:
video_divs=doc.find_all('div',class_=" ytd-video-renderer")
print(f'Found {(len(video_divs))} videos')
   