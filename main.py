import asyncio
import os
from vkbottle import Bot
from vkbottle.bot import Message

token = os.environ.get('VK_TOKEN')
bot = Bot(token=token)


@bot.on.message(text="Привет")
async def hi_handler(message: Message):
    users_info = await bot.api.users.get(message.from_id)
    await message.answer("Привет, {}".format(users_info[0].first_name))


# For local testing only
if __name__ == '__main__':
    fake_event = {
            'group_id': 202106649,
            'type': 'message_new',
            'event_id': 'c4c7177262d8d18985929772ecf5c0f8a0a90755',
            'v': '5.131',
            'object': {
                'message': {
                    'date': 1678997508,
                    'from_id': 850905,
                    'id': 821,
                    'out': 0,
                    'attachments': [],
                    'conversation_message_id': 499,
                    'fwd_messages': [],
                    'important': False,
                    'is_hidden': False,
                    'peer_id': 850905,
                    'random_id': 0,
                    'text': 'Привет'
                },
                'client_info': {
                    'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link', 'callback', 'intent_subscribe', 'intent_unsubscribe'],
                    'keyboard': True,
                    'inline_keyboard': True,
                    'carousel': True,
                    'lang_id': 0
                }
            }
        }
    asyncio.run(bot.process_event(fake_event))
