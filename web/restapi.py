import logging

from flask_restx import Api
from web import settings

# from sqlalchemy.orm.exc import NoResultFound

log = logging.getLogger(__name__)

api = Api(
    version='1.0',
    title='GoodAttitude 결제 구현 API.',
    description='GA 유저가 텀블러를 사용하기 위해, 카드를 선 등록 후 -> 대여 기간에 늦거나 반납을 하지 않았을 시, 해당 결제 금액만큼 자동결제(빌링)\n'
                '카드사1: toss payments\n'
                '카드사1: kakaopay (구현 예정)\n'
                '기능 1: 일반 카드 결제\n'
                '기능 2: 카드 선 등록 -> 자동 결제 (빌링)\n'
                '기능 2-1: 대여기간이 늦어질 시, status code: 1\n'
                '기능 2-2: 제품에 하자가 생길 시, status code:2\n'
                '기능 2-3: 반납이 안될 시(대여기간이 늦어진 상태에서 1차 결제를 하고, 그 후에도 반납이 안되면 추가 결제), status code:3\n'
                '기능 3: 결제 취소 (구현 예정)\n'
                '기능 4: 결제 조회 (구현 예정)\n'
                '기능 5: 결제 승인 및 취소 조회 (구현 예정)\n'
                '기능 6: 현금영수증 발급 및 취소 (구현 예정)\n'
                '기능 7: 수동 정산 (구현 예정)\n'
                '기능 8: 카드사 혜택 조회 (구현 예정)\n'
                '기능 9: 세금 처리 (구현 예정)\n',
    terms_url="/",
    contact_email="tyty587587@gmail.com",
    contact="010-7704-1961",
)


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500


# @api.errorhandler(NoResultFound)
# def database_not_found_error_handler(e):
#     """No results found in database"""
#     log.warning(traceback.format_exc())
#     return {'message': 'A database result was required but none was found.'}, 404