"""
수동 정산이 필요한 상점
수동 정산 방식은 카드사에서 지정한 매입 요청 기한을 넘길 수 있다는 리스크가 있지만, 결제가 승인된 후 바로 상품을 제공하지 않는 서비스나 결제 시점과 실제 상품 제공에 시차가 있는 상점에서는 필요한 기능입니다. 승인과 상품 제공 기간 사이에 취소가 일어날 수 있기 때문입니다.

예를 들어 시험 접수를 대행하는 상점에서 결제가 완료된 후 접수 취소가 발생할 수 있습니다. 이 때 접수가 취소된 결제 건을 제외하고 수동 정산을 요청해서 실제로 결제된 접수만 정산받을 수 있습니다.

수동 정산 요청이 가능한 기간은 카드사마다 다르지만 결제 승인 이후 최대 80일 이내에 요청해야 합니다. 기한을 넘기면 정산을 받을 수 없기 때문에 2~3주 단위로 요청하는 것을 권장합니다.
"""
from pprint import pprint
from json import loads
import http.client

# 수동 정산 요청 API 호출 함수
def request_manual_payments() -> dict:
    conn = http.client.HTTPSConnection("api.tosspayments.com")

    payload = "{\"paymentKey\":\"5zJ4xY7m0kODnyRpQWGrN2xqGlNvLrKwv1M9ENjbeoPaZdL6\"}"

    headers = {
        'Authorization': "Basic dGVzdF9za196WExrS0V5cE5BcldtbzUwblgzbG1lYXhZRzVSOg==",
        'Content-Type': "application/json"
    }

    conn.request("POST", "/v1/settlements", payload, headers)

    res = conn.getresponse()
    data = res.read()

    return loads(data.decode("utf-8"))

if __name__ == '__main__':
    print(pprint(request_manual_payments()))