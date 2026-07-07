import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import sys
import ctypes

# Hide Console Window (Optional)
try:
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
except:
    pass

# Chrome Options
options = Options()
options.add_argument("--window-position=-10000,-10000")  # Off-screen
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--log-level=3")
options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
options.add_experimental_option("useAutomationExtension", False)

# Start Chrome
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# ✅ Open Gmail Inbox
print("Opening Gmail...")
driver.get("https://mail.google.com/mail/u/0/#inbox")
time.sleep(8)  # Wait for page & cookies to load

# ✅ Get all cookies
cookies = driver.get_cookies()

# ✅ Format cookies as "name=value"
result = ""
for cookie in cookies:
    name = cookie.get('name', '')
    value = cookie.get('value', '')
    if name and value:
        result += f"{name}={value}\n"

# ✅ Save to Desktop
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
filepath = os.path.join(desktop, "gmail_cookies.txt")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(result)

print(f"✅ Saved {len(cookies)} cookies to: {filepath}")

driver.quit()
sys.exit()
