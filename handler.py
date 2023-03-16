import json
import os

confirmation_code = os.environ.get('VK_CONFIRMATION_CODE')


def handler(event, _):
    data = json.loads(event['body'])
    print(data)

    if data['type'] == 'confirmation':
        return {
            'statusCode': 200,
            'body': confirmation_code,
        }
    else:
        print("Новое сообщение")
        return {
            'statusCode': 200,
            'body': '!',
        }
