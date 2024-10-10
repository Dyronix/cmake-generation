@echo off
REM Check if the user provided an argument
if "%1"=="" (
    echo No project name provided. Please provide a project name.
    pause
    exit /b
)

REM Get the current working directory
set "CURRENT_DIR=%cd%"

REM Pass the project name (first argument) and current working directory to the Python script
python C:/Scripts/create_project.py %1 "%CURRENT_DIR%"

pause
