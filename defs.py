from keyboards_info import *
from admins import *
from datetime import datetime
from aiogram.types import *
import random


class Defs:
    def __init__(self):
        return

    @staticmethod
    def keyb_categories():
        keyb_categoriess = InlineKeyboardMarkup(row_width=2)
        row = []
        for ind, key in enumerate(category_dict.keys()):

            elem = category_dict.get(key)
            buttons = InlineKeyboardButton(elem, callback_data=key)
            row.append(buttons)
            if len(row) == 2:
                keyb_categoriess.row(row[0], row[1])
                row = []
            elif ind == len(category_dict.keys()) - 1:
                keyb_categoriess.row(row[0])
                row = []
        button = InlineKeyboardButton(text="🔙Назад", callback_data='back_to_menu')
        keyb_categoriess.add(button)
        return keyb_categoriess

    @staticmethod
    def main_menu():
        keyb_main_menu = InlineKeyboardMarkup(row_width=2)
        row = []
        for ind, key in enumerate(main_menu_dict.keys()):
            elem = main_menu_dict.get(key)
            buttons = InlineKeyboardButton(text=elem, callback_data=key)
            row.append(buttons)
            if len(row) == 2:
                keyb_main_menu.row(row[0], row[1])
                row = []
            elif ind == len(main_menu_dict.keys()) - 1:
                keyb_main_menu.row(row[0])
                row = []
        return keyb_main_menu

    @staticmethod
    def keyb_sub_categories(cat):
        print(cat)
        keyb_subcategories = InlineKeyboardMarkup()
        row = []
        dict_in_subcategories = subcategory.get(cat)
        for ind, key in enumerate(dict_in_subcategories.keys()):
            elem = dict_in_subcategories.get(key)
            buttons = InlineKeyboardButton(elem, callback_data=key)
            row.append(buttons)
            if len(row) == 2:
                keyb_subcategories.row(row[0], row[1])
                row = []
            elif ind == len(dict_in_subcategories.keys()) - 1:
                keyb_subcategories.row(row[0])
                row = []
        button = InlineKeyboardButton(text="Назад", callback_data='back_to_categories')
        keyb_subcategories.add(button)
        print(keyb_subcategories)
        return keyb_subcategories

    @staticmethod
    def admin_keyb_main_menu():
        keyb__admin_main_menu = InlineKeyboardMarkup(row_width=2)
        row = []
        for ind, key in enumerate(admin_main_menu_dict.keys()):
            elem = admin_main_menu_dict.get(key)
            buttons = InlineKeyboardButton(text=elem, callback_data=key)
            row.append(buttons)
            if len(row) == 2:
                keyb__admin_main_menu.row(row[0], row[1])
                row = []
            elif ind == len(admin_main_menu_dict.keys()) - 1:
                keyb__admin_main_menu.row(row[0])
                row = []
        return keyb__admin_main_menu

    @staticmethod
    def price_keyb():
        price_keyboard = InlineKeyboardMarkup(row_width=1)
        for key in price.keys():
            elem = price.get(key)
            price_keyboard.row(InlineKeyboardButton(text=elem, callback_data=key))
        return price_keyboard

    @staticmethod
    def blacklist_keyb():
        keyb = InlineKeyboardMarkup(row = 1)
        for key in blackist.keys():
            elem = blackist.get(key)
            keyb.row(InlineKeyboardButton(text=elem, callback_data=key))
        return keyb

    @staticmethod
    def code_is_false():
        code_keyb = InlineKeyboardMarkup(row_width=2)
        row = []
        for key in code_is_false.keys():
            elem = code_is_false.get(key)
            buttons = InlineKeyboardButton(text=elem, callback_data=key)
            row.append(buttons)
            if len(row) == 2:
                code_keyb.row(row[0], row[1])
                row = []
        return code_keyb

    @staticmethod
    def make_code_keyb():
        make_key_keyb = InlineKeyboardMarkup(row_width=2)
        row = []
        for key in make_code.keys():
            elem = make_code.get(key)
            buttons = InlineKeyboardButton(text=elem, callback_data=key)
            row.append(buttons)
            if len(row) == 2:
                make_key_keyb.row(row[0], row[1])
                row = []
        return make_key_keyb

    @staticmethod
    def generate_code():
        number = random.randint(10 ** 16, 10 ** 17)
        return number

    @staticmethod
    def subscription():
        make_key_keyb = InlineKeyboardMarkup(row_width=2)
        row = []
        for ind, key in enumerate(subscription.keys()):
            elem = subscription.get(key)
            buttons = InlineKeyboardButton(text=elem, callback_data=key)
            row.append(buttons)
            if len(row) == 2:
                make_key_keyb.row(row[0], row[1])
                row = []
            if len(row) == 1 and ind == len(subscription.keys()) - 1:
                make_key_keyb.row(row[0])
        return make_key_keyb

    @staticmethod
    def filters():
        filters_keyb = InlineKeyboardMarkup(row_width=2)
        row = []
        for ind, key in enumerate(filters.keys()):
            elem = filters.get(key)
            buttons = InlineKeyboardButton(text=elem, callback_data=key)
            row.append(buttons)
            if len(row) == 2:
                filters_keyb.row(row[0], row[1])
                row = []
            if len(row) == 1 and ind == len(filters.keys()) - 1:
                filters_keyb.row(row[0])
        return filters_keyb

    @staticmethod
    def check_date(date1, date2=str(datetime.now()).split('.')[0]):
        return date1 > date2

    @staticmethod
    def enter_or_no():
        enter_or_noo = InlineKeyboardMarkup(row_width=2)
        row = []
        for ind, key in enumerate(keyword_or_no.keys()):
            elem = keyword_or_no.get(key)
            buttons = InlineKeyboardButton(text=elem, callback_data=key)
            row.append(buttons)
            if len(row) == 2:
                enter_or_noo.row(row[0], row[1])
                row = []
        return enter_or_noo

    @staticmethod
    def empty_or_no(element):
        if element == '':
            return "Пусто"
        else:
            return element

    @staticmethod
    def get_category(cat):
        try:
            cat = category_dict.get(cat)
        except Exception:
            cat = 'Пусто'
        return cat

    @staticmethod
    def get_subcategory(cat, sub):
        try:
            cat = subcategory.get(cat).get(sub)
        except Exception:
            cat = "Пусто"
        if cat is None:
            cat = "Пусто"
        return cat

    @staticmethod
    def filterr(filter):
        print(list(filter))
        if len(filter) == 0:
            return "Пусто"
        else:
            for i in range(len(filter)):
                print(filter[i])
                filter[i] = filters.get(filter[i])
            return filter

    @staticmethod
    def reformat_token_file(file: list):
        for i in range(len(file)):
            file[i] = file[i].replace('\n', '')
        return file

