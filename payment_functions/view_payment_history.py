"""
[결제 기록 조회하기]
결제 조회 API를 사용해서 승인·취소된 특정 결제 기록을 다시 확인하거나 해당 결제의 세부 정보를 확인할 수 있습니다.
결제 한 건의 결제 상태, 결제 취소 기록, 매출 전표, 현금영수증 정보 등을 자세히 확인해보세요.
method1: 결제 키로 조회
method2: 주문 id로 조회
"""
from pprint import pprint
from json import loads
import http.client

# 2. 주문 ID로 조회하기
# 주문 ID로 조회하려면 아래와 같이 결제 조회 API 엔드포인트에 Path 파라미터로 orderId를 추가합니다.
# orderId는 상점에서 발급한 주문 ID입니다.
def get_pay_history(orderId) -> dict:
    conn = http.client.HTTPSConnection("api.tosspayments.com")
    headers = {
        'Authorization': "Basic dGVzdF9za19CRTkyTEFhNVBWYlBwTFlBNlg5ODdZbXBYeUpqOg=="
    }

    conn.request("GET", "/v1/payments/orders/kGU24kSobicj3OW2_wZXp", orderId, headers=headers)

    res = conn.getresponse()
    data = res.read()

    return loads(data.decode("utf-8"))

if __name__ == '__main__':
    print(pprint(get_pay_history()))