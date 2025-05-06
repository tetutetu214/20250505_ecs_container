import json
from datetime import datetime
import pytz
from fastapi import FastAPI  # Webフレームワーク用
from pydantic import BaseModel  # リクエスト検証用

# FastAPI初期化
app = FastAPI()

# リクエストモデル定義
class EventModel(BaseModel):
    message: str = "Default message from ECS!"
    key: str = ""

# ヘルスチェックエンドポイント
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# 関数定義
@app.post("/invoke")
async def invoke(event: EventModel):

    # 処理内容
    # 東京時間の取得
    tokyo_tz = pytz.timezone('Asia/Tokyo')
    current_time = datetime.now(tokyo_tz).strftime('%Y-%m-%d %H:%M:%S %Z')

    # メッセージ取得    
    Emessage = event.message  # pydanticモデルとして直接アクセス

    #レスポンス
    return {
        'statusCode': 200,
        'body': {
            'greeting': f'Hello from {event.message}!',
            'event': event.dict(),
            'requested_at': datetime.now(tokyo_tz).isoformat(),
            'display_time': current_time,
            'server_type': 'ECS',  # ECSであることを明示
        }
    }

# HTTPサーバ起動
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
