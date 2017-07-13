import random
from mongodb import MongoDB

# client = MongoClient(host='localhost', port=27017)

client = MongoDB()

db = client.session.aaron_db

language = ['EN', 'francais', 'vietnamese', 'espanol', '??? ???', '한국어']
country_code = ['US', 'KR', 'JP', 'VT', 'CN', 'FR']
device_carrier = ['SK Telecom', 'KT', 'LGU', 'airtel', 'vodacom', 'orange', 'vivo', 'o2']

s_random = random.SystemRandom()

for i in range(0, 100):
    postback = {
        'language': s_random.choice(language),
        'country_code': s_random.choice(country_code),
        'device_carrier': s_random.choice(device_carrier)
    }
    print(postback)
    postback_result = db.postback.insert_one(postback)
