from database import init_db, Session
from scraper import setup_driver, scrape_x
from config import SEARCH_QUERIES, DB_CONFIG
import time

if __name__ == "__main__":
    print("=== X/Twitter Tax Joke Scraper (Educational Demo) ===")
    
    # Setup DB
    init_db()
    session = Session()
    
    driver = setup_driver()
    
    try:
        for query in SEARCH_QUERIES:
            scrape_x(driver, query, session)
            time.sleep(10)  # delay between searches
        
        print("Scraping completed!")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()
        session.close()