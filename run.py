import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

print("🍪 Starting...")
print("=" * 30)

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# ⚡ FAST: 5 second timeout
print("📧 Opening Gmail...")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
driver.set_page_load_timeout(5)

try:
    driver.get("https://mail.google.com")
except:
    pass  # Agar timeout ho toh bhi chalega

# ⚡ FAST: Sirf 3 second wait
print("⏳ Loading...")
time.sleep(3)

# ⚡ FAST: Cookies lo
print("🍪 Fetching cookies...")
cookies = driver.get_cookies()

if not cookies:
    print("❌ No cookies found!")
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

with open("gmail_cookies.txt", "w", encoding="utf-8") as f:
    f.write(result)
print("💾 Cookies saved!")

driver.quit()
print("✅ Done!")
