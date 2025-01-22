@echo off

python keywordsReq_main.py


IF %ERRORLEVEL% NEQ 0 (
    echo Program execution failed, checking for errors...

    :: Check if beautifulsoup4 (bs4) module is installed
    python -m pip show beautifulsoup4 >nul 2>nul
    IF %ERRORLEVEL% NEQ 0 (
        echo "beautifulsoup4 (bs4) module is not installed, installing..."
        python -m pip install beautifulsoup4
    )

    :: Check if tkinter module is installed
    python -m pip show tkinter >nul 2>nul
    IF %ERRORLEVEL% NEQ 0 (
        echo "tkinter module is not installed, installing..."
        python -m pip install tk
    )

    :: Check if openpyxl module is installed
    python -m pip show openpyxl >nul 2>nul
    IF %ERRORLEVEL% NEQ 0 (
        echo "openpyxl module is not installed, installing..."
        python -m pip install openpyxl
    )


    :: Check if requests module is installed
    python -m pip show requests >nul 2>nul
    IF %ERRORLEVEL% NEQ 0 (
        echo "requests module is not installed, installing..."
        python -m pip install requests
    )

    :: Code error handling
    echo "There seems to be a code error, please check the Python script and execute again."
) ELSE (
    echo Program execution success!
)

pause
