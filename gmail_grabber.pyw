import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import sys

# Hide console completely
import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# ⏱️ Start Time
start_time = time.time()

print("🍪 Starting Auto Gmail Cookie Grabber...")
print("=" * 40)

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# 🔥 CHROME SCREEN SE BAHAR CHHUP JAYEGA!
options.add_argument("--window-position=-10000,-10000")

print("📧 Opening Gmail (hidden off-screen)...")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://mail.google.com")
print("⏳ Waiting for Gmail to load...")
time.sleep(6)

print("🍪 Fetching cookies...")
cookies = driver.get_cookies()

if not cookies:
    print("❌ No cookies found! Please login to Gmail.")
    time.sleep(3)
    driver.quit()
    sys.exit()

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

# ⏱️ End Time
end_time = time.time()
total_time = round(end_time - start_time, 2)

print("=" * 40)
print(f"⏱️ Total Time Taken: {total_time} seconds")
print("✅ Done!")

# Show notification
try:
    import plyer
    plyer.notification.notify(
        title="✅ Gmail Cookies Grabbed!",
        message=f"Total {len(cookies)} cookies saved!",
        timeout=3
    )
except:
    pass