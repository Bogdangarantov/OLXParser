# OUR FILES IMPORT
from messages import *
from bot_info import *
from defs import Defs
from admins import *
from State_m import *
from keyboards_info import *
# Libraries import
import json
from datetime import datetime
from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.types import *
from aiogram.utils.markdown import hlink
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands="start")
async def ComandStart(message: types.Message):
    print(message.from_user.id)
    permission = False
    with open("users_info.json") as f:
        info = json.load(f)
    for i in range(len(info['users'])):
        if int(info['users'][i]['id']) == message.from_user.id:
            permission = True
            break
    if permission:
        await message.answer('Вас приветствует бот ОЛХ', reply_markup=Defs().main_menu())
        await States.permission_accepted.set()
    else:
        await message.answer('К сожалению у вас нет доступа к Боту, модератор свяжется с вами')
        for i in admin_ids:
            q = message.from_user.first_name
            user_id = message.from_user
            mention = hlink(q, "tg://user?id=" + str(user_id.id))
            await bot.send_message(i,
                                   f'user {mention} tried to use bot, connect him if u want to accept him')


# USER PANEL

@dp.callback_query_handler(state=States.permission_accepted)
async def MainMenu(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    await state.finish()
    if callback == 'settings':
        await call.message.answer('Выберите категорию для парсинга', reply_markup=Defs().keyb_categories())
        await bot.delete_message(call.message.chat.id, call.message.message_id)

        await States.settings.set()

    if callback == 'Profile':
        await call.message.answer('Ваш профиль:')
        await bot.delete_message(call.message.chat.id, call.message.message_id)

        # await States.profile.set()
        #


@dp.callback_query_handler(state=States.settings)
async def categories(call: types.CallbackQuery, state: FSMContext):

    callback = call.data
    await state.finish()
    if callback == 'transport':
        print(Defs().keyb_sub_categories(callback))
        await call.message.answer(f'Категория "{category_dict.get(callback)}"',
                                  reply_markup=Defs().keyb_sub_categories(callback))
        await States.transport.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'nedvizhimost':
        await call.message.answer(f'Категория "{category_dict.get(callback)}"',
                                  reply_markup=Defs().keyb_sub_categories(callback))
        await States.nedvizhimost.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'zapchasti-dlya-transporta':
        await call.message.answer(f'Категория "{category_dict.get(callback)}"',
                                  reply_markup=Defs().keyb_sub_categories(callback))
        await States.zapchasti_dlya_transporta.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'zhivotnye':
        await call.message.answer(f'Категория "{category_dict.get(callback)}"',
                                  reply_markup=Defs().keyb_sub_categories(callback))
        await States.zhivotnye.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'dom-i-sad':
        await call.message.answer(f'Категория "{category_dict.get(callback)}"',
                                  reply_markup=Defs().keyb_sub_categories(callback))
        await States.dom_i_sad.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'detskiy-mir':
        await call.message.answer(f'Категория "{category_dict.get(callback)}"',
                                  reply_markup=Defs().keyb_sub_categories(callback))
        await States.detskiy_mir.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'elektronika':
        await call.message.answer(f'Категория "{category_dict.get(callback)}"',
                                  reply_markup=Defs().keyb_sub_categories(callback))
        await States.elektronika.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'moda-i-stil':
        await call.message.answer(f'Категория "{category_dict.get(callback)}"',
                                  reply_markup=Defs().keyb_sub_categories(callback))
        await States.moda_i_stil.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'hobbi-otdyh-i-sport':
        await call.message.answer(f'Категория "{category_dict.get(callback)}"',
                                  reply_markup=Defs().keyb_sub_categories(callback))
        await States.hobbi_otdyh_i_sport.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'back_to_menu':
        await call.message.answer('Главное меню', reply_markup=Defs().main_menu())
        await bot.delete_message(call.message.chat.id, call.message.message_id)


@dp.callback_query_handler(state=States.transport)
async def transport_category(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    await state.finish()
    if callback == 'legkovye-avtomobili':
        await call.message.answer(subcategory.get('transport').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'spetstehnika':
        await call.message.answer(subcategory.get('transport').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'selhoztehnika':
        await call.message.answer(subcategory.get('transport').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'moto':
        await call.message.answer(subcategory.get('transport').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'avtomobili-iz-polshi':
        await call.message.answer(subcategory.get('transport').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'avtobusy':
        await call.message.answer(subcategory.get('transport').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'vodnyy-transport':
        await call.message.answer(subcategory.get('transport').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'pritsepy-doma-na-kolesah':
        await call.message.answer(subcategory.get('transport').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'vozdushnyy-transport':
        await call.message.answer(subcategory.get('transport').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'drugoy-transport':
        await call.message.answer(subcategory.get('transport').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'gruzovye-avtomobili':
        await call.message.answer(subcategory.get('transport').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'back_to_categories':
        await call.message.answer('Категории', reply_markup=Defs().keyb_categories())
        await States.settings.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)


@dp.callback_query_handler(state=States.nedvizhimost)
async def nedvizhimost_category(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    await state.finish()
    if callback == 'posutochno-pochasovo':
        await call.message.answer(subcategory.get('nedvizhimost').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'nedvizhimost-za-rubezhom':
        await call.message.answer(subcategory.get('nedvizhimost').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'komnaty':
        await call.message.answer(subcategory.get('nedvizhimost').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'zemlya':
        await call.message.answer(subcategory.get('nedvizhimost').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'kommercheskaya-nedvizhimost':
        await call.message.answer(subcategory.get('nedvizhimost').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'kwatery-pracownicze':
        await call.message.answer(subcategory.get('nedvizhimost').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'doma':
        await call.message.answer(subcategory.get('nedvizhimost').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'kvartiry/novostroyki':
        await call.message.answer(subcategory.get('nedvizhimost').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'hale-magazyny':
        await call.message.answer(subcategory.get('nedvizhimost').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'garazhy-parkovki':
        await call.message.answer(subcategory.get('nedvizhimost').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'kvartiry':
        await call.message.answer(subcategory.get('nedvizhimost').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'back_to_categories':
        await call.message.answer('Категории', reply_markup=Defs().keyb_categories())
        await States.settings.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)


@dp.callback_query_handler(state=States.zapchasti_dlya_transporta)
async def zapchasti_dya_transporta_category(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    await state.finish()
    if callback == 'avtozapchasti-i-aksessuary':
        await call.message.answer(subcategory.get('zapchasti-dlya-transporta').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'shiny-diski-i-kolesa':
        await call.message.answer(subcategory.get('zapchasti-dlya-transporta').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'zapchasti-dlya-spets-sh-tehniki':
        await call.message.answer(subcategory.get('zapchasti-dlya-transporta').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'motozapchasti-i-aksessuary':
        await call.message.answer(subcategory.get('zapchasti-dlya-transporta').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'prochie-zapchasti':
        await call.message.answer(subcategory.get('zapchasti-dlya-transporta').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'back_to_categories':
        await call.message.answer('Категории', reply_markup=Defs().keyb_categories())
        await States.settings.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)


@dp.callback_query_handler(state=States.zhivotnye)
async def zapchasti_dya_transporta_category(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    await state.finish()
    if callback == 'sobaki':
        await call.message.answer(subcategory.get('zhivotnye').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'selskohozyaystvennye-zhivotnye':
        await call.message.answer(subcategory.get('zhivotnye').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'akvariumnye-rybki':
        await call.message.answer(subcategory.get('zhivotnye').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'koshki':
        await call.message.answer(subcategory.get('zhivotnye').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'ptitsy':
        await call.message.answer(subcategory.get('zhivotnye').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'drugie-zhivotnye':
        await call.message.answer(subcategory.get('zhivotnye').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'gryzuny':
        await call.message.answer(subcategory.get('zhivotnye').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'reptilii':
        await call.message.answer(subcategory.get('zhivotnye').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'tovary-dlya-zhivotnyh':
        await call.message.answer(subcategory.get('zhivotnye').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'back_to_categories':
        await call.message.answer('Категории', reply_markup=Defs().keyb_categories())
        await States.settings.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)


@dp.callback_query_handler(state=States.dom_i_sad)
async def dom_i_sad_category(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    await state.finish()
    if callback == 'mebel':
        await call.message.answer(subcategory.get('dom-i-sad').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'stroitelstvo-remont':
        await call.message.answer(subcategory.get('dom-i-sad').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'sprzet-agd':
        await call.message.answer(subcategory.get('dom-i-sad').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'kantstovary-rashodnye-materialy':
        await call.message.answer(subcategory.get('dom-i-sad').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'produkty-pitaniya-napitki':
        await call.message.answer(subcategory.get('dom-i-sad').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'sad-ogorod':
        await call.message.answer(subcategory.get('dom-i-sad').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'predmety-interera':
        await call.message.answer(subcategory.get('dom-i-sad').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'instrumenty':
        await call.message.answer(subcategory.get('dom-i-sad').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'prochie-tovary-dlya-doma':
        await call.message.answer(subcategory.get('dom-i-sad').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'back_to_categories':
        await call.message.answer('Категории', reply_markup=Defs().keyb_categories())
        await States.settings.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)


@dp.callback_query_handler(state=States.detskiy_mir)
async def zapchasti_dya_transporta_category(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    await state.finish()
    if callback == 'igrushki':
        await call.message.answer(subcategory.get('detskiy-mir').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'detskaya-odezhda':
        await call.message.answer(subcategory.get('detskiy-mir').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'detskie-kolyaski':
        await call.message.answer(subcategory.get('detskiy-mir').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'detskaya-obuv':
        await call.message.answer(subcategory.get('detskiy-mir').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'akcesoria-dla-niemowlat':
        await call.message.answer(subcategory.get('detskiy-mir').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'detskaya-mebel':
        await call.message.answer(subcategory.get('detskiy-mir').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'detskie-avtokresla':
        await call.message.answer(subcategory.get('detskiy-mir').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'prochie-detskie-tovary':
        await call.message.answer(subcategory.get('detskiy-mir').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'back_to_categories':
        await call.message.answer('Категории', reply_markup=Defs().keyb_categories())
        await States.settings.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)

@dp.callback_query_handler(state=States.elektronika)
async def zapchasti_dya_transporta_category(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    await state.finish()
    if callback == 'telefony-i-aksesuary':
        await call.message.answer(subcategory.get('elektronika').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'planshety-el-knigi-i-aksessuary':
        await call.message.answer(subcategory.get('elektronika').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'foto-video':
        await call.message.answer(subcategory.get('elektronika').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'aksessuary-i-komplektuyuschie':
        await call.message.answer(subcategory.get('elektronika').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'tehnika-dlya-doma':
        await call.message.answer(subcategory.get('elektronika').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'audiotehnika':
        await call.message.answer(subcategory.get('elektronika').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'kompyutery-i-komplektuyuschie':
        await call.message.answer(subcategory.get('elektronika').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'igry-i-igrovye-pristavki':
        await call.message.answer(subcategory.get('elektronika').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'prochaja-electronika':
        await call.message.answer(subcategory.get('elektronika').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'tehnika-dlya-kuhni':
        await call.message.answer(subcategory.get('elektronika').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'noutbuki-i-aksesuary':
        await call.message.answer(subcategory.get('elektronika').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'klimaticheskoe-oborudovanie':
        await call.message.answer(subcategory.get('elektronika').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'individualnyy-uhod':
        await call.message.answer(subcategory.get('elektronika').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'tv-videotehnika':
        await call.message.answer(subcategory.get('elektronika').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'back_to_categories':
        await call.message.answer('Категории', reply_markup=Defs().keyb_categories())
        await States.settings.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)


@dp.callback_query_handler(state=States.moda_i_stil)
async def zapchasti_dya_transporta_category(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    await state.finish()
    if callback == 'odezhda':
        await call.message.answer(subcategory.get('moda-i-stil').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'naruchnye-chasy':
        await call.message.answer(subcategory.get('moda-i-stil').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'podarki':
        await call.message.answer(subcategory.get('moda-i-stil').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'aksessuary':
        await call.message.answer(subcategory.get('moda-i-stil').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'krasota-zdorove':
        await call.message.answer(subcategory.get('moda-i-stil').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'moda-raznoe':
        await call.message.answer(subcategory.get('moda-i-stil').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'back_to_categories':
        await call.message.answer('Категории', reply_markup=Defs().keyb_categories())
        await States.settings.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)


@dp.callback_query_handler(state=States.hobbi_otdyh_i_sport)
async def zapchasti_dya_transporta_category(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    await state.finish()
    if callback == 'muzykalnye-instrumenty':
        await call.message.answer(subcategory.get('hobbi-otdyh-i-sport').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'sport-otdyh':
        await call.message.answer(subcategory.get('hobbi-otdyh-i-sport').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'drugoe':
        await call.message.answer(subcategory.get('hobbi-otdyh-i-sport').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'antikvariat-kollektsii':
        await call.message.answer(subcategory.get('hobbi-otdyh-i-sport').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'knigi-zhurnaly':
        await call.message.answer(subcategory.get('hobbi-otdyh-i-sport').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'cd-dvd-plastinki':
        await call.message.answer(subcategory.get('hobbi-otdyh-i-sport').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'bilety':
        await call.message.answer(subcategory.get('hobbi-otdyh-i-sport').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'poisk-poputchikov':
        await call.message.answer(subcategory.get('hobbi-otdyh-i-sport').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'poisk-grupp-muzykantov':
        await call.message.answer(subcategory.get('hobbi-otdyh-i-sport').get(callback))
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        # TODO
    elif callback == 'back_to_categories':
        await call.message.answer('Категории', reply_markup=Defs().keyb_categories())
        await States.settings.set()
        await bot.delete_message(call.message.chat.id, call.message.message_id)

executor.start_polling(dp, skip_updates=True)
