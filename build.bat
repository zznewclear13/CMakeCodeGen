@echo off
cd %~dp0
if not exist "%~dp0build" (mkdir "%~dp0build")
cd %~dp0build
cmake --build . --config Release
cd %~dp0
pause