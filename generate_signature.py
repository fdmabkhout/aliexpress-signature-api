from flask import Flask, request, jsonify
import hashlib
import time

app = Flask(__name__)

@app.route('/generate-signature', methods=['POST'])
def generate_signature():
    data = request.get_json()
    app_key = data.get("app_key")
    secret = data.get("secret")
    timestamp = str(data.get("timestamp"))
    fields = data.get("fields", "")
    category_id = data.get("categoryId")
    page_size = data.get("pageSize", "20")
    sign_method = data.get("sign_method", "md5")

    # Step 1: Create sign string
    param_string = f"app_key{app_key}categoryId{category_id}fields{fields}pageSize{page_size}sign_method{sign_method}timestamp{timestamp}"
    sign_string = f"{secret}{param_string}{secret}"

    # Step 2: MD5 hash
    md5_hash = hashlib.md5(sign_string.encode("utf-8")).hexdigest().upper()

    return jsonify({"sign": md5_hash})
