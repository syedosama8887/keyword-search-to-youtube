from fastapi import APIRouter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

router = APIRouter()
@router.get("/KEY_WORD_FINDER")
async def search_youtube(titile: str):
    return {"result":search_youtube(titile)}

def search_youtube(title):
    # Setup the Chrome driver
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    try:
        # Open YouTube
        driver.get("https://www.youtube.com/")

        # Find the search box and input the keyword
        search_box = driver.find_element("name", "search_query")
        search_box.send_keys(title)
        search_box.submit()

        # Wait for the search results to load
        time.sleep(5)

        # Find the titles of the top 10 videos
        video_titles = driver.find_elements(by='id', value="video-title")
        result = []
        for i, title in enumerate(video_titles[:10], 1):
            result.append(f"{i}. {title.get_attribute('title')}")

    except Exception as e:
        result = f"An error occurred: {e}"

    finally:
        # Close the browser
        driver.quit()

    return result



