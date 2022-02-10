from aiogram.dispatcher.filters.state import StatesGroup, State


class States(StatesGroup):
    permission_accepted = State()
    # /////////MAIN_MENU///////
    settings = State()
    profile = State()
    # ////////Categories///////
    transport = State()
    # ////////////////////////
    nedvizhimost = State()
    # ////////////////////////
    dom_i_sad = State()
    # ////////////////////////
    zapchasti_dlya_transporta = State()
    # ////////////////////////
    elektronika = State()
    # ////////////////////////
    moda_i_stil = State()
    # ////////////////////////
    zhivotnye = State()
    # ////////////////////////
    detskiy_mir = State()
    # ////////////////////////
    hobbi_otdyh_i_sport = State()
    # ////////////////////////
