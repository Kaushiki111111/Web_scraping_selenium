from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
youtube_trending_url="https://www.youtube.com/feed/trending"

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def get_videos(driver):
  driver.get(youtube_trending_url)
  print("Fetching the divs:")
  video_divs="ytd-video-renderer"
  VIDEO_DIV=driver.find_elements(by=By.TAG_NAME,value=video_divs)
  return VIDEO_DIV
print("Parsing the first video")
#title,url,thumbnail_url,channel,views,uploaded,description


  


if __name__=="__main__":
  print("Creating driver")
  driver=get_driver()
  print("Fetching the page:")
  videos=get_videos(driver)
  print(f"Found {(len(videos))}videos in trending")
  print("Parsing the first video")
  #title,url,thumbnail_url,views,uploaded,description

  video=videos[0]
  title_tag=video.find_element(By.ID,"video-title")
  title=title_tag.text
  url=title_tag.get_attribute('href')
  thumbnail_url=video.find_element(By.TAG_NAME,"img")
  thumbnail_tag=thumbnail_url.get_attribute("src")
  
  print("Title:",title)
  print("Url:",url)
  
  print("Thumbnail_url:",thumbnail_tag)