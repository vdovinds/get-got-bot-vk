import asyncio
import json
import os
from main import bot

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
        asyncio.run(bot.process_event(data))
        return {
            'statusCode': 200,
            'body': '!',
        }
