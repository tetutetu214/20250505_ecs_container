import json
from datetime import datetime
import pytz

def lambda_handler(event, context):
    # 東京時間の取得
    tokyo_tz = pytz.timezone('Asia/Tokyo')
    current_time = datetime.now(tokyo_tz).strftime('%Y-%m-%d %H:%M:%S %Z')
    
    # メッセージを取得
    message = event.get('message', 'Default message from Lambda!')
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'greeting': f'Hello from {message}!',
            'event': event,
            'requested_at': datetime.now(tokyo_tz).isoformat(),
            'display_time': current_time,
            'request_id': context.aws_request_id 
        })
    }
