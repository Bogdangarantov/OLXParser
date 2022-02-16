keyword_or_no = {'enter': 'Ввести',
                 'no': 'Нет'}
main_menu_dict = {'profile': '👤Профиль',
                  'settings': '⚙️Категории',
                  'parse': '🏁Начать парсинг',
                  'filter': '🔍Фильтр поиска',
                  'subscription': '🛒Подписка'}
admin_main_menu_dict = {'settings': '⚙️Категории',
                        'parse': '🏁Начать парсинг',
                        'filter': '🔍Фильтр поиска',
                        'Make_code': '🎰Сгенерировать код',
                        'add_token': '🎛Добавить токен'}
code_is_false = {'try_again': '✏️Ввести код \nснова',
                 'back_to_menu': '📖Главное меню'}
subscription = {'to_subscribe': '🛒Получить подписку',
                'enter_code': '📝Ввести код',
                'back_to_menu': '🔙Назад'}
filters = {'registration': 'Регистрация',
           'count_of_advert': 'Кол-во обьявлений',
           'black_list_of_words': 'Черный список слов',
           'clear_filters': 'Очистить фильтры',
           'back_to_menu':'Назад'}
category = ['detskiy-mir',
            'nedvizhimost',
            'transport',
            'zapchasti-dlya-transporta',
            'zhivotnye', 'dom-i-sad',
            'elektronika', 'uslugi',
            'moda-i-stil',
            'hobbi-otdyh-i-sport']
make_code = {'one_hour': '1 Час',
             'three_hours': '3 Часа',
             'five_hours': '5 Часов',
             'twelve_hours': '12 Часов',
             'one_day': '1 День',
             'three_days': '3 Дня',
             'Forever': 'Навсегда'}
category_dict = {'transport': '⚙️Авто',
                 'nedvizhimost': '⚙️Недвижимость',
                 'dom-i-sad': '⚙️Дом-сад',
                 'zapchasti-dlya-transporta': '⚙️Запчасти для трансторта',
                 'elektronika': '⚙️Электроника',
                 'moda-i-stil': '⚙️Одежда',
                 'zhivotnye': '⚙️Животные',
                 'detskiy-mir': '⚙️Дети',
                 'hobbi-otdyh-i-sport': '⚙️Спорт'}

subcategory = {
    'transport': {'legkovye-avtomobili': '⚙️Легковые',
                  'spetstehnika': '⚙️Спецтехника',
                  'selhoztehnika': '⚙️Сельхозтехника',
                  'moto': '⚙️Мотоциклы-скутеры',
                  'avtomobili-iz-polshi': '⚙️Авто с Польши',
                  'avtobusy': 'Автобусы',
                  'vodnyy-transport': '⚙️Водный транспорт',
                  'pritsepy-doma-na-kolesah': '⚙️Прицепы , дома на колесах',
                  'vozdushnyy-transport': '⚙️Воздушный транспорт',
                  'drugoy-transport': '⚙️Другой транспорт',
                  'gruzovye-avtomobili': '⚙️Грузовики',
                  'all_category': '❗️Вся категория',
                  'enter_keyword': '✏️Ввести ключ-слово подкатегории'},

    'nedvizhimost': {'posutochno-pochasovo': '⚙️Посуточная аренда',
                     'nedvizhimost-za-rubezhom': '⚙️Недвижимость за рубежом',
                     'komnaty': '⚙️Комнаты',
                     'zemlya': '⚙️Земля',
                     'kommercheskaya-nedvizhimost': '⚙️Комерческая недвижимость',
                     'kwatery-pracownicze': '⚙️Служебные',
                     'doma': '⚙️Дома',
                     'kvartiry/novostroyki': '⚙️Новостройки',
                     'hale-magazyny': '⚙️Склады',
                     'garazhy-parkovki': '⚙️Гаражи, Парковки',
                     'kvartiry': '⚙️Квартиры',
                     'all_category': '❗️Вся категория',
                     'enter_keyword': '✏️Ввести ключ-слово подкатегории'},

    'zapchasti-dlya-transporta': {'avtozapchasti-i-aksessuary': '⚙️Автозапчасти и аксесуары',
                                  'shiny-diski-i-kolesa': '⚙️Шины, диски и колёса',
                                  'zapchasti-dlya-spets-sh-tehniki': '⚙️Запчасти для спец/сх техники',
                                  'motozapchasti-i-aksessuary': '⚙️Мотозапчасти',
                                  'prochie-zapchasti': '⚙️Другие запчасти',
                                  'all_category': '❗️Вся категория',
                                  'enter_keyword': '✏️Ввести ключ-слово подкатегории'},

    'zhivotnye': {'sobaki': '⚙️Собаки',
                  'selskohozyaystvennye-zhivotnye': '⚙️Сельхоз животные',
                  'akvariumnye-rybki': '⚙️Рыбы',
                  'koshki': '⚙️Коты',
                  'ptitsy': '⚙️Птицы',
                  'drugie-zhivotnye': '⚙️Другое',
                  'gryzuny': '⚙️Грызуны',
                  'reptilii': '⚙️Рептилии',
                  'tovary-dlya-zhivotnyh': '⚙️Аксессуары',
                  'all_category': '❗️Вся категория',
                  'enter_keyword': '✏️Ввести ключ-слово подкатегории'},

    'dom-i-sad': {'mebel': 'Мебель',
                  'stroitelstvo-remont': '⚙️Строймат',
                  'sprzet-agd': '⚙️Техника',
                  'kantstovary-rashodnye-materialy': '⚙️Канцтовары',
                  'produkty-pitaniya-napitki': '⚙️Продукты и напитки',
                  'sad-ogorod': '⚙️Сад-огород',
                  'predmety-interera': '⚙️Интерьер',
                  'instrumenty': '⚙️Инструменты',
                  'prochie-tovary-dlya-doma': '⚙️Другое',
                  'all_category': '❗️Вся категория',
                  'enter_keyword': '✏️Ввести ключ-слово подкатегории'},

    'detskiy-mir': {'igrushki': '⚙️Игрушки',
                    'detskaya-odezhda': '⚙️Одежда ',
                    'detskie-kolyaski': '⚙️Коляски',
                    'detskaya-obuv': '⚙️Обувь',
                    'akcesoria-dla-niemowlat': '⚙️Аксуссуары',
                    'detskaya-mebel': '⚙️Мебель',
                    'detskie-avtokresla': '⚙️Авто-Кресла',
                    'prochie-detskie-tovary': '⚙️Другое',
                    'all_category': '❗️Вся категория',
                    'enter_keyword': '✏️Ввести ключ-слово подкатегории'},

    'elektronika': {'telefony-i-aksesuary': '⚙️Телефоны',
                    'planshety-el-knigi-i-aksessuary': '⚙️Планшеты',
                    'foto-video': '⚙️Фото',
                    'aksessuary-i-komplektuyuschie': '⚙️Аксессуары',
                    'tehnika-dlya-doma': '⚙️Техника для дома',
                    'audiotehnika': '⚙️Аудиотехника',
                    'kompyutery-i-komplektuyuschie': '⚙️Компьютеры',
                    'igry-i-igrovye-pristavki': '⚙️Игровые приставки',
                    'prochaja-electronika': '⚙️Другое',
                    'tehnika-dlya-kuhni': '⚙️Техника для кухни',
                    'noutbuki-i-aksesuary': '⚙️Ноутбуки',
                    'klimaticheskoe-oborudovanie': '⚙️Климатическое оборудование',
                    'individualnyy-uhod': '⚙️Индивидуальный уход',
                    'tv-videotehnika': '⚙️Телевизоры/Видеотехника',
                    'all_category': '❗️Вся категория',
                    'enter_keyword': '✏️Ввести ключ-слово подкатегории'},

    'moda-i-stil': {'odezhda': '⚙️Одежда',
                    'dlya-svadby': '⚙️Для свадьбы',
                    'naruchnye-chasy': '⚙️Наруные часы',
                    'podarki': '⚙️Подарки',
                    'aksessuary': '⚙️Аксесуары',
                    'krasota-zdorove': '⚙️Косметика',
                    'moda-raznoe': '⚙️Мода разное',
                    'all_category': '❗️Вся категория',
                    'enter_keyword': '✏️Ввести ключ-слово подкатегории'},

    'hobbi-otdyh-i-sport': {'muzykalnye-instrumenty': '⚙️Музыкальные инструменты',
                            'sport-otdyh': '⚙️Спорт отдых',
                            'drugoe': '⚙️Другое',
                            'antikvariat-kollektsii': '⚙️Колекции',
                            'knigi-zhurnaly': '⚙️Книги',
                            'cd-dvd-plastinki': '⚙️Пластинки/Касеты/Диски',
                            'bilety': '⚙️Билеты',
                            'poisk-poputchikov': '⚙️Поиск попутчиков',
                            'poisk-grupp-muzykantov': '⚙️Поиск групп/Музыкантов',
                            'all_category': '❗️Вся категория',
                            'enter_keyword': '✏️Ввести ключ-слово подкатегории'}}
