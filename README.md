# Déploiement API Proxy pour ESP32 GSM

## Étapes de déploiement Render

1. Crée un dépôt GitHub avec les fichiers suivants :
- `app.py`
- `requirements.txt`

2. Connecte-toi sur [Render](https://render.com)

3. Crée un nouveau service :
- Type : Web Service
- Langage : Python
- Branch : main
- Build Command : `pip install -r requirements.txt`
- Start Command : `python app.py`
- Free Plan suffisant

4. Render va te donner une URL comme :
   `https://ton-api-proxy.onrender.com`

5. Sur ton ESP32, remplace l’URL cible par :
