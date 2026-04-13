from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from PIL import Image
from io import BytesIO

def setup_driver():
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # uncomment for headless (less detectable but may break scrolling)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver

def take_screenshot(driver, element):
    try:
        screenshot = element.screenshot_as_png
        return screenshot
    except:
        # fallback: full page
        return driver.get_screenshot_as_png()

def scrape_x(driver, query, db_session):
    from database import save_post, Post  # avoid circular import
    
    print(f"Searching for: {query}")
    driver.get("https://x.com/explore")
    time.sleep(4)
    
    search_box = driver.find_element(By.XPATH, '//input[@data-testid="SearchBox_Search_Input"]')
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    scrolls = 0
    
    while scrolls < MAX_SCROLLS:
        # Find tweet articles
        tweets = driver.find_elements(By.XPATH, '//article[@data-testid="tweet"]')
        
        for tweet in tweets:
            try:
                # Extract data
                username_elem = tweet.find_element(By.XPATH, './/span[contains(text(), "@")]')
                username = username_elem.text.strip('@')
                
                full_name = tweet.find_element(By.XPATH, './/div[@data-testid="User-Name"]//span').text
                
                content = tweet.find_element(By.XPATH, './/div[@data-testid="tweetText"]').text if tweet.find_elements(By.XPATH, './/div[@data-testid="tweetText"]') else ""
                
                link_elem = tweet.find_element(By.XPATH, './/a[contains(@href, "/status/")]')
                post_url = "https://x.com" + link_elem.get_attribute('href')
                tweet_id = post_url.split('/status/')[-1]
                
                post_date = tweet.find_element(By.XPATH, './/time').get_attribute('datetime')
                
                # Check if already saved
                existing = db_session.query(Post).filter_by(tweet_id=tweet_id).first()
                if existing:
                    continue
                
                # Take screenshot of the tweet
                screenshot_bytes = take_screenshot(driver, tweet)
                
                tweet_data = {
                    'tweet_id': tweet_id,
                    'username': username,
                    'full_name': full_name,
                    'content': content,
                    'post_url': post_url,
                    'post_date': post_date
                }
                
                save_post(db_session, tweet_data, screenshot_bytes)
                
                # Save screenshot file as backup
                os.makedirs(SCREENSHOT_DIR, exist_ok=True)
                img = Image.open(BytesIO(screenshot_bytes))
                img.save(f"{SCREENSHOT_DIR}/{tweet_id}.png")
                
                print(f"✓ Saved: @{username} - {content[:60]}...")
                
            except Exception as e:
                continue  # skip problematic tweets
        
        # Scroll down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        scrolls += 1