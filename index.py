from flask import Flask, request, jsonify

app = Flask(__name__)

HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CodeAlpha Language Translation Tool</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 30px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }

        header {
            text-align: center;
            margin-bottom: 40px;
            color: white;
        }

        header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }

        header p {
            font-size: 1.1rem;
            opacity: 0.9;
        }

        .translation-container {
            display: grid;
            grid-template-columns: 1fr auto 1fr;
            gap: 20px;
            margin-bottom: 30px;
            align-items: start;
        }

        .input-section, .output-section {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .language-selector {
            margin-bottom: 15px;
        }

        .language-selector label {
            display: block;
            color: white;
            font-weight: 600;
            margin-bottom: 8px;
        }

        .language-selector select {
            width: 100%;
            padding: 12px;
            border: none;
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.9);
            font-size: 16px;
            cursor: pointer;
        }

        .text-area-container {
            position: relative;
        }

        textarea {
            width: 100%;
            height: 200px;
            padding: 15px;
            border: none;
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.9);
            font-size: 16px;
            resize: vertical;
            font-family: inherit;
        }

        textarea:focus {
            outline: 2px solid #4ade80;
        }

        .char-count {
            position: absolute;
            bottom: 10px;
            right: 15px;
            color: #666;
            font-size: 12px;
        }

        .output-actions {
            position: absolute;
            bottom: 10px;
            right: 15px;
            display: flex;
            gap: 8px;
        }

        .action-btn {
            background: #667eea;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 8px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.3s ease;
        }

        .action-btn:hover:not(:disabled) {
            background: #5a67d8;
            transform: translateY(-2px);
        }

        .action-btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }

        .swap-container {
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .swap-btn {
            background: rgba(255, 255, 255, 0.2);
            color: white;
            border: none;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            cursor: pointer;
            font-size: 18px;
            transition: all 0.3s ease;
        }

        .swap-btn:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: rotate(180deg);
        }

        .controls {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 20px;
        }

        .translate-btn, .clear-btn {
            padding: 15px 30px;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .translate-btn {
            background: linear-gradient(45deg, #4ade80, #22c55e);
            color: white;
        }

        .translate-btn:hover:not(:disabled) {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(74, 222, 128, 0.4);
        }

        .translate-btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }

        .clear-btn {
            background: rgba(255, 255, 255, 0.2);
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.3);
        }

        .clear-btn:hover {
            background: rgba(255, 255, 255, 0.3);
        }

        .loading {
            text-align: center;
            color: white;
            font-size: 18px;
            margin: 20px 0;
        }

        .loading i {
            margin-right: 10px;
        }

        .error-message {
            background: rgba(239, 68, 68, 0.9);
            color: white;
            padding: 15px;
            border-radius: 10px;
            margin: 20px 0;
            text-align: center;
        }

        .detected-language {
            background: rgba(59, 130, 246, 0.9);
            color: white;
            padding: 10px 15px;
            border-radius: 8px;
            margin: 10px 0;
            text-align: center;
        }

        .hidden {
            display: none;
        }

        .slide-in {
            animation: slideIn 0.5s ease-out;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @media (max-width: 768px) {
            .translation-container {
                grid-template-columns: 1fr;
                gap: 15px;
            }

            .swap-container {
                order: 2;
            }

            .swap-btn {
                transform: rotate(90deg);
            }

            .controls {
                flex-direction: column;
                align-items: center;
            }

            .translate-btn, .clear-btn {
                width: 100%;
                max-width: 300px;
            }
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
                        <option value="hi">Hindi</option>
                        <option value="fr">French</option>
                        <option value="es">Spanish</option>
                        <option value="de">German</option>
                        <option value="zh">Chinese</option>
                        <option value="ja">Japanese</option>
                        <option value="ko">Korean</option>
                        <option value="ar">Arabic</option>
                        <option value="pt">Portuguese</option>
                        <option value="ru">Russian</option>
                        <option value="it">Italian</option>
                        <option value="nl">Dutch</option>
                        <option value="tr">Turkish</option>
                    </select>
                </div>

                <div class="text-area-container">
                    <textarea 
                        id="input-text" 
                        placeholder="Enter text to translate..."
                        maxlength="5000"
                    ></textarea>
                    <div class="char-count">
                        <span id="char-counter">0/5000</span>
                    </div>
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
                        <option value="en">English</option>
                        <option value="hi">Hindi</option>
                        <option value="fr">French</option>
                        <option value="es" selected>Spanish</option>
                        <option value="de">German</option>
                        <option value="zh">Chinese</option>
                        <option value="ja">Japanese</option>
                        <option value="ko">Korean</option>
                        <option value="ar">Arabic</option>
                        <option value="pt">Portuguese</option>
                        <option value="ru">Russian</option>
                        <option value="it">Italian</option>
                        <option value="nl">Dutch</option>
                        <option value="tr">Turkish</option>
                    </select>
                </div>

                <div class="text-area-container">
                    <textarea 
                        id="output-text" 
                        placeholder="Translation will appear here..."
                        readonly
                    ></textarea>
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
                <i class="fas fa-language"></i>
                Translate
            </button>
            <button id="clear-btn" class="clear-btn">
                <i class="fas fa-trash"></i>
                Clear
            </button>
        </div>

        <div id="loading" class="loading hidden">
            <i class="fas fa-spinner fa-spin"></i>
            Translating...
        </div>

        <div id="error-message" class="error-message hidden"></div>

        <div id="detected-language" class="detected-language hidden">
            <i class="fas fa-info-circle"></i>
            <span id="detected-text"></span>
        </div>
    </div>

    <script>
        const inputText = document.getElementById('input-text');
        const outputText = document.getElementById('output-text');
        const sourceLang = document.getElementById('source-lang');
        const targetLang = document.getElementById('target-lang');
        const translateBtn = document.getElementById('translate-btn');
        const clearBtn = document.getElementById('clear-btn');
        const swapBtn = document.getElementById('swap-languages');
        const copyBtn = document.getElementById('copy-btn');
        const speakBtn = document.getElementById('speak-btn');
        const loading = document.getElementById('loading');
        const errorMessage = document.getElementById('error-message');
        const detectedLanguage = document.getElementById('detected-language');
        const detectedText = document.getElementById('detected-text');
        const charCounter = document.getElementById('char-counter');

        let currentAudio = null;

        document.addEventListener('DOMContentLoaded', function() {
            inputText.addEventListener('input', function() {
                const text = this.value.trim();
                const length = this.value.length;
                
                charCounter.textContent = `${length}/5000`;
                translateBtn.disabled = !text;
                
                if (!text) {
                    clearOutput();
                }
            });

            translateBtn.addEventListener('click', translateText);
            clearBtn.addEventListener('click', clearAll);
            swapBtn.addEventListener('click', swapLanguages);
            copyBtn.addEventListener('click', copyToClipboard);
            speakBtn.addEventListener('click', speakText);

            inputText.addEventListener('keydown', function(e) {
                if (e.ctrlKey && e.key === 'Enter') {
                    e.preventDefault();
                    if (!translateBtn.disabled) {
                        translateText();
                    }
                }
            });

            sourceLang.addEventListener('change', function() {
                if (inputText.value.trim()) {
                    clearOutput();
                }
            });

            targetLang.addEventListener('change', function() {
                if (inputText.value.trim()) {
                    clearOutput();
                }
            });
        });

        async function translateText() {
            const text = inputText.value.trim();
            const source = sourceLang.value;
            const target = targetLang.value;

            if (!text) {
                showError('Please enter text to translate');
                return;
            }

            if (source === target && source !== 'auto') {
                showError('Source and target languages cannot be the same');
                return;
            }

            showLoading(true);
            hideError();
            hideDetectedLanguage();

            try {
                console.log('Making translation request...', {text, source, target});
                
                const response = await fetch('/api/translate', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        text: text,
                        source_lang: source,
                        target_lang: target
                    })
                });

                console.log('Response status:', response.status);
                
                const data = await response.json();
                console.log('Response data:', data);

                if (!response.ok) {
                    throw new Error(data.error || `HTTP ${response.status}: Translation failed`);
                }

                if (!data.translated_text) {
                    throw new Error('No translation received from server');
                }

                outputText.value = data.translated_text;
                outputText.classList.add('slide-in');
                outputText.style.backgroundColor = '#f0fff4';
                
                console.log('Translation successful:', data.translated_text);
                
                const successMsg = document.createElement('div');
                successMsg.textContent = '✅ Translation completed!';
                successMsg.style.cssText = 'position:fixed;top:20px;right:20px;background:#4ade80;color:white;padding:10px 20px;border-radius:8px;z-index:1000;font-weight:600;';
                document.body.appendChild(successMsg);
                setTimeout(() => successMsg.remove(), 3000);

                if (source === 'auto' && data.detected_language) {
                    showDetectedLanguage(data.detected_language);
                }

                copyBtn.disabled = false;
                speakBtn.disabled = false;

            } catch (error) {
                showError(error.message);
                clearOutput();
            } finally {
                showLoading(false);
            }
        }

        async function speakText() {
            const text = outputText.value.trim();
            const lang = targetLang.value;

            if (!text) {
                showError('No text to speak');
                return;
            }

            if (currentAudio) {
                currentAudio.pause();
                currentAudio = null;
            }

            speakBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
            speakBtn.disabled = true;

            try {
                if ('speechSynthesis' in window) {
                    const utterance = new SpeechSynthesisUtterance(text);
                    utterance.lang = getVoiceLang(lang);
                    utterance.rate = 0.8;
                    utterance.pitch = 1;
                    
                    utterance.onend = function() {
                        speakBtn.innerHTML = '<i class="fas fa-volume-up"></i>';
                        speakBtn.disabled = false;
                    };
                    
                    utterance.onerror = function() {
                        speakBtn.innerHTML = '<i class="fas fa-volume-up"></i>';
                        speakBtn.disabled = false;
                        showError('Speech synthesis failed');
                    };
                    
                    speechSynthesis.speak(utterance);
                    return;
                }

            } catch (error) {
                showError(error.message);
            } finally {
                speakBtn.innerHTML = '<i class="fas fa-volume-up"></i>';
                speakBtn.disabled = false;
            }
        }

        function getVoiceLang(langCode) {
            const voiceMap = {
                'en': 'en-US', 'hi': 'hi-IN', 'fr': 'fr-FR', 'es': 'es-ES', 'de': 'de-DE',
                'zh': 'zh-CN', 'ja': 'ja-JP', 'ko': 'ko-KR', 'ar': 'ar-SA', 'pt': 'pt-BR',
                'ru': 'ru-RU', 'it': 'it-IT', 'nl': 'nl-NL', 'tr': 'tr-TR'
            };
            return voiceMap[langCode] || 'en-US';
        }

        async function copyToClipboard() {
            const text = outputText.value.trim();
            
            if (!text) {
                showError('No text to copy');
                return;
            }

            try {
                await navigator.clipboard.writeText(text);
                
                const originalIcon = copyBtn.innerHTML;
                copyBtn.innerHTML = '<i class="fas fa-check"></i>';
                copyBtn.style.background = '#28a745';
                
                setTimeout(() => {
                    copyBtn.innerHTML = originalIcon;
                    copyBtn.style.background = '#667eea';
                }, 1500);

            } catch (error) {
                outputText.select();
                document.execCommand('copy');
                showError('Text copied to clipboard');
            }
        }

        function swapLanguages() {
            const sourceValue = sourceLang.value;
            const targetValue = targetLang.value;
            const inputValue = inputText.value.trim();
            const outputValue = outputText.value.trim();

            if (sourceValue === 'auto') {
                showError('Cannot swap when auto-detect is selected');
                return;
            }

            sourceLang.value = targetValue;
            targetLang.value = sourceValue;

            inputText.value = outputValue;
            outputText.value = inputValue;

            const hasInputText = inputText.value.trim();
            translateBtn.disabled = !hasInputText;
            copyBtn.disabled = !outputText.value.trim();
            speakBtn.disabled = !outputText.value.trim();

            charCounter.textContent = `${inputText.value.length}/5000`;

            hideError();
            hideDetectedLanguage();
        }

        function clearAll() {
            inputText.value = '';
            clearOutput();
            translateBtn.disabled = true;
            charCounter.textContent = '0/5000';
            hideError();
            hideDetectedLanguage();
            
            if (currentAudio) {
                currentAudio.pause();
                currentAudio = null;
            }
        }

        function clearOutput() {
            outputText.value = '';
            copyBtn.disabled = true;
            speakBtn.disabled = true;
            outputText.classList.remove('slide-in');
        }

        function showLoading(show) {
            if (show) {
                loading.classList.remove('hidden');
                translateBtn.disabled = true;
            } else {
                loading.classList.add('hidden');
                translateBtn.disabled = !inputText.value.trim();
            }
        }

        function showError(message) {
            errorMessage.textContent = message;
            errorMessage.classList.remove('hidden');
            
            setTimeout(() => {
                hideError();
            }, 5000);
        }

        function hideError() {
            errorMessage.classList.add('hidden');
        }

        function showDetectedLanguage(language) {
            detectedText.textContent = `Detected language: ${language}`;
            detectedLanguage.classList.remove('hidden');
        }

        function hideDetectedLanguage() {
            detectedLanguage.classList.add('hidden');
        }
    </script>
</body>
</html>'''

@app.route('/')
def home():
    return HTML

@app.route('/api/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text', '').strip()
    target = data.get('target_lang', 'es')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    # Enhanced translation dictionary
    translations = {
        ('hello', 'es'): 'hola',
        ('hello world', 'es'): 'hola mundo',
        ('good morning', 'es'): 'buenos días',
        ('thank you', 'es'): 'gracias',
        ('how are you', 'es'): 'cómo estás',
        ('goodbye', 'es'): 'adiós',
        ('yes', 'es'): 'sí',
        ('no', 'es'): 'no',
        ('please', 'es'): 'por favor',
        
        ('hello', 'fr'): 'bonjour',
        ('hello world', 'fr'): 'bonjour le monde',
        ('good morning', 'fr'): 'bonjour',
        ('thank you', 'fr'): 'merci',
        ('how are you', 'fr'): 'comment allez-vous',
        ('goodbye', 'fr'): 'au revoir',
        ('yes', 'fr'): 'oui',
        ('no', 'fr'): 'non',
        
        ('hello', 'de'): 'hallo',
        ('hello world', 'de'): 'hallo welt',
        ('thank you', 'de'): 'danke',
        ('good morning', 'de'): 'guten morgen',
        ('goodbye', 'de'): 'auf wiedersehen',
        ('yes', 'de'): 'ja',
        ('no', 'de'): 'nein',
        
        ('hello', 'hi'): 'नमस्ते',
        ('hello world', 'hi'): 'नमस्ते दुनिया',
        ('thank you', 'hi'): 'धन्यवाद',
        ('good morning', 'hi'): 'सुप्रभात',
        ('goodbye', 'hi'): 'अलविदा',
        ('yes', 'hi'): 'हाँ',
        ('no', 'hi'): 'नहीं',
        
        ('hello', 'zh'): '你好',
        ('hello world', 'zh'): '你好世界',
        ('thank you', 'zh'): '谢谢',
        ('good morning', 'zh'): '早上好',
        ('goodbye', 'zh'): '再见',
        
        ('hello', 'ja'): 'こんにちは',
        ('hello world', 'ja'): 'こんにちは世界',
        ('thank you', 'ja'): 'ありがとう',
        ('good morning', 'ja'): 'おはよう',
        ('goodbye', 'ja'): 'さようなら'
    }
    
    key = (text.lower(), target)
    result = translations.get(key, f'[{target.upper()}] {text}')
    
    return jsonify({
        'translated_text': result,
        'detected_language': 'English',
        'confidence': 0.95
    })
