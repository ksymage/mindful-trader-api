
# Mindful Trader - 중간 API 서버 (FastAPI)

이 서버는 커스텀 GPT가 실시간 바이낸스 가격 및 거래량 정보를 요청할 수 있도록 중간 API를 제공합니다.

## 🔧 설치 및 실행 방법 (로컬 또는 클라우드)

### 1. 패키지 설치
```bash
pip install -r requirements.txt
```

### 2. 서버 실행
```bash
uvicorn main:app --reload
```

### 3. 기본 사용 예시 (GET 요청)
```bash
GET http://localhost:8000/price?symbol=BTCUSDT&interval=1h&limit=1
```

## ☁️ 무료 배포 플랫폼 추천
- Railway (https://railway.app)
- Render (https://render.com)
- Replit (https://replit.com)

## GPT 함수 연결 예시
GPT 함수 이름: get_price_data
입력 파라미터: symbol, interval, limit
출력값: open, high, low, close, volume
