@echo off
cd /d "%~dp0"

echo Enter student details below:
report_card.exe

echo Now generating report...
py analyze_report.py

echo Opening report in browser...
start report.html

pause
