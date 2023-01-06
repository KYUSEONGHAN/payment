# payment
## PurPose.
GoodAttitude 플랫폼 결제 시스템 구축

## 실행 방법.
> docker-compose up
* 로컬 환경에서 서버 실행 시
    * 터미널로 루트 디렉토리에서 가상환경 세팅 후, 패키지 설치

### 가상환경 및 패키지 세팅
> (터미널에서) python3 -m pip install --user -U  
> virtualenv env
> (가상 환경 활성화) source env/bin/activate
> (window) .\my_env\Scripts\activate

## Tech Stack.
<img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"><img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white"><img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white"><img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white"><img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white"><img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white"><img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white">

## Functions.
GA 유저가 텀블러를 사용하기 위해, 카드를 선 등록 후 -> 대여 기간에 늦거나 반납을 하지 않았을 시, 해당 결제 금액만큼 자동결제(빌링)
- 기능 1: 일반 카드 결제
- 기능 2: 카드 선 등록 -> 자동 결제 (빌링)
- 기능 2-1: 대여기간이 늦어질 시, status code: 1
- 기능 2-2: 제품에 하자가 생길 시, status code:2
- 기능 2-3: 반납이 안될 시(대여기간이 늦어진 상태에서 1차 결제를 하고, 그 후에도 반납이 안되면 추가 결제), status code:3
- 기능 3: 결제 취소
- 기능 4: 결제 조회
- 기능 5: 결제 승인 및 취소 조회
- 기능 6: 현금영수증 발급 및 취소
- 기능 7: 수동 정산
- 기능 8: 카드사 혜택 조회
- 기능 9: 세금 처리