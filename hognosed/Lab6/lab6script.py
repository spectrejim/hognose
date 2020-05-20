import requests
import csv
import json

api_key = ''
csv_file_name = 'CSVASL.txt'
URL = ''

headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': "Token " + "779ab9e24b5eb4a36ae09f47e53929dbc85b22a7"
}

with open(csv_file_name) as csv_file:
    with requests.Session() as s:
        cr = csv.reader(csv_file, delimiter=',')
        next(cr, None)

        for row in cr:
            data = {}
            data['Name'] = row[0]
            data['Overlays'] = row[1]
            dataJSON = json.dumps(data)
            req = requests.Request('POST', 'http://ec2-54-89-55-138.compute-1.amazonaws.com/api/Scenario/', data=dataJSON, headers=headers)
            prepared = req.prepare()
            print(prepared.headers)
            '''Send the request'''
            s = requests.Session()
            response = s.send(prepared)

            print(response.status_code)
            print(response.text)
