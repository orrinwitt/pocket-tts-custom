@echo off
start "PowerShell 7 - Pocket TTS" ^
  pwsh ^
  -NoExit -ExecutionPolicy Bypass ^
  -File "%~dp0start-pocket-tts.ps1"
