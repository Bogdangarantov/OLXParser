from datetime import datetime, timedelta

date = "2022-02-12 09:43:11"
date_2 = "2022-02-11 08:10:53"
print(datetime.strptime(date_2, '%Y-%m-%d %H:%M:%S') - datetime.strptime(date,'%Y-%m-%d %H:%M:%S'))
# await call.message.answer("Желаете ввести ключ слово")