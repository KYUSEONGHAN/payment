"""
[일반 카드 결제]
- 결제할 카드 선택 후,
- 결제 금액만큼 바로 결제
"""
from web.restapi import api

from flask import request
from flask_restx import Resource
import logging

log = logging.getLogger(__name__)

Order = api.namespace(
    name='payments/order',
    description='일반 카드 결제 API. (자동 결제 X)',
)

# @Order.route('/')
# class Order(Resource):
#     @api.response(200, "Order Success.")
#     @api.doc('Normal Card Order')
#     def post(self):
#         data = request.json
#         """
#         db 연동되면 사용자, 결제 정도 입력받고 card_payments() 함수로 결제 진행하도록 추후 수정
#         """
#         # card_payments(data)
#         return None, 200

@Order.route('/<int:user_id>')
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
