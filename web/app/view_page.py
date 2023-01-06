from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)  # flask 객체 인스턴스 생성

# 일반 카드 결제
@app.route('/order_page')
def order():
    return render_template('order.html')

# 자동 결제 (빌링)
@app.route('/auto_order_page')
def auto_order():
    return render_template('auto_order.html')

# 일반 카드 결제
@app.route('/success')
def success():
    paymentKey = request.args.get('paymentKey', "")
    orderId = request.args.get('orderId', "")
    amount = request.args.get('amount', "")

    url = "https://api.tosspayments.com/v1/payments/" + paymentKey
    params = {'orderId': orderId, 'amount': amount}
    headers = {'Authorization': 'Basic dGVzdF9za19CRTkyTEFhNVBWYlBwTFlBNlg5ODdZbXBYeUpqOg==',
               'Content-Type': 'application/json'}
    res = requests.post(url, data=json.dumps(params), headers=headers)

    print('## URL : ', res.request.url)
    print('## 요청헤더 : ', res.request.headers)
    print('## 요청보디 : ', res.request.body)
    print('## 요청결과 : ', res.text)

    return render_template('success.html', result=res.json())

# 자동 결제 (빌링)
# 일반 카드 결제
@app.route('/success2')
def success2():
    print('hohoho')
    customerKey = request.args.get('customerKey') or None
    print(customerKey)
    print('hohoho')

    customerKey = request.args.get('customerKey', "")
    authKey = request.args.get('authKey', "")

    url = "https://api.tosspayments.com/v1/payments/" + customerKey + authKey
    headers = {'Authorization': 'Basic dGVzdF9za19CRTkyTEFhNVBWYlBwTFlBNlg5ODdZbXBYeUpqOg==',
               'Content-Type': 'application/json'}
    res = requests.post(url, headers=headers)

    print('## URL : ', res.request.url)
    print('## 요청헤더 : ', res.request.headers)
    print('## 요청보디 : ', res.request.body)
    print('## 요청결과 : ', res.text)

    return render_template('success.html', result=res.json())