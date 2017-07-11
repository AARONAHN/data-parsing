import pymysql.cursors
from pymongo import MongoClient

mongodb = MongoClient(host='localhost', port=27017)

db = mongodb.aaron_db

mysql = pymysql.connect(
    host='localhost',
    user='root',
    db='aaron_db',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

postback_coll = db.postback.find()
postback_list = list(postback_coll)
print(postback_list)

for postback in postback_list:
    log_id = str(postback.get('_id'))
    language = postback.get('language')
    country_code = postback.get('country_code')
    device_carrier = postback.get('device_carrier')

    with mysql.cursor() as cursor:
        sql = "INSERT INTO `postback` (`log_id`, `language`, `country_code`, `device_carrier`) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (log_id, language, country_code, device_carrier))

mysql.commit()



# with connection.cursor() as cursor:
#     sql = "SELECT `id`, `log_id`, `language`, `country_code`, `device_carrier` FROM `postback`"
#     cursor.execute(sql)
#     result = cursor.fetchone()
#     print(result)

