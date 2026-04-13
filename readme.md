<div align="center">

  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium">
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/ChromeDriver-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white" alt="ChromeDriver">

  <h1>🔍 Tax Joke Scraper</h1>

  <p><strong>An educational Selenium-powered scraper that detects humorous posts on X (Twitter) about dodging taxes on crypto, gambling, reselling, and cash deals — then captures screenshots and stores everything in MySQL.</strong></p>

  <!-- Star & Fork badges -->
  <a href="https://github.com/AdamHanafi/tax-joke-scraper/stargazers">
    <img src="https://img.shields.io/github/stars/AdamHanafi/tax-joke-scraper?style=social&label=Star" alt="GitHub stars">
  </a>
  <a href="https://github.com/AdamHanafi/tax-joke-scraper/fork">
    <img src="https://img.shields.io/github/forks/AdamHanafi/tax-joke-scraper?style=social&label=Fork" alt="GitHub forks">
  </a>
  <a href="https://github.com/AdamHanafi/tax-joke-scraper/issues">
    <img src="https://img.shields.io/github/issues/AdamHanafi/tax-joke-scraper" alt="Issues">
  </a>

  <br><br>

  ![Demo](https://via.placeholder.com/850x420/1e40af/ffffff?text=Tax+Joke+Scraper+in+Action)  
  <!-- Replace the link above with a real screenshot or GIF after you push the project -->

</div>

---

## ✨ Features

- **Targeted scraping** on X (Twitter) for jokes about:
  - Not paying taxes on **crypto** / Bitcoin / Ethereum
  - **Gambling** winnings
  - **Reselling** / flipping items
  - **Cash** transactions / under-the-table deals
- Automatically takes **high-quality screenshots** of matching posts
- Extracts: username, full name, post content, URL, timestamp
- Stores all data + screenshot (as binary) in **MySQL** database
- Built-in anti-detection (ChromeDriver with stealth options)
- Clean, modular code — easy to extend to other platforms

## 🛠️ Tech Stack

- Python 3.10+
- Selenium 4 + WebDriver Manager
- SQLAlchemy + PyMySQL
- ChromeDriver (auto-installed)
- Pillow (for image handling)

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/AdamHanafi/tax-joke-scraper.git
cd tax-joke-scraper

2. Install dependencies
Bashpip install -r requirements.txt
3. Setup MySQL Database
SQLCREATE DATABASE tax_scraper CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
Create a .env file in the project root:
envDB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=tax_scraper
4. Run the scraper
Bashpython main.py
Screenshots are automatically saved in the screenshots/ folder and stored in the database.

📊 What Gets Saved

Tweet ID (unique)
Username & Display Name
Full post content
Direct post URL
Original post date
Full screenshot (PNG stored as BLOB)
Scraping timestamp

⚠️ Important Disclaimer
This project is for educational and research purposes only.
Scraping X (Twitter) violates their Terms of Service and may result in account suspension or IP bans.
Use responsibly and at your own risk. This tool should not be used for harassment, mass reporting, or any illegal activities.
⭐ Support
If you like this project, please give it a star! ⭐
Every star helps it reach more people.


  Made with ❤️ by Adam Hanafi
