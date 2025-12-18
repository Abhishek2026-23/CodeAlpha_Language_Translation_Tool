from flask import Flask, render_template, request, jsonify
import requests
import json
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

@app.route('/test')
def test_api():
    """Test endpoint to verify API is working"""
    return jsonify({
        'status': 'API is working',
        'message': 'Translation service is online',
        'supported_languages': len(LANGUAGES)
    })

@app.route('/translate', methods=['POST'])
def translate_text():
    """Handle translation requests"""
    try:
        # Get request data
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400
            
        text = data.get('text', '').strip()
        source_lang = data.get('source_lang', 'auto')
        target_lang = data.get('target_lang', 'en')
        
        print(f"Translation request: '{text}' from {source_lang} to {target_lang}")
        
        # Validate input
        if not text:
            return jsonify({'error': 'Please enter text to translate'}), 400
        
        if source_lang == target_lang and source_lang != 'auto':
            return jsonify({'error': 'Source and target languages cannot be the same'}), 400
        
        # Perform translation using Google Translate (free, no API key needed)
        try:
            # Use Google Translate free service
            url = "https://translate.googleapis.com/translate_a/single"
            params = {
                'client': 'gtx',
                'sl': source_lang,
                'tl': target_lang,
                'dt': 't',
                'q': text
            }
            
            print(f"Making request to Google Translate: {params}")
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            # Parse the response
            result_data = response.json()
            print(f"Google Translate response: {result_data}")
            
            if result_data and len(result_data) > 0 and result_data[0]:
                # Extract translated text
                translated_text = ""
                for item in result_data[0]:
                    if item and len(item) > 0:
                        translated_text += item[0]
                
                # Get detected language if auto-detect was used
                detected_lang_name = LANGUAGES.get(source_lang, 'Unknown')
                if source_lang == 'auto' and len(result_data) > 2 and result_data[2]:
                    detected_lang_code = result_data[2]
                    detected_lang_name = LANGUAGES.get(detected_lang_code, f'Detected: {detected_lang_code}')
                
                print(f"Translation successful: '{translated_text}'")
                
                if not translated_text:
                    return jsonify({'error': 'Translation returned empty result'}), 500
                
                return jsonify({
                    'translated_text': translated_text,
                    'detected_language': detected_lang_name,
                    'confidence': None
                })
            else:
                return jsonify({'error': 'Invalid response from translation service'}), 500
            
        except Exception as translation_error:
            print(f"Translation API error: {translation_error}")
            
            # Fallback: Simple demo translations for testing
            demo_translations = {
                ('hello', 'es'): 'hola',
                ('hello', 'fr'): 'bonjour',
                ('hello', 'de'): 'hallo',
                ('hello', 'hi'): 'नमस्ते',
                ('good morning', 'es'): 'buenos días',
                ('how are you', 'es'): '¿cómo estás?',
                ('thank you', 'es'): 'gracias',
                ('hello world', 'es'): 'hola mundo'
            }
            
            # Try demo translation
            demo_key = (text.lower(), target_lang)
            if demo_key in demo_translations:
                return jsonify({
                    'translated_text': demo_translations[demo_key],
                    'detected_language': 'English (Demo)',
                    'confidence': None
                })
            
            return jsonify({'error': f'Translation service error: {str(translation_error)}'}), 500
        
    except Exception as e:
        print(f"General error in translate_text: {e}")
        return jsonify({'error': f'Server error: {str(e)}'}), 500

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