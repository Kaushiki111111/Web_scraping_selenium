import requests
Youtube_trending_url="https://www.youtube.com/feed/trending"
r=requests.get(Youtube_trending_url)
print('Status_code',r.status_code)
print('if returns 200->successful',r.status_code==200)
#print(r.text[:5000])
with open('trending.html','w')as f:
  f.write(r.text)


