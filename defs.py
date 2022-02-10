from keyboards_info import *
import json
from datetime import datetime
from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.types import *
from aiogram.utils.markdown import hlink


class Defs():
    def __init__(self):
        return

    def keyb_categories(self):
        keyb_categoriess = InlineKeyboardMarkup(row_width=2)
        row = []
        for ind,key in enumerate(category_dict.keys()):

            elem = category_dict.get(key)
            buttons = InlineKeyboardButton(elem, callback_data=key)
            row.append(buttons)
            if len(row) == 2:
                keyb_categoriess.row(row[0], row[1])
                row = []
            elif ind == len(category_dict.keys())-1:
                keyb_categoriess.row(row[0])
                row = []
        print(keyb_categoriess)
        button = InlineKeyboardButton(text = "Назад", callback_data='back_to_menu')
        keyb_categoriess.add(button)
        return keyb_categoriess

    def main_menu(self):
        keyb_main_menu = InlineKeyboardMarkup(row_width=2)
        row = []
        for key in main_menu_dict.keys():
            elem = main_menu_dict.get(key)
            buttons = InlineKeyboardButton(text = elem, callback_data=key)
            row.append(buttons)
            if len(row) == 2:
                keyb_main_menu.row(row[0], row[1])
                row = []
        print(keyb_main_menu)
        return keyb_main_menu

    def keyb_sub_categories(self, category):
        keyb_subcategories = InlineKeyboardMarkup()
        row = []
        dict_in_subcategories = subcategory.get(category)
        for ind,key in enumerate(dict_in_subcategories.keys()):
            elem = dict_in_subcategories.get(key)
            buttons = InlineKeyboardButton(elem, callback_data=key)
            row.append(buttons)
            if len(row) == 2:
                keyb_subcategories.row(row[0], row[1])
                row = []
            elif ind == len(dict_in_subcategories.keys())-1:
                keyb_subcategories.row(row[0])
                row = []
        button = InlineKeyboardButton(text = "Назад", callback_data='back_to_categories')
        keyb_subcategories.add(button)
        return keyb_subcategories
