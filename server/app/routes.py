from app import app
from flask import jsonify, request
import io
import csv

@app.route('/')
@app.route('/domains', methods=["GET", "POST"])
def get_domains():
    if request.method == 'POST':
        f = request.files['file']
        if not f:
            return "No file"
        
        content = f.stream.read().decode("utf-8")
        list_of_domains = content.split('\n')[1:]
        print(list_of_domains)       
        # stream = io.StringIO(f.stream().read().decode("UTF-8"), newline=None)
        # csv_input = csv.reader(stream)
        # print(csv_input)
        # for row in csv_input:
        #     print(row)
    else:
        return jsonify('get test')
    return jsonify('post test')



    