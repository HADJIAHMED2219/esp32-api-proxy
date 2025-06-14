from flask import Flask, request
import requests

app = Flask(__name__)

# Lien Google Apps Script
GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbxRz34bDGikrFP6avcTUl9AMM6HI6JyJT4NbAN_fxWYNgUaHulubl6mIfK4r6nk-Qb9/exec'

@app.route('/sync', methods=['GET'])
def sync():
    try:
        # Récupérer les paramètres GET envoyés par le module GSM
        params = request.args

        # Relayer la requête vers Google Apps Script (HTTPS)
        response = requests.get(GOOGLE_SCRIPT_URL, params=params)

        # Retourner la réponse de Google au module GSM
        return response.text, response.status_code
    except Exception as e:
        return f"Erreur serveur proxy : {str(e)}", 500

@app.route('/')
def home():
    return "Bienvenue sur l'API Proxy ESP32 vers Google Sheets !"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
