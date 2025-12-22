from flask import Flask, request, jsonify

app = Flask(__name__)

HTML = '''<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CodeAlpha Translation Tool</title>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Segoe UI',sans-serif;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);min-height:100vh;padding:20px}
.container{max-width:1200px;margin:0 auto;background:rgba(255,255,255,0.1);backdrop-filter:blur(20px);border-radius:20px;padding:30px;box-shadow:0 8px 32px rgba(0,0,0,0.1)}
header{text-align:center;margin-bottom:40px;color:white}
h1{font-size:2.5rem;margin-bottom:10px}
.grid{display:grid;grid-template-columns:1fr auto 1fr;gap:20px;margin-bottom:30px}
.box{background:rgba(255,255,255,0.1);border-radius:15px;padding:20px}
label{display:block;color:white;font-weight:600;margin-bottom:8px}
select{width:100%;padding:12px;border:none;border-radius:10px;background:rgba(255,255,255,0.9);font-size:16px}
textarea{width:100%;height:200px;padding:15px;border:none;border-radius:10px;background:rgba(255,255,255,0.9);font-size:16px;resize:vertical}
.btn{padding:15px 30px;border:none;border-radius:10px;font-size:16px;font-weight:600;cursor:pointer;display:inline-flex;align-items:center;gap:10px}
.btn-primary{background:linear-gradient(45deg,#4ade80,#22c55e);color:white}
.btn-secondary{background:rgba(255,255,255,0.2);color:white}
.controls{display:flex;justify-content:center;gap:20px;margin-bottom:20px}
.hidden{display:none}
.error{background:rgba(239,68,68,0.9);color:white;padding:15px;border-radius:10px;margin:20px 0;text-align:center}
@media(max-width:768px){.grid{grid-template-columns:1fr}}
</style>
</head><body>
<div class="container">
<header><h1><i class="fas fa-language"></i> CodeAlpha Translation Tool</h1>
<p>Translate text between multiple languages</p></header>
<div class="grid">
<div class="box">
<label>From:</label>
<select id="source"><option value="auto">Auto Detect</option><option value="en">English</option><option value="es">Spanish</option><option value="fr">French</option></select>
<textarea id="input" placeholder="Enter text..."></textarea>
</div>
<div style="display:flex;align-items:center"><button class="btn btn-secondary" onclick="swap()"><i class="fas fa-exchange-alt"></i></button></div>
<div class="box">
<label>To:</label>
<select id="target"><option value="es" selected>Spanish</option><option value="en">English</option><option value="fr">French</option></select>
<textarea id="output" placeholder="Translation..." readonly></textarea>
</div>
</div>
<div class="controls">
<button class="btn btn-primary" onclick="translate()"><i class="fas fa-language"></i> Translate</button>
<button class="btn btn-secondary" onclick="clear()"><i class="fas fa-trash"></i> Clear</button>
</div>
<div id="error" class="error hidden"></div>
</div>
<script>
async function translate(){
const text=document.getElementById('input').value.trim();
const target=document.getElementById('target').value;
if(!text)return showError('Enter text');
try{
const res=await fetch('/api/translate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({text,target_lang:target})});
const data=await res.json();
if(!res.ok)throw new Error(data.error);
document.getElementById('output').value=data.translated_text;
}catch(e){showError(e.message)}}
function clear(){document.getElementById('input').value='';document.getElementById('output').value='';hideError()}
function swap(){const s=document.getElementById('source').value;const t=document.getElementById('target').value;if(s!=='auto'){document.getElementById('source').value=t;document.getElementById('target').value=s}}
function showError(msg){const e=document.getElementById('error');e.textContent=msg;e.classList.remove('hidden');setTimeout(hideError,3000)}
function hideError(){document.getElementById('error').classList.add('hidden')}
</script>
</body></html>'''

@app.route('/')
def home():
    return HTML

@app.route('/api/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text', '').strip()
    target = data.get('target_lang', 'es')
    
    if not text:
        return jsonify({'error': 'No text'}), 400
    
    trans = {
        ('hello','es'):'hola',('hello world','es'):'hola mundo',('thank you','es'):'gracias',
        ('hello','fr'):'bonjour',('hello world','fr'):'bonjour le monde',('thank you','fr'):'merci',
        ('hello','en'):'hello',('hola','en'):'hello',('bonjour','en'):'hello'
    }
    
    result = trans.get((text.lower(), target), f'[{target.upper()}] {text}')
    return jsonify({'translated_text': result})
