@echo off
set SCRIPT_FILE=main.py

REM Activate virtual environment if applicable
REM activate your_virtual_env


pip install -r requirements.txt

REM Run mitmproxy with the script
mitmproxy -s main.py
