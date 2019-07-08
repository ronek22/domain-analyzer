from app import app, db
from app.models import Domain
from flask import jsonify, request, url_for
import celery
from retry import retry
import io
import csv
import validators
import whois
import time
import errno
import datetime


@app.route('/domains', methods=["GET", "POST"])
def get_domains():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        f = request.files['file']
        if not f:
            return "No file"

        content = f.stream.read().decode("utf-8")
        list_of_domains = [x.strip() for x in content.split('\n')]
        list_of_domains = [x for x in list_of_domains if validators.domain(x)]

        # START BACKGROUND JOB
        task = loop_through_domains.apply_async([list_of_domains])
        return jsonify({}), 202, {'Location': url_for('taskstatus', task_id=task.id)}

    else:
        db_domains = Domain.query.all()
        db_domains = [x.serialize for x in db_domains]
        response_object['domains'] = db_domains
    return jsonify(response_object)

@app.route('/status/<task_id>')
def taskstatus(task_id):
    task = loop_through_domains.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # something must go wrong
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info)
        }
    return jsonify(response)


@celery.task(bind=True)
def loop_through_domains(self, domains):
    """Background task for checking all domains from the file"""
    total = len(domains)
    for i, domain in enumerate(domains):
        process_domain(domain)
        self.update_state(state="PROGRESS", meta={
            'current': i, 'total': total, 'status': 'Still processing :D'
        })
    return {'current': total, 'total': total, 'status': 'Task completed!', 'result': 'Okey dokey :)'}


def process_domain(domain_name):
    print(domain_name)
    if Domain.query.filter_by(name=domain_name).first() is None:
        try:
            reg_date, exp_date = domain_whois(domain_name)
            db.session.add(Domain(name=domain_name, registration_date=reg_date,
                                  expiration_date=exp_date, checked=True))
            db.session.commit()
        except Exception as err:
            print(f"Something goes wrong with {domain_name}, exactly: {err}")


@retry(OSError, tries=5, delay=2)
def domain_whois(domain_name):
    w = whois.whois(domain_name)
    reg_date = w.creation_date[0] if type(
        w.creation_date) == list else w.creation_date
    exp_date = w.expiration_date[0] if type(
        w.expiration_date) == list else w.expiration_date

    if (type(reg_date) == str and 'before' in reg_date):
        reg_date = datetime.date(1996, 8, 1)
    return reg_date, exp_date


