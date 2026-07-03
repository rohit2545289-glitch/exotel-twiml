@echo off
powershell -windowstyle hidden -command ""
cd /d "%~dp0"

python -c "
import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

print('🍪 Starting Gmail Cookie Grabber...')
print('=' * 40)

options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)

# 🔥 Yeh line Chrome ko minimize karegi
options.add_argument('--start-minimized')

print('📧 Opening Gmail (minimized)...')
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get('https://mail.google.com')
print('⏳ Loading...')
time.sleep(6)

print('🍪 Fetching cookies...')
cookies = driver.get_cookies()

if not cookies:
    print('❌ No cookies found! Login to Gmail.')
    driver.quit()
    exit()

result = '🍪 GMAIL COOKIES (' + str(len(cookies)) + ')\n'
result += '═══════════════════════════\n\n'

for i, cookie in enumerate(cookies, 1):
    name = cookie.get('name', 'unknown')
    value = cookie.get('value', '')[:70]
    domain = cookie.get('domain', 'unknown')
    result += f'{i}. {name}\n'
    result += f'   {value}\n'
    result += f'   Domain: {domain}\n\n'

result += '═══════════════════════════\n'
result += f'✅ Total: {len(cookies)} cookies\n'

print('\n' + result)

try:
    pyperclip.copy(result)
    print('📋 Copied to clipboard!')
except:
    print('⚠️ Could not copy to clipboard.')

with open('gmail_cookies.txt', 'w', encoding='utf-8') as f:
    f.write(result)
print('💾 Cookies saved to gmail_cookies.txt')

driver.quit()
print('✅ Done!')
"

exit
