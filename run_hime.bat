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

echo Welcome to Himeverse!
echo.
goto loop

:loop
	set input=" "
	set /p input=How many Himes do you want?  

	echo %input%|findstr "^[0-9]*$">nul
	if %errorlevel%==0 (
		for /L %%i in (1,1,%input%) do (
			start /B python main.py
		)
		echo as you wish, %input% Hime appeared!
	) else (
		start /B python main.py
		echo you have not enter a number, but Hime appeared!
	)
	goto loop

endlocal
exit