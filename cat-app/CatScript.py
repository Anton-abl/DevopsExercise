from flask import Flask, jsonify
import requests
import os

app=Flask("CatApp")

JOKE_API = os.environ.get("JOKE_API")

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "up"}), 200

@app.route('/joke/any', methods=['GET'])
def joke():
    try:
        response = requests.get(JOKE_API, timeout=5)
        response.raise_for_status()
        joke_response = response.json()
        return jsonify({"joke": joke_response.get("joke", f"{joke_response.get('setup', '')} - {joke_response.get('delivery', '')}")}), 200
        joke = response.json().get("joke", "Unable to retrieve a joke")
        return jsonify({"joke": joke}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)      
