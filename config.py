import os
from dotenv import load_dotenv

load_dotenv()

# MySQL config
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'tax_scraper')
}

# Search queries (you can expand these)
SEARCH_QUERIES = [
    '"not paying taxes" crypto OR bitcoin OR ethereum joke OR funny OR lmao',
    '"tax free" gambling OR casino OR sportsbet',
    '"no taxes on" reselling OR flipping OR ebay OR mercari',
    '"cash only" no taxes OR under the table',
    'joking about dodging taxes on crypto',
    '"irs can suck it" crypto'
]

# Selenium settings
SCROLL_PAUSE_TIME = 3
MAX_SCROLLS = 20
SCREENSHOT_DIR = "screenshots"