"""
[자동 결제]
- 결제할 카드 등록 후,
- 1. 대여기간이 늦어질 시,  status code: 1
- 2. 제품에 하자가 생길 시, status code: 2
- 3. 반납이 완될 시(대여기간이 늦어진 상태에서 1차 결제를 하고 그 후에도 반납이 안되면 추가 결제), status code: 3
"""
from web.restapi import api

from flask import request
from flask_restx import Resource

AutoOrder = api.namespace(
    name='payments/auto_order',
    description='자동 결제, 빌링 API. (카드 선 등록 후, 추후 결제), code: (1, 2, 3)',
)

# @AutoOrder.route('/')
# class AutoOrder(Resource):
#     @api.response(200, "Atudo Order Success.")
#     @api.doc('Biling Card Order')
#     def post(self):
#         data = request.json
#         """
#         db 연동되면 사용자, 결제 정도 입력받고 card_payments() 함수로 결제 진행하도록 추후 수정
#         """
#         # card_payments(data)
#         return None, 200

@AutoOrder.route('/<int:user_id>')
class TodoSimple(Resource):
    def get(self, user_id):
        """user 리스트에 item_idx와 일치하는 ID를 가진 목록을 가져옵니다."""
        data = request.json
        return {
            'user_id': user_id,
            'data': data[user_id]
        }

    def put(self, user_id):
        """user 리스트에 user_id와 일치하는 ID를 가진 할 일을 수정합니다."""
        data = request.json
        return {
            'user_id': user_id,
            'data': data[user_id]
        }

    def delete(self, user_id):
        """user 리스트에 user_id와 일치하는 ID를 가진 할 일을 삭제합니다."""
        data = request.json
        del data[user_id]
        return {
            "delete": "success"
        }