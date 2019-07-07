from app import app
from flask import jsonify

@app.route('/')
@app.route('/domains', methods=['GET'])
def get_domains():
    return jsonify('test')