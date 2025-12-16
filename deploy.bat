@echo off
echo ========================================
echo   CodeAlpha Translation Tool Deployment
echo ========================================
echo.

echo Step 1: Initializing Git repository...
git init
git add .
git commit -m "Initial commit: CodeAlpha Language Translation Tool"

echo.
echo Step 2: Ready for GitHub!
echo.
echo Next steps:
echo 1. Create a new repository on GitHub named: CodeAlpha_Language_Translation_Tool
echo 2. Run these commands:
echo.
echo    git remote add origin https://github.com/YOUR_USERNAME/CodeAlpha_Language_Translation_Tool.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo 3. Go to vercel.com and import your GitHub repository
echo 4. Deploy with default settings!
echo.
echo Your app will be live at: https://your-project-name.vercel.app
echo.
pause