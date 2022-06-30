from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
youtube_trending_url="https://www.youtube.com/feed/trending"
import pandas as pd
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
  videos=driver.find_elements(By.TAG_NAME,video_divs)
  return videos
#print("Parsing the first video")
#title,url,thumbnail_url,channel,views,uploaded,description


def parse_videos(video):
  title_tag=video.find_element(By.ID,"video-title")
  title=title_tag.text
  url=title_tag.get_attribute('href')
  thumbnail_url=video.find_element(By.TAG_NAME,"img")
  thumbnail_tag=thumbnail_url.get_attribute("src")
  channel_name=video.find_element(By.ID,"container")
  channel=channel_name.text
  views=video.find_element(By.ID,"metadata-line").text
  desc=video.find_element(By.ID,"description-text").text
  
  return{
    "Title:":title,
    "Url:":url,
    "Thumbnail_url:":thumbnail_tag,
    "Channel name:":channel,
    "Views:":views,
    "Description of the video":desc
    }
  
if __name__=="__main__":
  print("Creating driver")
  driver=get_driver()
  print("Fetching the trending videos:")
  videos=get_videos(driver)
  print(f"Found {(len(videos))}videos in trending")
  #print("Parsing the first video")
  #title,url,thumbnail_url,views,uploaded,description
  videos_data=[parse_videos(video) for video in videos[:10]]
  
  videos_df=pd.DataFrame(videos_data)
  print( videos_df)
  videos_df.to_csv("videos_trending.csv",index=None)
  #print(videos_data)
  #print(videos_data[3])
  #print(f"Save to a csv file")
 