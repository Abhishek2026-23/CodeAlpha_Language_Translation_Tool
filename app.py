from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator
import os
from gtts import gTTS
import tempfile
import base64

app = Flask(__name__)

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
            detected_lang = GoogleTranslator(source='auto', target='en').detect(text)
            detected_lang_name = LANGUAGES.get(detected_lang, 'Auto-detected')
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
    """Generate audio for translated text"""
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        lang = data.get('lang', 'en')
        
        if not text:
            return jsonify({'error': 'No text provided for speech'}), 400
        
        # Generate speech
        tts = gTTS(text=text, lang=lang, slow=False)
        
        # Save to temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
            tts.save(tmp_file.name)
            
            # Read file and encode to base64
            with open(tmp_file.name, 'rb') as audio_file:
                audio_data = base64.b64encode(audio_file.read()).decode('utf-8')
            
            # Clean up temporary file
            os.unlink(tmp_file.name)
            
        return jsonify({'audio_data': audio_data})
        
    except Exception as e:
        return jsonify({'error': f'Text-to-speech failed: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)