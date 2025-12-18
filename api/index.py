from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator
import os
import tempfile
import base64

# For Vercel deployment
app = Flask(__name__, 
           template_folder='../templates',
           static_folder='../static')

# Supported languages with their codes
LANGUAGES = {
    'auto': 'Auto Detect',
    'en': 'English',
    'hi': 'Hindi',
    'fr': 'French',
    'es': 'Spanish',
    'de': 'German',
    'zh': 'Chinese',
    'ja': 'Japanese',
    'ko': 'Korean',
    'ar': 'Arabic',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'it': 'Italian',
    'nl': 'Dutch',
    'tr': 'Turkish'
}

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html', languages=LANGUAGES)

@app.route('/translate', methods=['POST'])
def translate_text():
    """Handle translation requests"""
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        source_lang = data.get('source_lang', 'auto')
        target_lang = data.get('target_lang', 'en')
        
        # Validate input
        if not text:
            return jsonify({'error': 'Please enter text to translate'}), 400
        
        if source_lang == target_lang and source_lang != 'auto':
            return jsonify({'error': 'Source and target languages cannot be the same'}), 400
        
        # Perform translation
        if source_lang == 'auto':
            # Use auto-detect
            translator = GoogleTranslator(source='auto', target=target_lang)
            result = translator.translate(text)
            try:
                detected_lang = GoogleTranslator(source='auto', target='en').detect(text)
                detected_lang_name = LANGUAGES.get(detected_lang, 'Auto-detected')
            except:
                detected_lang_name = 'Auto-detected'
        else:
            # Use specified source language
            translator = GoogleTranslator(source=source_lang, target=target_lang)
            result = translator.translate(text)
            detected_lang_name = LANGUAGES.get(source_lang, 'Unknown')
        
        return jsonify({
            'translated_text': result,
            'detected_language': detected_lang_name,
            'confidence': None
        })
        
    except Exception as e:
        return jsonify({'error': f'Translation failed: {str(e)}'}), 500

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    """Generate audio for translated text - Simplified for serverless"""
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        lang = data.get('lang', 'en')
        
        if not text:
            return jsonify({'error': 'No text provided for speech'}), 400
        
        # For serverless deployment, we'll use browser's built-in speech synthesis
        # Return a success response that triggers client-side TTS
        return jsonify({
            'use_browser_tts': True,
            'text': text,
            'lang': lang,
            'message': 'Using browser text-to-speech'
        })
        
    except Exception as e:
        return jsonify({'error': f'Text-to-speech failed: {str(e)}'}), 500

# Vercel will automatically use this Flask app
# No additional configuration needed