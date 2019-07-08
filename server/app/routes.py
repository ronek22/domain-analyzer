from app import app, db
from app.models import Domain
from flask import jsonify, request
from retry import retry
import io
import csv
import validators
import whois
import time
import errno

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
        for domain in list_of_domains:
            process_domain(domain)

        print(list_of_domains)       
    else:
        db_domains = Domain.query.all()
        db_domains = [x.serialize for x in db_domains]
        response_object['domains'] = db_domains
    return jsonify(response_object)

def process_domain(domain_name):
    print(domain_name)
    if Domain.query.filter_by(name=domain_name).first() is None:
        try:
            reg_date, exp_date = domain_whois(domain_name)
            db.session.add(Domain(name=domain_name, registration_date=reg_date, expiration_date=exp_date, checked=True))
            db.session.commit()
        except Exception as err:
            print(f"Something goes wrong with {domain_name}, exactly: {err}")

@retry(OSError, tries=5, delay=2)
def domain_whois(domain_name):
    w = whois.whois(domain_name)
    reg_date = w.creation_date[0] if type(w.creation_date) == list else w.creation_date
    exp_date = w.expiration_date[0] if type(w.expiration_date) == list else w.expiration_date
    return reg_date, exp_date

    