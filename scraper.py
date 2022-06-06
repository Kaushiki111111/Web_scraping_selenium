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


if __name__=="__main__":
  print("Creating driver")
  driver=get_driver()
  print("Fetching the page:")
  videos=get_videos(driver)
  print(f"Found {(len(videos))}videos in trending")
  
 
