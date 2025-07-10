from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

def generate_signature(params, secret):
    sorted_params = sorted(params.items())
    query_string = ''.join(f"{k}{v}" for k, v in sorted_params)
    sign_string = f"{secret}{query_string}{secret}"
    return hashlib.md5(sign_string.encode('utf-8')).hexdigest().upper()

@app.route('/generate-signature', methods=['GET'])
def sign():
    params = dict(request.args)
    secret = params.pop('secret', None)
    if not secret:
        return jsonify({"error": "Missing 'secret' parameter"}), 400
    sign = generate_signature(params, secret)
    return jsonify({"sign": sign})

@app.route('/')
def home():
    return "AliExpress Signature API is running."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
