import http.client

"""
API 호출하기
카드 자동 결제 빌링키 발급 요청 API를 호출합니다. authKey, customerKey 값을 요청 본문으로 보냅니다.
"""
def get_keyvalue():
    conn = http.client.HTTPSConnection("api.tosspayments.com")

    payload = "{\"authKey\":\"bln_JJeREObQa\",\"customerKey\":\"aCcQOUMaiwje9pIeN09Vw\"}"

    headers = {
        'Authorization': "Basic dGVzdF9za19CRTkyTEFhNVBWYlBwTFlBNlg5ODdZbXBYeUpqOg==",
        'Content-Type': "application/json"
    }

    conn.request("POST", "/v1/billing/authorizations/issue", payload, headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")

print(get_keyvalue())