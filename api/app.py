from flask import Flask, request, jsonify

app = Flask(__name__)

# HTML template embedded
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CodeAlpha Language Translation Tool</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh; padding: 20px;
        }
        .container {
            max-width: 1200px; margin: 0 auto;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px); border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 30px; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }
        header { text-align: center; margin-bottom: 40px; color: white; }
        header h1 { font-size: 2.5rem; margin-bottom: 10px; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); }
        header p { font-size: 1.1rem; opacity: 0.9; }
        .translation-container {
            display: grid; grid-template-columns: 1fr auto 1fr;
            gap: 20px; margin-bottom: 30px; align-items: start;
        }
        .input-section, .output-section {
            background: rgba(255, 255, 255, 0.1); border-radius: 15px;
            padding: 20px; border: 1px solid rgba(255, 255, 255, 0.2);
        }
        .language-selector { margin-bottom: 15px; }
        .language-selector label { display: block; color: white; font-weight: 600; margin-bottom: 8px; }
        .language-selector select {
            width: 100%; padding: 12px; border: none; border-radius: 10px;
            background: rgba(255, 255, 255, 0.9); font-size: 16px; cursor: pointer;
        }
        .text-area-container { position: relative; }
        textarea {
            width: 100%; height: 200px; padding: 15px; border: none;
            border-radius: 10px; background: rgba(255, 255, 255, 0.9);
            font-size: 16px; resize: vertical; font-family: inherit;
        }
        textarea:focus { outline: 2px solid #4ade80; }
        .char-count { position: absolute; bottom: 10px; right: 15px; color: #666; font-size: 12px; }
        .output-actions { position: absolute; bottom: 10px; right: 15px; display: flex; gap: 8px; }
        .action-btn {
            background: #667eea; color: white; border: none; border-radius: 6px;
            padding: 8px; cursor: pointer; font-size: 14px; transition: all 0.3s ease;
        }
        .action-btn:hover:not(:disabled) { background: #5a67d8; transform: translateY(-2px); }
        .action-btn:disabled { opacity: 0.5; cursor: not-allowed; }
        .swap-container { display: flex; align-items: center; justify-content: center; }
        .swap-btn {
            background: rgba(255, 255, 255, 0.2); color: white; border: none;
            border-radius: 50%; width: 50px; height: 50px; cursor: pointer;
            font-size: 18px; transition: all 0.3s ease;
        }
        .swap-btn:hover { background: rgba(255, 255, 255, 0.3); transform: rotate(180deg); }
        .controls { display: flex; justify-content: center; gap: 20px; margin-bottom: 20px; }
        .translate-btn, .clear-btn {
            padding: 15px 30px; border: none; border-radius: 10px;
            font-size: 16px; font-weight: 600; cursor: pointer;
            transition: all 0.3s ease; display: flex; align-items: center; gap: 10px;
        }
        .translate-btn { background: linear-gradient(45deg, #4ade80, #22c55e); color: white; }
        .translate-btn:hover:not(:disabled) { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(74, 222, 128, 0.4); }
        .translate-btn:disabled { opacity: 0.5; cursor: not-allowed; }
        .clear-btn { background: rgba(255, 255, 255, 0.2); color: white; border: 1px solid rgba(255, 255, 255, 0.3); }
        .clear-btn:hover { background: rgba(255, 255, 255, 0.3); }
        .loading { text-align: center; color: white; font-size: 18px; margin: 20px 0; }
        .loading i { margin-right: 10px; }
        .error-message { background: rgba(239, 68, 68, 0.9); color: white; padding: 15px; border-radius: 10px; margin: 20px 0; text-align: center; }
        .hidden { display: none; }
        @media (max-width: 768px) {
            .translation-container { grid-template-columns: 1fr; gap: 15px; }
            .swap-container { order: 2; }
            .swap-btn { transform: rotate(90deg); }
            .controls { flex-direction: column; align-items: center; }
            .translate-btn, .clear-btn { width: 100%; max-width: 300px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1><i class="fas fa-language"></i> CodeAlpha Language Translation Tool</h1>
            <p>Translate text between multiple languages instantly</p>
        </header>
        <main class="translation-container">
            <div class="input-section">
                <div class="language-selector">
                    <label for="source-lang">From:</label>
                    <select id="source-lang">
                        <option value="auto" selected>Auto Detect</option>
                        <option value="en">English</option>
                        <option value="es">Spanish</option>
                        <option value="fr">French</option>
                        <option value="de">German</option>
                        <option value="hi">Hindi</option>
                    </select>
                </div>
                <div class="text-area-container">
                    <textarea id="input-text" placeholder="Enter text to translate..." maxlength="5000"></textarea>
                    <div class="char-count"><span id="char-counter">0/5000</span></div>
                </div>
            </div>
            <div class="swap-container">
                <button id="swap-languages" class="swap-btn" title="Swap languages">
                    <i class="fas fa-exchange-alt"></i>
                </button>
            </div>
            <div class="output-section">
                <div class="language-selector">
                    <label for="target-lang">To:</label>
                    <select id="target-lang">
                        <option value="es" selected>Spanish</option>
                        <option value="en">English</option>
                        <option value="fr">French</option>
                        <option value="de">German</option>
                        <option value="hi">Hindi</option>
                    </select>
                </div>
                <div class="text-area-container">
                    <textarea id="output-text" placeholder="Translation will appear here..." readonly></textarea>
                    <div class="output-actions">
                        <button id="copy-btn" class="action-btn" title="Copy to clipboard" disabled>
                            <i class="fas fa-copy"></i>
                        </button>
                        <button id="speak-btn" class="action-btn" title="Listen to translation" disabled>
                            <i class="fas fa-volume-up"></i>
                        </button>
                    </div>
                </div>
            </div>
        </main>
        <div class="controls">
            <button id="translate-btn" class="translate-btn" disabled>
                <i class="fas fa-language"></i> Translate
            </button>
            <button id="clear-btn" class="clear-btn">
                <i class="fas fa-trash"></i> Clear
            </button>
        </div>
        <div id="loading" class="loading hidden">
            <i class="fas fa-spinner fa-spin"></i> Translating...
        </div>
        <div id="error-message" class="error-message hidden"></div>
    </div>
    <script>
        const inputText = document.getElementById('input-text');
        const outputText = document.getElementById('output-text');
        const sourceLang = document.getElementById('source-lang');
        const targetLang = document.getElementById('target-lang');
        const translateBtn = document.getElementById('translate-btn');
        const clearBtn = document.getElementById('clear-btn');
        const copyBtn = document.getElementById('copy-btn');
        const speakBtn = document.getElementById('speak-btn');
        const loading = document.getElementById('loading');
        const errorMessage = document.getElementById('error-message');
        const charCounter = document.getElementById('char-counter');

        inputText.addEventListener('input', function() {
            const length = this.value.length;
            charCounter.textContent = `${length}/5000`;
            translateBtn.disabled = !this.value.trim();
            if (!this.value.trim()) clearOutput();
        });

        translateBtn.addEventListener('click', translateText);
        clearBtn.addEventListener('click', clearAll);
        copyBtn.addEventListener('click', copyToClipboard);
        speakBtn.addEventListener('click', speakText);

        async function translateText() {
            const text = inputText.value.trim();
            const target = targetLang.value;
            if (!text) return showError('Please enter text to translate');

            showLoading(true);
            hideError();

            try {
                const response = await fetch('/api/translate', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ text: text, target_lang: target })
                });

                const data = await response.json();
                if (!response.ok) throw new Error(data.error || 'Translation failed');

                outputText.value = data.translated_text;
                copyBtn.disabled = false;
                speakBtn.disabled = false;
            } catch (error) {
                showError(error.message);
                clearOutput();
            } finally {
                showLoading(false);
            }
        }

        async function copyToClipboard() {
            const text = outputText.value.trim();
            if (!text) return showError('No text to copy');
            try {
                await navigator.clipboard.writeText(text);
                copyBtn.innerHTML = '<i class="fas fa-check"></i>';
                setTimeout(() => copyBtn.innerHTML = '<i class="fas fa-copy"></i>', 1500);
            } catch (error) {
                showError('Copy failed');
            }
        }

        function speakText() {
            const text = outputText.value.trim();
            if (!text) return showError('No text to speak');
            if ('speechSynthesis' in window) {
                const utterance = new SpeechSynthesisUtterance(text);
                speechSynthesis.speak(utterance);
            }
        }

        function clearAll() {
            inputText.value = '';
            clearOutput();
            translateBtn.disabled = true;
            charCounter.textContent = '0/5000';
            hideError();
        }

        function clearOutput() {
            outputText.value = '';
            copyBtn.disabled = true;
            speakBtn.disabled = true;
        }

        function showLoading(show) {
            loading.classList.toggle('hidden', !show);
            translateBtn.disabled = show || !inputText.value.trim();
        }

        function showError(message) {
            errorMessage.textContent = message;
            errorMessage.classList.remove('hidden');
            setTimeout(hideError, 5000);
        }

        function hideError() {
            errorMessage.classList.add('hidden');
        }
    </script>
</body>
</html>'''

@app.route('/')
def index():
    return HTML_TEMPLATE

@app.route('/api/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        target_lang = data.get('target_lang', 'es')
        
        if not text:
            return jsonify({'error': 'Please enter text to translate'}), 400
        
        # Simple translation dictionary
        translations = {
            ('hello', 'es'): 'hola',
            ('hello world', 'es'): 'hola mundo',
            ('good morning', 'es'): 'buenos días',
            ('thank you', 'es'): 'gracias',
            ('hello', 'fr'): 'bonjour',
            ('hello world', 'fr'): 'bonjour le monde',
            ('thank you', 'fr'): 'merci',
            ('hello', 'de'): 'hallo',
            ('hello world', 'de'): 'hallo welt',
            ('thank you', 'de'): 'danke',
            ('hello', 'hi'): 'नमस्ते',
            ('hello world', 'hi'): 'नमस्ते दुनिया',
            ('thank you', 'hi'): 'धन्यवाद'
        }
        
        key = (text.lower(), target_lang)
        translated_text = translations.get(key, f"[{target_lang.upper()}] {text}")
        
        return jsonify({
            'translated_text': translated_text,
            'detected_language': 'English'
        })
        
    except Exception as e:
        return jsonify({'error': f'Translation failed: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)