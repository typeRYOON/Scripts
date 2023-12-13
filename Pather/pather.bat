@echo off
py "@@@menu.py"
for /f %%i in ('py "@@@run.py"') do set NEWDIR=%%i
cd /d %NEWDIR%
