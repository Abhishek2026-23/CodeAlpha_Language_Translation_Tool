@echo off
echo ========================================
echo   CodeAlpha Translation Tool Deployment
echo ========================================
echo.

echo Current Status: Repository is ready!
echo All files committed and prepared for deployment.
echo.

echo NEXT STEPS:
echo.
echo 1. CREATE GITHUB REPOSITORY:
echo    - Go to github.com
echo    - Click "New repository" 
echo    - Name: CodeAlpha_Language_Translation_Tool
echo    - Make it Public
echo    - DON'T initialize with README
echo    - Click "Create repository"
echo.

echo 2. CONNECT AND PUSH:
echo    Replace YOUR_USERNAME with your GitHub username:
echo.
echo    git remote add origin https://github.com/YOUR_USERNAME/CodeAlpha_Language_Translation_Tool.git
echo    git branch -M main  
echo    git push -u origin main
echo.

echo 3. DEPLOY ON VERCEL:
echo    - Go to vercel.com
echo    - Sign up with GitHub
echo    - Click "New Project"
echo    - Import your repository
echo    - Click "Deploy"
echo.

echo Your app will be live at: https://your-project-name.vercel.app
echo.
echo Perfect for your CodeAlpha internship portfolio!
echo.
pause