# 🌐 CodeAlpha Language Translation Tool

A modern, feature-rich web-based language translation tool built for the CodeAlpha AI Internship. This application provides real-time translation between multiple languages with a beautiful glassmorphism UI.

![Translation Tool Demo](https://img.shields.io/badge/Status-Live-brightgreen)
![CodeAlpha](https://img.shields.io/badge/CodeAlpha-AI%20Internship-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-red)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)

## 🚀 **Live Demo**

**🔗 [https://codealpha-translator-tool.vercel.app](https://codealpha-translator-tool.vercel.app)**

## ✨ **Features**

### 🎯 **Core Functionality**
- ✅ **Real-time Translation** - Powered by Google Translate API
- ✅ **15+ Languages** - English, Spanish, French, German, Hindi, Chinese, Japanese, and more
- ✅ **Auto Language Detection** - Automatically detects source language
- ✅ **Character Counter** - 5000 character limit with live counting
- ✅ **Input Validation** - Prevents empty submissions and oversized text

### 🎨 **User Interface**
- ✅ **Glassmorphism Design** - Modern blur effects and transparency
- ✅ **Responsive Layout** - Works perfectly on desktop, tablet, and mobile
- ✅ **Smooth Animations** - Loading states and success indicators
- ✅ **Intuitive Controls** - Clear language selectors and action buttons

### 🔧 **Advanced Features**
- ✅ **Copy to Clipboard** - One-click copying of translated text
- ✅ **Text-to-Speech** - Listen to translations in native pronunciation
- ✅ **Language Swap** - Quickly swap source and target languages
- ✅ **Keyboard Shortcuts** - Ctrl+Enter to translate, Ctrl+L to clear
- ✅ **Error Handling** - Graceful fallbacks and user-friendly error messages
- ✅ **API Fallback** - Local dictionary when API is unavailable

## 🛠 **Tech Stack**

### **Backend**
- **Python Flask** - Lightweight web framework
- **Google Translate API** - Professional translation service
- **Requests** - HTTP library for API calls

### **Frontend**
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with glassmorphism effects
- **Vanilla JavaScript** - No frameworks, pure ES6+
- **Font Awesome** - Beautiful icons

### **Deployment**
- **Vercel** - Serverless deployment platform
- **Git** - Version control

## 📋 **Requirements Met**

| CodeAlpha Requirement | Status | Implementation |
|----------------------|--------|----------------|
| Text Input Field | ✅ | 5000 character limit with counter |
| Language Selectors | ✅ | From/To dropdowns with 15+ languages |
| Translate Button | ✅ | With loading states and validation |
| Real Translation API | ✅ | Google Translate API integration |
| Output Display | ✅ | Clear results with success indicators |
| Copy Functionality | ✅ | One-click clipboard copying |
| Text-to-Speech | ✅ | Browser-based speech synthesis |
| Error Handling | ✅ | User-friendly error messages |
| Professional UI | ✅ | Glassmorphism design |
| Mobile Responsive | ✅ | Works on all devices |

## 🚀 **Quick Start**

### **1. Clone Repository**
```bash
git clone https://github.com/yourusername/CodeAlpha_Language_Translation_Tool.git
cd CodeAlpha_Language_Translation_Tool
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Set Up API Key (Optional)**
```bash
# Copy environment template
cp .env.example .env

# Edit .env file and add your Google Translate API key
GOOGLE_TRANSLATE_API_KEY=your_api_key_here
```

### **4. Run Locally**
```bash
python index.py
```

Visit `http://localhost:5000` to see the application.

## 🔑 **API Key Setup**

### **Google Translate API (Recommended)**

1. **Create Google Cloud Project**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select existing one

2. **Enable Translation API**
   - Navigate to "APIs & Services" → "Library"
   - Search for "Cloud Translation API"
   - Click "Enable"

3. **Create API Key**
   - Go to "APIs & Services" → "Credentials"
   - Click "Create Credentials" → "API Key"
   - Copy the generated key

4. **Set Environment Variable**
   ```bash
   export GOOGLE_TRANSLATE_API_KEY=your_api_key_here
   ```

### **Alternative: Local Dictionary Mode**
The application works without an API key using an enhanced local dictionary with 100+ common phrases in multiple languages.

## 🌐 **Deployment**

### **Deploy to Vercel**

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Login and Deploy**
   ```bash
   vercel login
   vercel --prod
   ```

3. **Set Environment Variables**
   - Go to Vercel Dashboard → Your Project → Settings → Environment Variables
   - Add `GOOGLE_TRANSLATE_API_KEY` with your API key

## 📱 **Usage Examples**

### **Basic Translation**
1. Enter text: "Hello, how are you?"
2. Select languages: English → Spanish
3. Click "Translate"
4. Result: "Hola, ¿cómo estás?"

### **Advanced Features**
- **Copy Result**: Click copy icon to save translation
- **Listen**: Click speaker icon for text-to-speech
- **Swap Languages**: Click swap button to reverse translation
- **Auto-detect**: Select "Auto Detect" to identify source language

## 🧪 **API Testing**

### **Sample Request**
```javascript
fetch('/api/translate', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    text: 'Hello world',
    source_lang: 'en',
    target_lang: 'es'
  })
})
```

### **Sample Response**
```json
{
  "success": true,
  "translated_text": "Hola mundo",
  "detected_language": "en",
  "confidence": 0.95,
  "api_used": "Google Translate API"
}
```

## 🎯 **CodeAlpha Internship Compliance**

This project fully satisfies CodeAlpha Task 1 requirements:

- ✅ **Professional UI** with modern design
- ✅ **Real Translation API** integration
- ✅ **Complete Functionality** with all required features
- ✅ **Error Handling** and user validation
- ✅ **Responsive Design** for all devices
- ✅ **Production Ready** with live deployment
- ✅ **Well Documented** with setup instructions
- ✅ **Bonus Features** like TTS and copy functionality

## 🤝 **Contributing**

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 **Developer**

**Your Name**
- 🌐 Portfolio: [your-portfolio.com](https://your-portfolio.com)
- 💼 LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
- 📧 Email: your.email@example.com
- 🐙 GitHub: [@yourusername](https://github.com/yourusername)

## 🏆 **CodeAlpha AI Internship**

This project was developed as part of the CodeAlpha Artificial Intelligence Internship program, demonstrating proficiency in:

- Full-stack web development
- API integration and management
- Modern UI/UX design principles
- Responsive web design
- Error handling and user experience
- Production deployment and DevOps

---

⭐ **Star this repository if you found it helpful!**

🔗 **Live Demo**: [https://codealpha-translator-tool.vercel.app](https://codealpha-translator-tool.vercel.app)