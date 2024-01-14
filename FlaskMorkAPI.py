from flask import Flask, request, jsonify
import json
import random

app = Flask(__name__)

@app.route('/GET',methods=['GET'])
def getPrice():
    dict = {}
    dict['Price'] = 111
    dict['Face'] = 222
    dict['Coupon'] = 333
    return json.dumps(dict)

@app.route('/POST',methods=['POST'])
def getResult():
    Coupon = float(request.args.get('Coupon'))
    j_data = request.json
    app.logger.info(j_data)
    price = j_data['Price']
    face = j_data['Face']
    #Coupon = j_data['Coupon']
    dict={}
    dict['Price'] = price
    dict['Face'] = face
    dict['Result'] = price*face*(1-Coupon)
    return json.dumps(dict)

if __name__ == '__main__':
    app.run(debug=False)
