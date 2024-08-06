@echo off
setlocal enabledelayedexpansion

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python and try again.
    exit /b 1
)

:: Check if pip is installed
pip --version >nul 2>&1
if errorlevel 1 (
    echo pip is not installed. Please install pip and try again.
    exit /b 1
)

:: Run dependencies check
python check_requirements.py
if errorlevel 1 (
    pause
    exit
) else (
    if errorlevel 2 (
        pause
        exit
    )
)

echo.
echo.

set "default_resolution=1920x1080"
set "default_scale=1"

set /p resolution="Your screen resolution (default: 1920x1080): "
set /p scale="Your UI scale (default: 1): "

if "!resolution!"=="" set "resolution=%default_resolution%"
if "!scale!"=="" set "scale=%default_scale%"

echo Welcome to Himeverse!
start /B python main.py --resolution %resolution% --scale %scale%
start /B python main.py --resolution %resolution% --scale %scale%
start /B python main.py --resolution %resolution% --scale %scale%
start /B python main.py --resolution %resolution% --scale %scale%
start /B python main.py --resolution %resolution% --scale %scale%
start /B python main.py --resolution %resolution% --scale %scale%
start /B python main.py --resolution %resolution% --scale %scale% --super

endlocal
pause