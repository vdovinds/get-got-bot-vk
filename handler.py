def handler(event, _):
    print(event)
    return {
        'statusCode': 200,
        'body': '!',
    }