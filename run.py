import time
import json
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

print("🍪 Starting Auto Gmail Cookie Grabber...")
print("=" * 40)

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

print("📧 Opening Chrome with Gmail...")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://mail.google.com")
print("⏳ Waiting for Gmail to load...")
time.sleep(8)

print("🍪 Fetching cookies...")
cookies = driver.get_cookies()

if not cookies:
    print("❌ No cookies found! Please login to Gmail.")
    time.sleep(5)
    driver.quit()
    exit()

result = "🍪 GMAIL COOKIES (" + str(len(cookies)) + ")\n"
result += "═══════════════════════════\n\n"

for i, cookie in enumerate(cookies, 1):
    name = cookie.get("name", "unknown")
    value = cookie.get("value", "")[:70]
    domain = cookie.get("domain", "unknown")
    result += f"{i}. {name}\n"
    result += f"   {value}\n"
    result += f"   Domain: {domain}\n\n"

result += "═══════════════════════════\n"
result += f"✅ Total: {len(cookies)} cookies\n"

print("\n" + result)

try:
    pyperclip.copy(result)
    print("📋 Cookies copied to clipboard!")
except:
    print("⚠️ Could not copy to clipboard. Install: pip install pyperclip")

with open("gmail_cookies.txt", "w", encoding="utf-8") as f:
    f.write(result)
print("💾 Cookies saved to gmail_cookies.txt")

driver.quit()
print("✅ Done!")