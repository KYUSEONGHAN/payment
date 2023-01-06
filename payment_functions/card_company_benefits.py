"""
카드사 혜택 조회하기
- 카드사 혜택 조회 API를 사용하면 카드사별로 제공되는 즉시할인 정보와 무이자 할부 혜택을 한 번에 조회합니다.
"""
from pprint import pprint
from json import loads
import http.client

# 카드사 혜택 조회 API 호출 함수
# 모든 카드사의 즉시할인 정보와 무이자 할부 혜택을 조회하는 카드사 혜택 조회 API를 호출합니다.
"""
discountCards array
카드사의 즉시 할인 정보입니다.

companyCode string
카드사 숫자 코드입니다. 카드사 코드를 참고하세요.

discountAmount number
할인 금액입니다.

balance number
남은 프로모션 예산입니다. 값이 '0'이면 즉시 할인을 적용할 수 없습니다.

discountCode string
즉시 할인 코드(카드사 고유 번호)로 결제할 때 함께 넘겨야 하는 값입니다.

dueDate string
할인 종료일입니다. yyyy-MM-dd 형식입니다. 종료일의 23:59:59까지 행사가 유효합니다.

minimumPaymentAmount number
즉시 할인을 적용할 수 있는 최소 결제 금액입니다.

maximumPaymentAmount number
즉시 할인을 적용할 수 있는 최대 결제 금액입니다.
"""
"""
interestFreeCards array
카드사의 무이자 할부 정보입니다.

companyCode string
카드사 숫자 코드입니다. 카드사 코드를 참고하세요.

dueDate string
무이자 할부 행사 종료일입니다. yyyy-MM-dd 형식입니다. 종료일의 23:59:59까지 행사가 유효합니다.

installmentFreeMonths array
무이자 할부를 적용할 수 있는 개월 수 입니다.

minimumPaymentAmount number
무이자 할부를 적용할 수 있는 최소 결제 금액입니다.
"""
def get_benefits() -> dict:
    conn = http.client.HTTPSConnection("api.tosspayments.com")
    headers = {
        'Authorization': "Basic dGVzdF9za19CRTkyTEFhNVBWYlBwTFlBNlg5ODdZbXBYeUpqOg=="
    }
    conn.request("GET", "/v1/promotions/card", headers=headers)
    res = conn.getresponse()
    data = res.read()

    # string to json
    return loads(data.decode("utf-8"))


if __name__ == '__main__':
    print(pprint(get_benefits()))