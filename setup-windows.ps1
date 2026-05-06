# Pocket TTS — Windows Setup Script
# Run this once to install everything, then use start-pocket-tts.bat to launch

$ErrorActionPreference = 'Stop'

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Pocket TTS — Windows Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# --- Check Python ---
Write-Host "Checking for Python..." -ForegroundColor Yellow
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    $pythonCmd = Get-Command python3 -ErrorAction SilentlyContinue
}
if (-not $pythonCmd) {
    Write-Host "ERROR: Python is not installed or not in PATH." -ForegroundColor Red
    Write-Host "Please install Python 3.10+ from https://python.org/downloads/" -ForegroundColor Red
    Write-Host "Make sure to check 'Add Python to PATH' during installation." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

$pyVersion = & $pythonCmd.Source --version 2>$1
Write-Host "Found: $pyVersion" -ForegroundColor Green

# --- Create virtual environment ---
$venvPath = Join-Path $PSScriptRoot ".venv"
if (Test-Path $venvPath) {
    Write-Host "Virtual environment already exists at .venv\ — skipping creation." -ForegroundColor Green
} else {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    & $pythonCmd.Source -m venv $venvPath
    Write-Host "Virtual environment created." -ForegroundColor Green
}

# --- Install package ---
Write-Host "Installing Pocket TTS and dependencies..." -ForegroundColor Yellow
$pipPath = Join-Path $venvPath "Scripts\pip.exe"
& $pipPath install --upgrade pip | Out-Null
& $pipPath install -e $PSScriptRoot
Write-Host "Installation complete." -ForegroundColor Green

# --- Create desktop shortcut ---
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$env:USERPROFILE\Desktop\Pocket TTS.lnk")
$Shortcut.TargetPath = Join-Path $PSScriptRoot "start-pocket-tts.bat"
$Shortcut.WorkingDirectory = $PSScriptRoot
$Shortcut.IconLocation = Join-Path $PSScriptRoot "pocket_tts\static\favicon.ico"
$Shortcut.Save()
Write-Host "Desktop shortcut created." -ForegroundColor Green

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Setup complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "To start Pocket TTS:" -ForegroundColor White
Write-Host "  • Double-click start-pocket-tts.bat" -ForegroundColor White
Write-Host "  • Or use the 'Pocket TTS' shortcut on your desktop" -ForegroundColor White
Write-Host ""
Read-Host "Press Enter to exit"
