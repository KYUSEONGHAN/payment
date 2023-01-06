import http.client

conn = http.client.HTTPSConnection("api.tosspayments.com")

# 추후, 디비에 연동되면 사용자, 가격 등의 파라미터를 자동으로 받아와서 결제승인 요청하도록 변경
payload = "{\"customerKey\":\"lpZrPCWTj9htHUHgfneKw\",\"amount\":15000,\"orderId\":\"UGA0woZ4WCihnMpx2TVgx\",\"orderName\":\"토스 티셔츠 외 2건\"}"

headers = {
    'Authorization': "Basic dGVzdF9za19CRTkyTEFhNVBWYlBwTFlBNlg5ODdZbXBYeUpqOg==",
    'Content-Type': "application/json"
    }

biling_key = ''

conn.request("POST", f"/v1/billing/{biling_key}", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))