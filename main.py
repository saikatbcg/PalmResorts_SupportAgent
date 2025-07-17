from flask import Flask, render_template

from flask import Flask, jsonify
from flask_cors import CORS
import jwt
import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    phones = [
        {"name": "iPhone 16 Pro Max", "price": "$1,199", "image": "https://m.media-amazon.com/images/I/81CgtwSII3L._AC_SX679_.jpg"},
        {"name": "Samsung Galaxy S23 Ultra", "price": "$1,099", "image": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s23-ultra-5g-1.jpg"},
        {"name": "OnePlus 12R", "price": "$649", "image": "https://m.media-amazon.com/images/I/71V--WZVUIL._AC_SX679_.jpg"},
        {"name": "OnePlus 14R", "price": "$649", "image": "https://m.media-amazon.com/images/I/71V--WZVUIL._AC_SX679_.jpg"},
        {"name": "iPhone 17 Pro Max", "price": "$2,199", "image": "https://m.media-amazon.com/images/I/81CgtwSII3L._AC_SX679_.jpg"},
    ]
    plans = [
        {"name": "Basic Plan", "details": "$20/month - 5GB data, 100 mins, 100 texts"},
        {"name": "Unlimited Plan", "details": "$49/month - Unlimited data, calls, and texts"},
        {"name": "Family Plan", "details": "$99/month - 4 lines, Unlimited everything"}
    ]
    return render_template('index.html', phones=phones, plans=plans)





# Replace these with your real values
COMPANY_SECRET = 'a2819f9722ccb65c4fc351d871604190e02a2e8a71d7c2a48571e7fedc4057e7'
JWT_ISSUER = 'ccai-auth-service'
JWT_EXPIRY_MINUTES = 10

@app.route('/auth/token')
def get_token():
    payload = {
        "sub": "user-id-2345",  # Unique user ID
        "name": "Alex Doe",
        "email": "john.doe@example.com",
        "iss": JWT_ISSUER,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=JWT_EXPIRY_MINUTES)
    }

    token = jwt.encode(payload, COMPANY_SECRET, algorithm='HS256')
    return jsonify({ "token": token })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
