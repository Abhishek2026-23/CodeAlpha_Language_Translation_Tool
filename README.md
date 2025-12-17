# CodeAlpha Language Translation Tool

A modern, web-based language translation tool built for the **CodeAlpha AI Internship**. This application allows users to translate text between multiple languages using Google Translate API, with additional features like text-to-speech and copy-to-clipboard functionality.

## 🌟 Features

- **Real-time Translation**: Translate text between 15+ languages instantly
- **Auto Language Detection**: Automatically detect the source language
- **Text-to-Speech**: Listen to translations with natural voice synthesis
- **Copy to Clipboard**: One-click copying of translated text
- **Language Swapping**: Easily swap source and target languages
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI**: Clean, intuitive interface with smooth animations
- **Error Handling**: Comprehensive error handling and user feedback
- **Keyboard Shortcuts**: Efficient navigation with keyboard shortcuts

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Python Flask (Serverless on Vercel)
- **Translation API**: Google Translate API (via deep-translator library)
- **Text-to-Speech**: Browser Web Speech API
- **Styling**: Custom CSS with Glassmorphism design
- **Icons**: Font Awesome
- **Deployment**: Vercel (Serverless Functions)
- **Version Control**: Git & GitHub

## 🔧 Backend API Integration

### Google Translate API Implementation

This project uses the **Google Translate API** through the `deep-translator` Python library for accurate translations:

```python
from deep_translator import GoogleTranslator

# Translation with auto-detection
translator = GoogleTranslator(source='auto', target='es')
result = translator.translate("Hello World")
# Returns: "Hola Mundo"
```

### API Endpoints

**POST /translate**
- Handles translation requests
- Supports 15+ languages
- Auto-detection capability
- Error handling for invalid inputs

**POST /text-to-speech**
- Generates audio for translated text
- Uses browser's Web Speech API for optimal performance
- Fallback to server-side generation if needed

### Backend Architecture

- **Flask Application**: Lightweight Python web framework
- **Serverless Deployment**: Optimized for Vercel's serverless functions
- **Error Handling**: Comprehensive error management
- **CORS Support**: Cross-origin resource sharing enabled
- **JSON API**: RESTful API design with JSON responses

## 🌍 Supported Languages

- English, Hindi, French, Spanish, German
- Chinese, Japanese, Korean, Arabic
- Portuguese, Russian, Italian, Dutch, Turkish
- Auto-detection for source language

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.7 or higher installed
- pip (Python package installer)
- Internet connection (for translation API)

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/CodeAlpha_Language_Translation_Tool.git
cd CodeAlpha_Language_Translation_Tool
```

### 2. Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

### 5. Access the Application
Open your web browser and navigate to:
```
http://localhost:5000
```

## 💻 How to Use

1. **Enter Text**: Type or paste the text you want to translate in the input box
2. **Select Languages**: Choose source language (or use auto-detect) and target language
3. **Translate**: Click the "Translate" button or press Ctrl+Enter
4. **Listen**: Click the speaker icon to hear the translation
5. **Copy**: Click the copy icon to copy translation to clipboard
6. **Swap**: Use the swap button to reverse source and target languages
7. **Clear**: Clear all text and start over

## ⌨️ Keyboard Shortcuts

- `Ctrl + Enter`: Translate text
- `Ctrl + K`: Focus input text area
- `Ctrl + L`: Clear all text
- `Ctrl + C`: Copy translation (when output is focused)

## 📁 Project Structure

```
CodeAlpha_Language_Translation_Tool/
│
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
│
├── templates/
│   └── index.html        # Main HTML template
│
└── static/
    ├── style.css         # CSS styling
    └── script.js         # JavaScript functionality
```

## 🔧 Configuration

The application uses the following default settings:
- **Host**: 0.0.0.0 (accessible from any IP)
- **Port**: 5000
- **Debug Mode**: Enabled (disable for production)
- **Character Limit**: 5000 characters per translation

## 🧪 API Testing & Verification

### Translation API Testing
You can verify the Google Translate API integration by:

1. **Basic Translation Test**:
   - Input: "Hello, how are you?"
   - Source: English (auto-detect)
   - Target: Spanish
   - Expected Output: "Hola, ¿cómo estás?"

2. **Auto-Detection Test**:
   - Input: "Bonjour le monde"
   - Source: Auto Detect
   - Target: English
   - Expected Output: "Hello world" (French detected)

3. **Multiple Language Test**:
   - Test translations between: EN↔ES, EN↔FR, EN↔DE, EN↔HI
   - Verify accuracy and speed of translations

### API Response Format
```json
{
  "translated_text": "Hola Mundo",
  "detected_language": "English",
  "confidence": null
}
```

### Backend API Endpoints
- **POST /translate**: Main translation endpoint
- **POST /text-to-speech**: Audio generation endpoint
- **GET /**: Main application interface

## 🎯 LinkedIn Demo Video Points

When creating your demo video, highlight these key features:

1. **Professional Interface**: Show the clean, modern design
2. **Multi-language Support**: Demonstrate translation between different languages
3. **Auto-detection**: Show how the tool detects languages automatically
4. **Text-to-Speech**: Play audio of translations
5. **Responsive Design**: Show it working on mobile/tablet
6. **Error Handling**: Demonstrate how errors are handled gracefully
7. **User Experience**: Highlight smooth animations and intuitive controls
8. **Real-world Usage**: Translate practical sentences/phrases
9. **API Integration**: Show real-time API calls and responses
10. **Copy Functionality**: Demonstrate the copy-to-clipboard feature

## 🚀 Deployment Options

### Local Development
- Run with `python app.py`
- Access at `http://localhost:5000`

### 🌐 Vercel Deployment (Recommended)
Deploy your app to the cloud in minutes!

1. **Quick Deploy:**
   - Push code to GitHub
   - Import to Vercel
   - Auto-deploy with zero configuration

2. **Live Demo URL:**
   - Your app will be available at: `https://your-project-name.vercel.app`
   - Perfect for LinkedIn demos and portfolio

3. **Detailed Guide:**
   - See [DEPLOYMENT.md](DEPLOYMENT.md) for step-by-step instructions
   - Run `deploy.bat` for automated setup

### Production Deployment (Alternative)
- Use a WSGI server like Gunicorn
- Set `debug=False` in app.py
- Configure environment variables for security
- Use a reverse proxy like Nginx

## 🔒 Security Considerations

- Input validation and sanitization
- Rate limiting for API calls
- HTTPS in production
- Environment variables for sensitive data
- CORS configuration if needed

## 🐛 Troubleshooting

### Common Issues:

1. **Translation not working**: Check internet connection
2. **Audio not playing**: Ensure browser supports audio playback
3. **Slow translations**: May be due to API rate limits
4. **Module not found**: Run `pip install -r requirements.txt`

### Error Messages:
- "Please enter text to translate": Input field is empty
- "Translation failed": API error or network issue
- "Text-to-speech failed": Audio generation error

## 🤝 Contributing

This project was built for the CodeAlpha AI Internship. If you'd like to contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is created for educational purposes as part of the CodeAlpha AI Internship program.

## 👨‍💻 Developer

**Built for CodeAlpha AI Internship**
- Internship Program: CodeAlpha Artificial Intelligence
- Project Type: Language Translation Tool
- Technologies: Python Flask, HTML/CSS/JavaScript, Google Translate API

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section
2. Review the error messages in the browser console
3. Ensure all dependencies are installed correctly
4. Verify internet connection for API access

---

**Note**: This project demonstrates practical AI integration, web development skills, and modern UI/UX design principles suitable for an AI internship portfolio.

## 📸 Screenshots

### Main Interface
![CodeAlpha Language Translation Tool - Main Interface](https://your-vercel-url.vercel.app)

### Translation in Action
![Translation Example](https://your-vercel-url.vercel.app)
*Example: Translating "Hello World" from English to Spanish*

### Mobile Responsive Design
![Mobile View](https://your-vercel-url.vercel.app)
*Fully responsive design works on all devices*

### Features Demonstration
- **Auto Language Detection**: Automatically detects source language
- **Real-time Translation**: Instant translation using Google Translate API
- **Text-to-Speech**: Click speaker icon to hear pronunciation
- **Copy Functionality**: One-click copy to clipboard
- **Language Swapping**: Easy language switching with swap button

**Live Demo**: [https://code-alpha-language-translation-tool.vercel.app](https://code-alpha-language-translation-tool.vercel.app)