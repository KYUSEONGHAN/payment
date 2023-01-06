"""
[현금영수증 발급 및 취소하기]
홈택스 접속 없이 토스페이먼츠에서 제공하는 현금영수증 API로 현금영수증을 편리하게 발급해보세요.
토스페이먼츠에서는 발급 요청된 현금영수증을 모아 국세청에 전달합니다.
토스페이먼츠로 결제하지 않은 건도 발급 및 취소 요청을 할 수 있습니다.
고객이 가상계좌나 계좌이체와 같이 현금성 결제 수단으로 결제했다면,
고객이 현금영수증 발급을 신청하지 않았거나 발행을 원하지 않더라도 현금영수증 발급 의무에 따라 상점에서 현금영수증을 발행해야 합니다.
"""
from pprint import pprint
from json import loads
import http.client

# 현금영수증 발급 함수
def request_receipts() -> dict:
    conn = http.client.HTTPSConnection("api.tosspayments.com")

    payload = "{\"orderId\":\"3iKKcNRi79CWzrtTDhTKn\",\"orderName\":\"토스 티셔츠 외 2건\",\"amount\":\"10000\",\"type\":\"소득공제\",\"customerIdentityNumber\":\"01012345678\"}".encode("utf-8")

    headers = {
        'Authorization': "Basic dGVzdF9za19CRTkyTEFhNVBWYlBwTFlBNlg5ODdZbXBYeUpqOg==",
        'Content-Type': "application/json"
        }

    conn.request("POST", "/v1/cash-receipts", payload, headers)

    res = conn.getresponse()
    data = res.read()

    return loads(data.decode("utf-8"))

if __name__ == '__main__':
    print(pprint(request_receipts()))