@echo off
echo Starting screenshot-to-code Local Application...
set REPO_DIR=e:\common folder\screenshot-to-code

if not exist "%REPO_DIR%" (
    echo Error: screenshot-to-code directory not found at %REPO_DIR%
    pause
    exit /b 1
)

echo.
echo Checking backend/.env...
if not exist "%REPO_DIR%\backend\.env" (
    echo [WARNING] backend/.env not found! Please create "%REPO_DIR%\backend\.env" with your OPENAI_API_KEY, ANTHROPIC_API_KEY, or GEMINI_API_KEY.
)

echo.
echo Starting Backend (FastAPI) on port 7001...
start "screenshot-to-code Backend" cmd /k "cd /d %REPO_DIR%\backend && poetry run uvicorn main:app --reload --port 7001"

echo Starting Frontend (Vite) on port 5173...
start "screenshot-to-code Frontend" cmd /k "cd /d %REPO_DIR%\frontend && pnpm dev"

echo.
echo Application launched!
echo Backend: http://localhost:7001
echo Frontend: http://localhost:5173
