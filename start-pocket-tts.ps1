$ErrorActionPreference = 'Continue'

Write-Host 'Starting Pocket-TTS' -ForegroundColor Cyan

# Open browser once the server is ready
Start-ThreadJob -ScriptBlock {
    do {
        try {
            Invoke-WebRequest -Uri 'http://localhost:8000' -TimeoutSec 2 -ErrorAction Stop | Out-Null
            break
        } catch {
            Start-Sleep 1
        }
    } while ($true)

    Start-Process 'http://localhost:8000'
} | Out-Null

# Run from the local virtual environment
& "$PSScriptRoot\.venv\Scripts\python.exe" -m pocket_tts.main serve
