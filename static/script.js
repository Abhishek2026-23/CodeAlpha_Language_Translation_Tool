// DOM Elements
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

// State management
let currentAudio = null;

// Event Listeners
document.addEventListener('DOMContentLoaded', function() {
    // Input text change handler
    inputText.addEventListener('input', function() {
        const text = this.value.trim();
        const length = this.value.length;
        
        // Update character counter
        charCounter.textContent = `${length}/5000`;
        
        // Enable/disable translate button
        translateBtn.disabled = !text;
        
        // Clear output when input changes
        if (!text) {
            clearOutput();
        }
    });

    // Translate button click
    translateBtn.addEventListener('click', translateText);

    // Clear button click
    clearBtn.addEventListener('click', clearAll);

    // Swap languages button
    swapBtn.addEventListener('click', swapLanguages);

    // Copy button click
    copyBtn.addEventListener('click', copyToClipboard);

    // Speak button click
    speakBtn.addEventListener('click', speakText);

    // Enter key to translate
    inputText.addEventListener('keydown', function(e) {
        if (e.ctrlKey && e.key === 'Enter') {
            e.preventDefault();
            if (!translateBtn.disabled) {
                translateText();
            }
        }
    });

    // Language change handlers
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

// Translation function
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

    // Show loading state
    showLoading(true);
    hideError();
    hideDetectedLanguage();

    try {
        const response = await fetch('/translate', {
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

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Translation failed');
        }

        // Display translation
        outputText.value = data.translated_text;
        outputText.classList.add('slide-in');

        // Show detected language if auto-detect was used
        if (source === 'auto' && data.detected_language) {
            showDetectedLanguage(data.detected_language);
        }

        // Enable action buttons
        copyBtn.disabled = false;
        speakBtn.disabled = false;

    } catch (error) {
        showError(error.message);
        clearOutput();
    } finally {
        showLoading(false);
    }
}

// Text-to-speech function
async function speakText() {
    const text = outputText.value.trim();
    const lang = targetLang.value;

    if (!text) {
        showError('No text to speak');
        return;
    }

    // Stop current audio if playing
    if (currentAudio) {
        currentAudio.pause();
        currentAudio = null;
    }

    // Show loading state for speech
    speakBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
    speakBtn.disabled = true;

    try {
        // Check if browser supports speech synthesis
        if ('speechSynthesis' in window) {
            // Use browser's built-in text-to-speech
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

        // Fallback to server-side TTS
        const response = await fetch('/text-to-speech', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: text,
                lang: lang
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Text-to-speech failed');
        }

        if (data.use_browser_tts) {
            // Server requested browser TTS
            const utterance = new SpeechSynthesisUtterance(data.text);
            utterance.lang = getVoiceLang(data.lang);
            speechSynthesis.speak(utterance);
        } else if (data.audio_data) {
            // Server provided audio data
            const audioBlob = base64ToBlob(data.audio_data, 'audio/mp3');
            const audioUrl = URL.createObjectURL(audioBlob);
            currentAudio = new Audio(audioUrl);
            
            currentAudio.onended = function() {
                URL.revokeObjectURL(audioUrl);
                currentAudio = null;
            };

            await currentAudio.play();
        }

    } catch (error) {
        showError(error.message);
    } finally {
        // Reset speak button
        speakBtn.innerHTML = '<i class="fas fa-volume-up"></i>';
        speakBtn.disabled = false;
    }
}

// Helper function to convert language codes to speech synthesis format
function getVoiceLang(langCode) {
    const voiceMap = {
        'en': 'en-US',
        'hi': 'hi-IN',
        'fr': 'fr-FR',
        'es': 'es-ES',
        'de': 'de-DE',
        'zh': 'zh-CN',
        'ja': 'ja-JP',
        'ko': 'ko-KR',
        'ar': 'ar-SA',
        'pt': 'pt-BR',
        'ru': 'ru-RU',
        'it': 'it-IT',
        'nl': 'nl-NL',
        'tr': 'tr-TR'
    };
    return voiceMap[langCode] || 'en-US';
}

// Copy to clipboard function
async function copyToClipboard() {
    const text = outputText.value.trim();
    
    if (!text) {
        showError('No text to copy');
        return;
    }

    try {
        await navigator.clipboard.writeText(text);
        
        // Visual feedback
        const originalIcon = copyBtn.innerHTML;
        copyBtn.innerHTML = '<i class="fas fa-check"></i>';
        copyBtn.style.background = '#28a745';
        
        setTimeout(() => {
            copyBtn.innerHTML = originalIcon;
            copyBtn.style.background = '#667eea';
        }, 1500);

    } catch (error) {
        // Fallback for older browsers
        outputText.select();
        document.execCommand('copy');
        showError('Text copied to clipboard');
    }
}

// Swap languages function
function swapLanguages() {
    const sourceValue = sourceLang.value;
    const targetValue = targetLang.value;
    const inputValue = inputText.value.trim();
    const outputValue = outputText.value.trim();

    // Don't swap if source is auto-detect
    if (sourceValue === 'auto') {
        showError('Cannot swap when auto-detect is selected');
        return;
    }

    // Swap language selections
    sourceLang.value = targetValue;
    targetLang.value = sourceValue;

    // Swap text content
    inputText.value = outputValue;
    outputText.value = inputValue;

    // Update UI state
    const hasInputText = inputText.value.trim();
    translateBtn.disabled = !hasInputText;
    copyBtn.disabled = !outputText.value.trim();
    speakBtn.disabled = !outputText.value.trim();

    // Update character counter
    charCounter.textContent = `${inputText.value.length}/5000`;

    // Clear messages
    hideError();
    hideDetectedLanguage();
}

// Clear all function
function clearAll() {
    inputText.value = '';
    clearOutput();
    translateBtn.disabled = true;
    charCounter.textContent = '0/5000';
    hideError();
    hideDetectedLanguage();
    
    // Stop any playing audio
    if (currentAudio) {
        currentAudio.pause();
        currentAudio = null;
    }
}

// Clear output function
function clearOutput() {
    outputText.value = '';
    copyBtn.disabled = true;
    speakBtn.disabled = true;
    outputText.classList.remove('slide-in');
}

// Show loading state
function showLoading(show) {
    if (show) {
        loading.classList.remove('hidden');
        translateBtn.disabled = true;
    } else {
        loading.classList.add('hidden');
        translateBtn.disabled = !inputText.value.trim();
    }
}

// Show error message
function showError(message) {
    errorMessage.textContent = message;
    errorMessage.classList.remove('hidden');
    
    // Auto-hide error after 5 seconds
    setTimeout(() => {
        hideError();
    }, 5000);
}

// Hide error message
function hideError() {
    errorMessage.classList.add('hidden');
}

// Show detected language
function showDetectedLanguage(language) {
    detectedText.textContent = `Detected language: ${language}`;
    detectedLanguage.classList.remove('hidden');
}

// Hide detected language
function hideDetectedLanguage() {
    detectedLanguage.classList.add('hidden');
}

// Utility function to convert base64 to blob
function base64ToBlob(base64, mimeType) {
    const byteCharacters = atob(base64);
    const byteNumbers = new Array(byteCharacters.length);
    
    for (let i = 0; i < byteCharacters.length; i++) {
        byteNumbers[i] = byteCharacters.charCodeAt(i);
    }
    
    const byteArray = new Uint8Array(byteNumbers);
    return new Blob([byteArray], { type: mimeType });
}

// Keyboard shortcuts info
document.addEventListener('keydown', function(e) {
    // Ctrl+K to focus input
    if (e.ctrlKey && e.key === 'k') {
        e.preventDefault();
        inputText.focus();
    }
    
    // Ctrl+L to clear all
    if (e.ctrlKey && e.key === 'l') {
        e.preventDefault();
        clearAll();
    }
    
    // Ctrl+C to copy (when output is focused)
    if (e.ctrlKey && e.key === 'c' && document.activeElement === outputText) {
        e.preventDefault();
        copyToClipboard();
    }
});