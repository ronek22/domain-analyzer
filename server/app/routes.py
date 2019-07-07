from app import app, db
from app.models import Domain
from flask import jsonify, request
import io
import csv
import validators

@app.route('/domains', methods=["GET", "POST"])
def get_domains():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        f = request.files['file']
        if not f: return "No file"
        
        content = f.stream.read().decode("utf-8")
        list_of_domains = [x.strip() for x in content.split('\n')]
        list_of_domains = [x for x in list_of_domains if validators.domain(x)]
        
        # TODO: WHOLE PROCESS OF WORKING WITH DOMAINS
        print(list_of_domains)       
    else:
        db_domains = Domain.query.all()
        db_domains = [x.serialize for x in db_domains]
        response_object['domains'] = db_domains
    return jsonify(response_object)


    