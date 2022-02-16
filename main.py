# OUR FILES IMPORT
import logging
from bot_info import *
from defs import Defs
from admins import *
from State_m import *
from keyboards_info import *
# Libraries import
import json
from datetime import datetime, timedelta
from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.utils.markdown import hlink
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import urllib
bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands="start")
async def ComandStart(message: types.Message):
    await bot.delete_message(message.chat.id, message.message_id)

    login = False
    print(f"{datetime.now()}  log--> START  {message.from_user.id}")
    with open("users_info.json") as f:
        users = json.load(f)
    for i in range(len(users['users-active'])):
        if str(users['users-active'][i]['id']) == str(message.from_user.id):
            login = True
            break

    if str(message.from_user.id) in admin_ids:
        await message.answer('Добро пожаловать Администратор☺️', reply_markup=Defs().admin_keyb_main_menu())
        await States.admin.set()
    else:
        if login:
            await message.answer('Вас приветствует бот ОЛХ', reply_markup=Defs().main_menu())
        else:
            users['users-active'].append({"id": message.from_user.id,
                                          "username": message.from_user.username,
                                          "category": "",
                                          "subcategory": "",
                                          "keyword": "",
                                          "filters":[],
                                          "blacklist_of_words":[],
                                          "date": "0 days 0 hours"
                                          })
            with open("users_info.json", 'w') as f:
                json.dump(users, f, indent=3)
            await message.answer('вы успешно зарегестрированы', reply_markup=Defs().main_menu())
        # await States.enter_code.set()
        await States.normal_permission.set()

# Admin Panel
@dp.callback_query_handler(state=States.admin)
async def MainMenu(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    await state.finish()
    print(f"{datetime.now()}  log--> ADMIN  {call.from_user.id}")

    if callback == 'settings':
        await call.message.answer('Выберите категорию для парсинга', reply_markup=Defs().keyb_categories())
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await States.settings.set()
    elif callback == 'parse':
        await call.message.answer('Считывание данных началось...')
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await States.parse.set()
        # TODO
    elif callback == 'Make_code':
        await call.message.answer('Выберите врямя работы токена', reply_markup=Defs().make_code_keyb())
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await States.make_code.set()
    elif callback == 'add_token':
        await call.message.answer('Ожидание файла с токенами')
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await States.add_token_file.set()
    elif callback == 'filter':
        await call.message.answer('Фильтры',reply_markup=Defs().filters())
        await States.filters.set()
    else:
        await call.message.answer('Используйте представленные вам кнопки')

@dp.message_handler(state = States.add_token_file,content_types=['document'])
async def get_toke_file(message:types.Message,state:FSMContext):
    print(f"{datetime.now()}  log--> ADD TOKEN  {call.from_user.id}")
    document_id = message.document.file_id
    file_info = await bot.get_file(document_id)
    fi = file_info.file_path
    name = message.document.file_name
    urllib.request.urlretrieve(f'https://api.telegram.org/file/bot{BOT_TOKEN}/{fi}', f'./token_files/{name}')
    token_files.append(name)
    await bot.send_message(message.from_user.id, 'Файл успешно сохранён',reply_markup=Defs().admin_keyb_main_menu())
    await States.normal_permission.set()

@dp.callback_query_handler(state=States.make_code)
async def make_code(call: types.CallbackQuery, state: FSMContext):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    print(f"{datetime.now()}  log--> MAKE CODE  {call.from_user.id}")

    callback = call.data
    number = Defs().generate_code()
    await state.finish()
    with open("key_db.json") as f:
        codes = json.load(f)
    while number in codes["used_keys"]:
        number = Defs().generate_code()
    time_out = ''
    if callback == "one_hour":
        time_out = '1 hours'
        codes["keys"].append({f"id": f"{number}", "time_out": f"{time_out}"})
    elif callback == "three_hours":
        time_out = '3 hours'
        codes["keys"].append({f"id": f"{number}", "time_out": f"{time_out}"})
    elif callback == "five_hours":
        time_out = '5 hours'
        codes["keys"].append({f"id": f"{number}", "time_out": f"{time_out}"})
    elif callback == "twelve_hours":
        time_out = '12 hours'
        codes["keys"].append({f"id": f"{number}", "time_out": f"{time_out}"})
    elif callback == "one_day":
        time_out = '1 day'
        codes["keys"].append({f"id": f"{number}", "time_out": f"{time_out}"})
    elif callback == "three_days":
        time_out = '3 days'
        codes["keys"].append({f"id": f"{number}", "time_out": f"{time_out}"})
    elif callback == "Forever":
        time_out = 'Forever'
        codes["keys"].append({f"id": f"{number}", "time_out": f"{time_out}"})
    with open("key_db.json", "w") as f:
        json.dump(codes, f, indent=3)
    await call.message.answer(f"Сгенерированный код :\n\n" + f"{'<code>'} {number} {'</code>'} \n\n"
                                                             f"Время действия : {time_out}\n"
                                                             f"Нажмите на код чтобы его скопировать.",
                              parse_mode='HTML')
    await call.message.answer(f"Главное меню", reply_markup=Defs().admin_keyb_main_menu())
    await States.admin.set()

# USER PANEL

@dp.callback_query_handler(state=States.normal_permission)
async def MainMenu(call: types.CallbackQuery, state: FSMContext):
    print(f"{datetime.now()}  log--> NORMAL PERMISSION  {call.from_user.id}")
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    callback = call.data
    await state.finish()
    if callback == 'settings':
        await call.message.answer('Выберите категорию для парсинга', reply_markup=Defs().keyb_categories())
        await States.settings.set()
    elif callback == 'profile':
        with open("users_info.json") as f:
            users = json.load(f)
        date = ''
        try :
            for i in range(len(users['users-active'])):
                if str(users['users-active'][i]['id']) == str(call.from_user.id):
                    date = str(users['users-active'][i]['date'])
                    category = str(users['users-active'][i]['category'])
                    subcategory = str(users['users-active'][i]['subcategory'])
                    keyword = str(users['users-active'][i]['keyword'])
                    filters = (users['users-active'][i]['filters'])
        except Exception:
            print(f"{datetime.now()}  log--> <<ERROR>> NO SUCH CATEGORY  {call.from_user.id}")
        date_2 = str(datetime.now()).split('.')[0]
        if date == 'Forever':
            time_line = "Forever"
        elif date == '0 days 0 hours':
            time_line = date
        else:
            if datetime.strptime(date_2, '%Y-%m-%d %H:%M:%S') > datetime.strptime(date, '%Y-%m-%d %H:%M:%S'):
                time_line = '0 days 0 hours'

            else:
                time_line = (
                    str(datetime.strptime(date, '%Y-%m-%d %H:%M:%S') - datetime.strptime(date_2, '%Y-%m-%d %H:%M:%S')))

        await call.message.answer(f'Ваш профиль:\n'
                                  f'👤Username : @{call.from_user.username}\n'
                                  f'🆔Telegram ID : {call.from_user.id}\n\n'
                                  f'⬇️Настройки ⬇️\n'
                                  f'⚙️Категория : {Defs().get_category(category)}\n'
                                  f'⚙️Подкатегория : {Defs().get_subcategory(category,subcategory)}\n'
                                  f'⚙️Ключевое слово : {Defs().empty_or_no(keyword)}\n'
                                  f'⚙️Фильтры : {Defs().filterr(filters)}\n\n'
                                  f'🕗Статус подписки : {time_line}', reply_markup=Defs().main_menu())
        await States.normal_permission.set()
    elif callback == "subscription":
        await call.message.answer('Меню подписки:', reply_markup=Defs().subscription())
        await States.subscription.set()
    elif callback == "parse":
        await call.message.answer('Используйте представленные вам кнопки', reply_markup=Defs().main_menu())
        await States.normal_permission.set()
    elif callback == 'filter':
        await call.message.answer('Фильтры',reply_markup=Defs().filters())
        await States.filters.set()
    else:
        await call.message.answer('Используйте представленные вам кнопки', reply_markup=Defs().main_menu())
        await States.normal_permission.set()

@dp.callback_query_handler(state=States.subscription)
async def subscription(call: types.CallbackQuery, state: FSMContext):
    print(f"{datetime.now()}  log--> SUBSCRIPTION  {call.from_user.id}")
    await bot.delete_message(call.message.chat.id, call.message.message_id)

    callback = call.data
    await state.finish()
    if callback == 'to_subscribe':
        # vas_realo
        await call.message.answer("Для приобритения кода подписки напишите @vas_realo",
                                  reply_markup=Defs().subscription())
        await States.subscription.set()
    elif callback == 'enter_code':
        await call.message.answer('Введите код доступа:')
        await States.enter_code.set()
    elif callback == 'back_to_menu':
        await call.message.answer('Главное меню:', reply_markup=Defs().main_menu())
        await States.normal_permission.set()

@dp.message_handler(state=States.enter_code)
async def enter_code(message: types.Message, state: FSMContext):
    print(f"{datetime.now()}  log--> ENTERING CODE  {call.from_user.id}")
    code = message.text
    await bot.delete_message(message.chat.id, message.message_id-1)
    await bot.delete_message(message.chat.id, message.message_id-2)


    is_code_true = False
    await state.finish()
    with open("key_db.json") as f:
        codes = json.load(f)
    time_out = ''
    for i in range(len(codes['keys'])):
        if str(codes['keys'][i]['id']) == str(code):
            time_out = codes['keys'][i]['time_out']
            is_code_true = True
            codes["used_keys"].append(codes['keys'][i]['id'])
            del codes['keys'][i]
            with open("key_db.json", "w") as f:
                json.dump(codes, f, indent=3)
            break
    if is_code_true:
        date_finish = ''
        with open("users_info.json") as f:
            users = json.load(f)
        if time_out == "1 hours":
            date_finish = str(datetime.now() + timedelta(hours=1)).split('.')[0]
        elif time_out == "3 hours":
            date_finish = str(datetime.now() + timedelta(hours=3)).split('.')[0]
        elif time_out == "5 hours":
            date_finish = str(datetime.now() + timedelta(hours=5)).split('.')[0]
        elif time_out == "12 hours":
            date_finish = str(datetime.now() + timedelta(hours=12)).split('.')[0]
        elif time_out == "1 day":
            date_finish = str(datetime.now() + timedelta(days=1)).split('.')[0]
        elif time_out == "3 days":
            date_finish = str(datetime.now() + timedelta(days=3)).split('.')[0]
        elif time_out == "Forever":
            date_finish = "Forever"
        for i in range(len(users['users-active'])):
            if str(users['users-active'][i]['id']) == str(message.from_user.id):
                users['users-active'][i]['date'] = date_finish
        with open("users_info.json", "w") as f:
            json.dump(users, f, indent=3)
        print(f"{datetime.now()}  log--> ENTERED CODE  {message.from_user.id}")
        for admin in admin_ids:
            await bot.send_message(admin,
                                   f"Пользователь "
                                   f"{hlink(message.from_user.first_name, 'tg://user?id=' + str(message.from_user.id))}"
                                   f" активировал код")
        await message.answer('Главное меню', reply_markup=Defs().main_menu())
        await States.normal_permission.set()
    else:
        await message.answer('К сожалению код не действителен\n',reply_markup=Defs().code_is_false())

        await States.code_is_false.set()
@dp.callback_query_handler(state = States.code_is_false)
async def code_is_fase(call:types.CallbackQuery,state:FSMContext):
    callback = call.data
    print(f"{datetime.now()}  log--> CODE IS FALSE  {call.from_user.id}")
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    if callback == 'try_again':
        await call.message.answer('Введите код доступа :')
        await States.enter_code.set()
    elif callback == 'back_to_menu':
        await call.message.answer('Главное меню',reply_markup=Defs().main_menu())
        await States.normal_permission.set()

@dp.callback_query_handler(state = States.filters)
async def filter (call:types.CallbackQuery,state:FSMContext):
    callback = call.data
    print(f"{datetime.now()}  log--> FILTERS  {call.from_user.id}")
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    with open('users_info.json') as f :
        users = json.load(f)
    index = 0
    for ind,user in enumerate(users['users-active']) :
        if user['id'] == call.from_user.id:
            index = ind
            break
    if callback == 'clear_filters':
        users['users-active'][index]['filters']=[]
        await call.message.answer('Список фильтров очищен',
                                  reply_markup=Defs().main_menu())
        if call.from_user.id in admin_ids:
            await call.message.answer('Главное меню:', reply_markup=Defs().admin_keyb_main_menu())
            await States.admin.set()
        else:
            await call.message.answer('Главное меню:', reply_markup=Defs().main_menu())
            await States.normal_permission.set()
    elif callback == 'black_list_of_words':
        await call.message.answer(f'Черный список слов:\n{users["users-active"][index]["black_list_of_words"]}',reply_markup=Defs().filters())

    elif callback == 'back_to_menu':
        if call.from_user.id in admin_ids:
            await call.message.answer('Главное меню:', reply_markup=Defs().admin_keyb_main_menu())
            await States.admin.set()
        else:
            await call.message.answer('Главное меню:', reply_markup=Defs().main_menu())
            await States.normal_permission.set()
    elif callback in filters.keys() :
        if callback not in users['users-active'][index]['filters']:
            users['users-active'][index]['filters'].append(callback)
            await call.message.answer(f'Фильтр {callback} '
                                      f'добавлен',reply_markup=Defs().main_menu())
            await States.normal_permission.set()
    with open('users_info.json','w')as f :
        json.dump(users,f,indent=3)

@dp.callback_query_handler(state=States.settings)
async def categories(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    print(f"{datetime.now()}  log--> CATEGORIES  {call.from_user.id}")
    await state.finish()
    with open("users_info.json") as f:
        users = json.load(f)
    index = int()
    for ind, userr in enumerate(users["users-active"]):
        if userr["id"] == call.from_user.id:
            index = ind
            break
    if callback == 'back_to_menu':
        if call.from_user.id in admin_ids:
            await call.message.answer('Главное меню:', reply_markup=Defs().admin_keyb_main_menu())
            await States.admin.set()
        else:
            await call.message.answer('Главное меню:', reply_markup=Defs().main_menu())
            await States.normal_permission.set()
    elif callback == 'transport':
        await call.message.answer(f'Категория "{category_dict.get(callback)}"',
                                  reply_markup=Defs().keyb_sub_categories(callback))
        users['users-active'][index]['category'] = callback
        users['users-active'][index]['subcategory'] = ''
        await States.transport.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
    elif callback == 'nedvizhimost':
        await call.message.answer(f'Категория "{category_dict.get(callback)}"',
                                  reply_markup=Defs().keyb_sub_categories(callback))
        users['users-active'][index]['category'] = callback
        users['users-active'][index]['subcategory'] = ''
        await States.nedvizhimost.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
    elif callback == 'zapchasti-dlya-transporta':
        await call.message.answer(f'Категория "{category_dict.get(callback)}"',
                                  reply_markup=Defs().keyb_sub_categories(callback))
        users['users-active'][index]['category'] = callback
        users['users-active'][index]['subcategory'] = ''
        await States.zapchasti_dlya_transporta.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
    elif callback == 'zhivotnye':
        await call.message.answer(f'Категория "{category_dict.get(callback)}"',
                                  reply_markup=Defs().keyb_sub_categories(callback))
        users['users-active'][index]['category'] = callback
        users['users-active'][index]['subcategory'] = ''
        await States.zhivotnye.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
    elif callback == 'dom-i-sad':
        await call.message.answer(f'Категория "{category_dict.get(callback)}"',
                                  reply_markup=Defs().keyb_sub_categories(callback))
        users['users-active'][index]['category'] = callback
        users['users-active'][index]['subcategory'] = ''
        await States.dom_i_sad.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
    elif callback == 'detskiy-mir':
        await call.message.answer(f'Категория "{category_dict.get(callback)}"',
                                  reply_markup=Defs().keyb_sub_categories(callback))
        users['users-active'][index]['category'] = callback
        users['users-active'][index]['subcategory'] = ''
        await States.detskiy_mir.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
    elif callback == 'elektronika':
        await call.message.answer(f'Категория "{category_dict.get(callback)}"',
                                  reply_markup=Defs().keyb_sub_categories(callback))
        users['users-active'][index]['category'] = callback
        users['users-active'][index]['subcategory'] = ''
        await States.elektronika.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
    elif callback == 'moda-i-stil':
        await call.message.answer(f'Категория "{category_dict.get(callback)}"',
                                  reply_markup=Defs().keyb_sub_categories(callback))
        users['users-active'][index]['category'] = callback
        users['users-active'][index]['subcategory'] = ''
        await States.moda_i_stil.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
    elif callback == 'hobbi-otdyh-i-sport':
        await call.message.answer(f'Категория "{category_dict.get(callback)}"',
                                  reply_markup=Defs().keyb_sub_categories(callback))
        users['users-active'][index]['category'] = callback
        users['users-active'][index]['subcategory'] = ''
        await States.hobbi_otdyh_i_sport.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
    else:
        await call.message.answer('Используйте представленные вам кнопки',reply_markup=Defs().keyb_categories())
        await States.settings.set()
    with open("users_info.json", 'w') as f:
        json.dump(users, f, indent=3)

@dp.callback_query_handler(state=States.transport)
async def transport_category(call: types.CallbackQuery, state: FSMContext):
    print(f"{datetime.now()}  log--> TRANSPORT  {call.from_user.id}")
    callback = call.data
    await state.finish()
    with open("users_info.json") as f:
        users = json.load(f)
    index = int()
    for ind, userr in enumerate(users["users-active"]):
        if userr["id"] == call.from_user.id:
            index = ind
            break
    if callback == 'back_to_categories':
        await call.message.answer('Категории', reply_markup=Defs().keyb_categories())
        users['users-active'][index]['category'] = ''
        users['users-active'][index]['subcategory'] = ''
        await States.settings.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
    elif callback == 'all_category':
        await call.message.answer('Главное меню', reply_markup=Defs().main_menu())
        await States.normal_permission.set()
    elif callback == 'enter_keyword':
        await call.message.answer('Введіть ключ слово ✏️:')
        await States.enter_keyword.set()
    elif callback in subcategory.get('transport').keys():
        await call.message.answer(f"Вы выбрали подкатегорию :{subcategory.get('transport').get(callback)}")
        await call.message.answer('Желаете ввести ключ-слово ?', reply_markup=Defs().enter_or_no())
        users['users-active'][index]['subcategory'] = callback
        users["users-active"][index]['keyword'] = ''
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await States.enter_keyword_or_no.set()
    else:
        await call.message.answer('Используйте представленные вам кнопки',reply_markup=Defs().keyb_sub_categories('transport'))
        await States.transport.set()
    with open("users_info.json", 'w') as f:
        json.dump(users, f, indent=3)

@dp.callback_query_handler(state=States.nedvizhimost)
async def nedvizhimost_category(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    print(f"{datetime.now()}  log--> NEDVIHIMOST  {call.from_user.id}")
    await state.finish()
    with open("users_info.json") as f:
        users = json.load(f)
    index = int()
    for ind, userr in enumerate(users["users-active"]):
        if userr["id"] == call.from_user.id:
            index = ind
            break
    if callback == 'back_to_categories':
        await call.message.answer('Категории', reply_markup=Defs().keyb_categories())
        users['users-active'][index]['category'] = ''
        users['users-active'][index]['subcategory'] = ''
        await States.settings.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
    elif callback == 'all_category':
        await call.message.answer('Главное меню', reply_markup=Defs().main_menu())
        await States.normal_permission.set()
    elif callback == 'enter_keyword':
        await call.message.answer('Введіть ключ слово ✏️:')
        await States.enter_keyword.set()
    elif callback in subcategory.get('nedvizhimost').keys():
        await call.message.answer(f"Вы выбрали подкатегорию :{subcategory.get('nedvizhimost').get(callback)}")
        await call.message.answer('Желаете ввести ключ-слово ?', reply_markup=Defs().enter_or_no())
        users['users-active'][index]['subcategory'] = callback
        users["users-active"][index]['keyword'] = ''
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await States.enter_keyword_or_no.set()
    else:
        await call.message.answer('Используйте представленные вам кнопки',reply_markup=Defs().keyb_sub_categories('nedvizhimost'))
        await States.nedvizhimost.set()
    with open("users_info.json", 'w') as f:
        json.dump(users, f, indent=3)

@dp.callback_query_handler(state=States.zapchasti_dlya_transporta)
async def zapchasti_dya_transporta_category(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    print(f"{datetime.now()}  log--> ZAPCHASTI DLYA TRANSPORTA  {call.from_user.id}")
    await state.finish()
    with open("users_info.json") as f:
        users = json.load(f)
    index = int()
    for ind, userr in enumerate(users["users-active"]):
        if userr["id"] == call.from_user.id:
            index = ind
            break
    if callback == 'back_to_categories':
        await call.message.answer('Категории', reply_markup=Defs().keyb_categories())
        users['users-active'][index]['category'] = ''
        users['users-active'][index]['subcategory'] = ''
        await States.settings.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
    elif callback == 'all_category':
        await call.message.answer('Главное меню', reply_markup=Defs().main_menu())
        await States.normal_permission.set()
    elif callback == 'enter_keyword':
        await call.message.answer('Введіть ключ слово ✏️:')
        await States.enter_keyword.set()
    elif callback in subcategory.get('zapchasti-dlya-transporta').keys():
        await call.message.answer(f"Вы выбрали подкатегорию :{subcategory.get('zapchasti-dlya-transporta').get(callback)}")
        await call.message.answer('Желаете ввести ключ-слово ?', reply_markup=Defs().enter_or_no())
        users['users-active'][index]['subcategory'] = callback
        users["users-active"][index]['keyword'] = ''
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await States.enter_keyword_or_no.set()
    else:
        await call.message.answer('Используйте представленные вам кнопки',reply_markup=Defs().keyb_sub_categories('zapchasti-dlya-transporta'))
        await States.zapchasti_dlya_transporta.set()
    with open("users_info.json", 'w') as f:
        json.dump(users, f, indent=3)

@dp.callback_query_handler(state=States.zhivotnye)
async def zhivotnye_transporta_category(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    print(f"{datetime.now()}  log--> ZHIVOTNYE  {call.from_user.id}")
    await state.finish()
    with open("users_info.json") as f:
        users = json.load(f)
    index = int()
    for ind, userr in enumerate(users["users-active"]):
        if userr["id"] == call.from_user.id:
            index = ind
            break
    if callback == 'back_to_categories':
        await call.message.answer('Категории', reply_markup=Defs().keyb_categories())
        users['users-active'][index]['category'] = ''
        users['users-active'][index]['subcategory'] = ''
        await States.settings.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
    elif callback == 'all_category':
        await call.message.answer('Главное меню', reply_markup=Defs().main_menu())
        await States.normal_permission.set()
    elif callback == 'enter_keyword':
        await call.message.answer('Введіть ключ слово ✏️:')
        await States.enter_keyword.set()
    elif callback in subcategory.get('zhivotnye').keys():
        await call.message.answer(f"Вы выбрали подкатегорию :{subcategory.get('zhivotnye').get(callback)}")
        await call.message.answer('Желаете ввести ключ-слово ?', reply_markup=Defs().enter_or_no())
        users['users-active'][index]['subcategory'] = callback
        users["users-active"][index]['keyword'] = ''
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await States.enter_keyword_or_no.set()
    else:
        await call.message.answer('Используйте представленные вам кнопки',reply_markup=Defs().keyb_sub_categories('zhivotnye'))
        await States.zhivotnye.set()
    with open("users_info.json", 'w') as f:
        json.dump(users, f, indent=3)

@dp.callback_query_handler(state=States.dom_i_sad)
async def dom_i_sad_category(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    print(f"{datetime.now()}  log--> DOM I SAD  {call.from_user.id}")
    await state.finish()
    with open("users_info.json") as f:
        users = json.load(f)
    index = int()
    for ind, userr in enumerate(users["users-active"]):
        if userr["id"] == call.from_user.id:
            index = ind
            break
    if callback == 'back_to_categories':
        await call.message.answer('Категории', reply_markup=Defs().keyb_categories())
        users['users-active'][index]['category'] = ''
        users['users-active'][index]['subcategory'] = ''
        await States.settings.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
    elif callback == 'all_category':
        await call.message.answer('Главное меню', reply_markup=Defs().main_menu())
        await States.normal_permission.set()
    elif callback == 'enter_keyword':
        await call.message.answer('Введіть ключ слово ✏️:')
        await States.enter_keyword.set()
    elif callback in subcategory.get('dom-i-sad').keys():
        await call.message.answer(f"Вы выбрали подкатегорию :{subcategory.get('dom-i-sad').get(callback)}")
        await call.message.answer('Желаете ввести ключ-слово ?', reply_markup=Defs().enter_or_no())
        users['users-active'][index]['subcategory'] = callback
        users["users-active"][index]['keyword'] = ''
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await States.enter_keyword_or_no.set()
    else:
        await call.message.answer('Используйте представленные вам кнопки',reply_markup=Defs().keyb_sub_categories('dom-i-sad'))
        await States.dom_i_sad.set()
    with open("users_info.json", 'w') as f:
        json.dump(users, f, indent=3)

@dp.callback_query_handler(state=States.detskiy_mir)
async def detskiy_mir_category(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    print(f"{datetime.now()}  log--> DETSKIY MIR  {call.from_user.id}")
    await state.finish()
    with open("users_info.json") as f:
        users = json.load(f)
    index = int()
    for ind, userr in enumerate(users["users-active"]):
        if userr["id"] == call.from_user.id:
            index = ind
            break
    if callback == 'back_to_categories':
        await call.message.answer('Категории', reply_markup=Defs().keyb_categories())
        users['users-active'][index]['category'] = ''
        users['users-active'][index]['subcategory'] = ''
        await States.settings.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
    elif callback == 'all_category':
        await call.message.answer('Главное меню', reply_markup=Defs().main_menu())
        await States.normal_permission.set()
    elif callback == 'enter_keyword':
        await call.message.answer('Введіть ключ слово ✏️:')
        await States.enter_keyword.set()
    elif callback in subcategory.get('detskiy-mir').keys():
        await call.message.answer(f"Вы выбрали подкатегорию :{subcategory.get('detskiy-mir').get(callback)}")
        await call.message.answer('Желаете ввести ключ-слово ?', reply_markup=Defs().enter_or_no())
        users['users-active'][index]['subcategory'] = callback
        users["users-active"][index]['keyword'] = ''
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await States.enter_keyword_or_no.set()
    else:
        await call.message.answer('Используйте представленные вам кнопки',reply_markup=Defs().keyb_sub_categories('detskiy-mir'))
        await States.detskiy_mir.set()
    with open("users_info.json", 'w') as f:
        json.dump(users, f, indent=3)

@dp.callback_query_handler(state=States.elektronika)
async def elektronika_category(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    print(f"{datetime.now()}  log--> ELEKTRONIKA  {call.from_user.id}")
    await state.finish()
    with open("users_info.json") as f:
        users = json.load(f)
    index = int()
    for ind, userr in enumerate(users["users-active"]):
        if userr["id"] == call.from_user.id:
            index = ind
            break
    if callback == 'back_to_categories':
        await call.message.answer('Категории', reply_markup=Defs().keyb_categories())
        users['users-active'][index]['category'] = ''
        users['users-active'][index]['subcategory'] = ''
        await States.settings.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
    elif callback == 'all_category':
        await call.message.answer('Главное меню', reply_markup=Defs().main_menu())
        await States.normal_permission.set()
    elif callback == 'enter_keyword':
        await call.message.answer('Введіть ключ слово ✏️:')
        await States.enter_keyword.set()
    elif callback in subcategory.get('elektronika').keys():
        await call.message.answer(f"Вы выбрали подкатегорию :{subcategory.get('elektronika').get(callback)}")
        await call.message.answer('Желаете ввести ключ-слово ?', reply_markup=Defs().enter_or_no())
        users['users-active'][index]['subcategory'] = callback
        users["users-active"][index]['keyword'] = ''
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await States.enter_keyword_or_no.set()
    else:
        await call.message.answer('Используйте представленные вам кнопки',reply_markup=Defs().keyb_sub_categories('elektronika'))
        await States.elektronika.set()
    with open("users_info.json", 'w') as f:
        json.dump(users, f, indent=3)

@dp.callback_query_handler(state=States.moda_i_stil)
async def moda_i_stil_category(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    print(f"{datetime.now()}  log--> MODA I STIL  {call.from_user.id}")
    await state.finish()
    with open("users_info.json") as f:
        users = json.load(f)
    index = int()
    for ind, userr in enumerate(users["users-active"]):
        if userr["id"] == call.from_user.id:
            index = ind
            break
    if callback == 'back_to_categories':
        await call.message.answer('Категории', reply_markup=Defs().keyb_categories())
        users['users-active'][index]['category'] = ''
        users['users-active'][index]['subcategory'] = ''
        await States.settings.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
    elif callback == 'all_category':
        await call.message.answer('Главное меню', reply_markup=Defs().main_menu())
        await States.normal_permission.set()
    elif callback == 'enter_keyword':
        await call.message.answer('Введіть ключ слово ✏️:')
        await States.enter_keyword.set()
    elif callback in subcategory.get('moda-i-stil').keys():
        await call.message.answer(f"Вы выбрали подкатегорию :{subcategory.get('moda-i-stil').get(callback)}")
        await call.message.answer('Желаете ввести ключ-слово ?', reply_markup=Defs().enter_or_no())
        users['users-active'][index]['subcategory'] = callback
        users["users-active"][index]['keyword'] = ''
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await States.enter_keyword_or_no.set()
    else:
        await call.message.answer('Используйте представленные вам кнопки',reply_markup=Defs().keyb_sub_categories('moda-i-stil'))
        await States.moda_i_stil.set()
    with open("users_info.json", 'w') as f:
        json.dump(users, f, indent=3)

@dp.callback_query_handler(state=States.hobbi_otdyh_i_sport)
async def hobbi_otdyh_i_sport_category(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    print(f"{datetime.now()}  log--> OTDYH I SPORT  {call.from_user.id}")
    await state.finish()
    with open("users_info.json") as f:
        users = json.load(f)
    index = int()
    for ind, userr in enumerate(users["users-active"]):
        if userr["id"] == call.from_user.id:
            index = ind
            break
    if callback == 'back_to_categories':
        await call.message.answer('Категории', reply_markup=Defs().keyb_categories())
        users['users-active'][index]['category'] = ''
        users['users-active'][index]['subcategory'] = ''
        await States.settings.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
    elif callback == 'all_category':
        await call.message.answer('Главное меню', reply_markup=Defs().main_menu())
        await States.normal_permission.set()
    elif callback == 'enter_keyword':
        await call.message.answer('Введіть ключ слово ✏️:')
        await States.enter_keyword.set()
    elif callback in subcategory.get('hobbi-otdyh-i-sport').keys():
        await call.message.answer(f"Вы выбрали подкатегорию :{subcategory.get('hobbi-otdyh-i-sport').get(callback)}")
        await call.message.answer('Желаете ввести ключ-слово ?', reply_markup=Defs().enter_or_no())
        users['users-active'][index]['subcategory'] = callback
        users["users-active"][index]['keyword'] = ''
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await States.enter_keyword_or_no.set()
    else:
        await call.message.answer('Используйте представленные вам кнопки',reply_markup=Defs().keyb_sub_categories('hobbi-otdyh-i-sport'))
        await States.hobbi_otdyh_i_sport.set()
    with open("users_info.json", 'w') as f:
        json.dump(users, f, indent=3)

@dp.callback_query_handler(state = States.enter_keyword_or_no)
async def enter_keyword_or_no(call:types.CallbackQuery,state:FSMContext):
    callback = call.data
    print(f"{datetime.now()}  log--> CHOOSED SUBCATEGORY  {call.from_user.id}")
    await state.finish()
    if callback == "enter" :
        await call.message.answer('Введите ключ слово :')
        await States.enter_keyword.set()
    elif callback == "no" :
        await call.message.answer('Подкатегория добавлена в поиск\n\n'
                                  'Главное меню',reply_markup=Defs().main_menu())
        await States.normal_permission.set()

@dp.message_handler(state=States.enter_keyword)
async def enter_keyword(message: types.Message, state: FSMContext):
    keyword = message.text
    print(f"{datetime.now()}  log--> ENTERING KEYWORD  {call.from_user.id}")
    await state.finish()
    with open("users_info.json") as f:
        users = json.load(f)
    index = int()
    for ind, userr in enumerate(users["users-active"]):
        if userr["id"] == message.from_user.id:
            index = ind
            break
    users["users-active"][index]['keyword'] = keyword
    with open("users_info.json", 'w') as f:
        json.dump(users, f, indent=3)
    await message.answer('Ключевое слово добавлено')
    await message.answer('Главное меню',reply_markup=Defs().main_menu())
    await States.normal_permission.set()

@dp.callback_query_handler(state=States.parse)
async def parsing(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    print(f"{datetime.now()}  log--> START PARSING  {call.from_user.id}")
    with open("users_info.json") as f:
        users = json.load(f)
    for ind, user in enumerate(users["users-active"]):
        if user["id"] == call.from_user.id:
            if Defs().check_date(user['date']):
                print(f"{datetime.now()}  log--> PARSER {call.from_user.id}")



executor.start_polling(dp, skip_updates=True)
