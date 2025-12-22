# 📡 API Documentation

## Base URL
```
https://codealpha-translator-tool.vercel.app
```

## Endpoints

### 1. **GET /** 
Main application page

**Response:** HTML page with translation interface

---

### 2. **POST /api/translate**
Translate text between languages

#### Request
```json
{
  "text": "Hello world",
  "source_lang": "en",
  "target_lang": "es"
}
```

#### Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `text` | string | Yes | Text to translate (max 5000 chars) |
| `source_lang` | string | No | Source language code (default: "auto") |
| `target_lang` | string | Yes | Target language code |

#### Language Codes
| Code | Language |
|------|----------|
| `auto` | Auto Detect |
| `en` | English |
| `es` | Spanish |
| `fr` | French |
| `de` | German |
| `hi` | Hindi |
| `zh` | Chinese |
| `ja` | Japanese |
| `ko` | Korean |
| `ar` | Arabic |
| `pt` | Portuguese |
| `ru` | Russian |
| `it` | Italian |
| `nl` | Dutch |
| `tr` | Turkish |

#### Success Response
```json
{
  "success": true,
  "translated_text": "Hola mundo",
  "detected_language": "en",
  "confidence": 0.95,
  "api_used": "Google Translate API"
}
```

#### Error Response
```json
{
  "error": "Please enter text to translate"
}
```

#### Status Codes
- `200` - Success
- `400` - Bad Request (empty text, text too long)
- `500` - Internal Server Error

---

### 3. **GET /api/test**
API health check

#### Response
```json
{
  "status": "working",
  "message": "API is live",
  "sample_translation": "hello -> hola"
}
```

---

### 4. **GET /test**
API testing interface

**Response:** HTML page for testing API endpoints

## Usage Examples

### JavaScript (Fetch)
```javascript
async function translateText(text, targetLang) {
  try {
    const response = await fetch('/api/translate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        text: text,
        target_lang: targetLang
      })
    });
    
    const data = await response.json();
    
    if (response.ok) {
      console.log('Translation:', data.translated_text);
      return data;
    } else {
      console.error('Error:', data.error);
    }
  } catch (error) {
    console.error('Network error:', error);
  }
}

// Usage
translateText('Hello world', 'es');
```

### Python (Requests)
```python
import requests

def translate_text(text, target_lang, source_lang='auto'):
    url = 'https://codealpha-translator-tool.vercel.app/api/translate'
    
    payload = {
        'text': text,
        'source_lang': source_lang,
        'target_lang': target_lang
    }
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        return data['translated_text']
    else:
        print(f"Error: {response.json().get('error')}")
        return None

# Usage
result = translate_text('Hello world', 'es')
print(result)  # Output: Hola mundo
```

### cURL
```bash
# Basic translation
curl -X POST https://codealpha-translator-tool.vercel.app/api/translate \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello world",
    "target_lang": "es"
  }'

# With source language specified
curl -X POST https://codealpha-translator-tool.vercel.app/api/translate \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello world",
    "source_lang": "en",
    "target_lang": "fr"
  }'
```

## Rate Limits

### Google Translate API
- Depends on your Google Cloud quota
- Default: 1000 requests per day (free tier)
- Can be increased with billing

### Local Dictionary
- No rate limits
- Instant responses
- 100+ pre-defined translations

## Error Handling

### Common Errors
| Error | Cause | Solution |
|-------|-------|----------|
| "Please enter text to translate" | Empty text field | Provide text input |
| "Text too long. Maximum 5000 characters allowed." | Text exceeds limit | Reduce text length |
| "Translation failed" | API error | Check API key or try again |

### Best Practices
1. Always check response status
2. Handle network errors gracefully
3. Implement retry logic for failed requests
4. Validate input before sending requests
5. Cache translations to reduce API calls

## Authentication

### API Key (Optional)
- Set `GOOGLE_TRANSLATE_API_KEY` environment variable
- No authentication required for local dictionary mode
- API key is server-side only (not exposed to frontend)

## Response Times

### Local Dictionary
- **Average:** < 50ms
- **Use case:** Common phrases and words

### Google Translate API
- **Average:** 200-500ms
- **Use case:** Any text, all languages

## Supported Features

### Translation Features
- ✅ Text translation
- ✅ Language auto-detection
- ✅ Confidence scoring
- ✅ Multiple language support
- ✅ Fallback dictionary

### API Features
- ✅ RESTful design
- ✅ JSON responses
- ✅ Error handling
- ✅ Input validation
- ✅ Health checks

## Testing

### Manual Testing
Visit: `https://codealpha-translator-tool.vercel.app/test`

### Automated Testing
```javascript
// Test basic translation
fetch('/api/translate', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    text: 'hello',
    target_lang: 'es'
  })
})
.then(response => response.json())
.then(data => {
  console.assert(data.translated_text === 'hola', 'Translation failed');
});
```

## Changelog

### v1.0.0
- Initial API release
- Google Translate integration
- Local dictionary fallback
- Error handling
- Input validation