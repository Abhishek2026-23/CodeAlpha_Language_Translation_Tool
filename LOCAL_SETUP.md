# 🚀 Local Development Setup

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## Step-by-Step Setup

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/CodeAlpha_Language_Translation_Tool.git
cd CodeAlpha_Language_Translation_Tool
```

### 2. Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables (Optional)
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env file and add your Google Translate API key
# GOOGLE_TRANSLATE_API_KEY=your_api_key_here
```

### 5. Run the Application
```bash
python index.py
```

### 6. Access the Application
Open your browser and navigate to: `http://localhost:5000`

## Testing the Application

### Basic Functionality Test
1. Enter "Hello world" in the input field
2. Select "Spanish" as target language
3. Click "Translate"
4. Expected result: "Hola mundo"

### Advanced Features Test
1. Test copy functionality
2. Test text-to-speech
3. Test language swap
4. Test character counter
5. Test error handling (empty input)

## API Key Setup (Optional)

### Google Translate API
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable Cloud Translation API
4. Create credentials (API Key)
5. Add the key to your `.env` file

### Without API Key
The application works perfectly with the enhanced local dictionary containing 100+ translations.

## Troubleshooting

### Common Issues

**Port Already in Use**
```bash
# Kill process on port 5000
# On Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# On macOS/Linux:
lsof -ti:5000 | xargs kill -9
```

**Module Not Found**
```bash
# Ensure virtual environment is activated
pip install -r requirements.txt
```

**API Key Issues**
- Verify API key is correct
- Check if Translation API is enabled
- Ensure billing is set up (Google Cloud)

## Development Tips

### Code Structure
```
CodeAlpha_Language_Translation_Tool/
├── index.py              # Main Flask application
├── requirements.txt      # Python dependencies
├── vercel.json          # Deployment configuration
├── .env.example         # Environment variables template
├── README.md            # Project documentation
└── test_api.html        # API testing page
```

### Making Changes
1. Edit `index.py` for backend changes
2. HTML/CSS/JS is embedded in the Flask app
3. Test locally before deploying
4. Use browser dev tools for debugging

### Adding New Languages
1. Add language code to `LANGUAGE_CODES` dictionary
2. Add translations to local dictionary
3. Update language options in HTML

## Deployment

### Vercel Deployment
```bash
# Install Vercel CLI
npm install -g vercel

# Login and deploy
vercel login
vercel --prod
```

### Environment Variables in Production
- Add `GOOGLE_TRANSLATE_API_KEY` in Vercel dashboard
- Go to Project Settings → Environment Variables

## Performance Optimization

### Local Dictionary
- Contains 100+ common phrases
- Instant response time
- No API rate limits
- Perfect for demo purposes

### Google API
- Professional translations
- Supports all languages
- Requires internet connection
- Has usage limits

## Support

If you encounter any issues:
1. Check the troubleshooting section
2. Verify all dependencies are installed
3. Ensure Python version compatibility
4. Check browser console for errors

## Next Steps

1. ✅ Get the application running locally
2. ✅ Test all features
3. ✅ Set up API key (optional)
4. ✅ Deploy to Vercel
5. ✅ Submit to CodeAlpha

Happy coding! 🎉