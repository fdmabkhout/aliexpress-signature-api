from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/generate-signature', methods=['POST'])
def generate_signature():
    data = request.json
    secret = data.get('secret')
    params = data.get('params', {})

    if not secret or not params:
        return jsonify({'error': 'Missing secret or params'}), 400

    sorted_keys = sorted(params.keys())
    base_string = secret + ''.join(f'{k}{params[k]}' for k in sorted_keys) + secret

    md5_hash = hashlib.md5(base_string.encode('utf-8')).hexdigest().upper()

    return jsonify({'sign': md5_hash})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)