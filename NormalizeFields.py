# -*- coding: utf-8 -*-
__author__ = 'Nurzhanov Edward'

LEN_SNILS = 11
LEN_PASSPORT_NOMER = 6
LEN_INDEX_NOMER = 6
LEN_PASSPORT_COD = 6
EAST_GENDER = ['кызы', 'оглы']

########################################################################################################################
# НУЛЕВЫЕ ЗНАЧЕНИЯ
NULL_VALUE = '\\N'  # НУЛЕВОЕ ЗНАЧЕНИЕ В ФАЙЛЕ
NEW_NULL_VALUE = ''  # НОВОЕ НУЛЕВОЕ ЗНАЧЕНИЕ

NEW_NULL_VALUE_FOR_DATE = '11.11.1111'
NEW_NULL_VALUE_FOR_SERIYA_PASSPORTA = '11 11'
NEW_NULL_VALUE_FOR_NOMER_PASSPORTA = '111111'
NEW_NULL_VALUE_FOR_COD_PASSPORTA = '111-111'
NEW_NULL_VALUE_FOR_GENDER = '0'
NEW_NULL_VALUE_FOR_INDEX = '111111'
NEW_NULL_VALUE_FOR_ALL_TEXT = 'заполнить'
NEW_NULL_VALUE_FOR_HOME = 'заполнить'
########################################################################################################################
# ЗНАЧЕНИЕ ПРИ ОШИБКЕ
ERROR_VALUE = 'ERROR'

########################################################################################################################
# СОКРАЩЕНИЯ ТИПОВ В АДРЕСЕ
DISTRICT_TYPES = ['р-н']

CITY_TYPES = ['г', 'п']

NP_TYPES = ['пгт', 'рп', 'кп', 'к', 'пс', 'сс', 'смн', 'вл', 'дп', 'нп', 'пст', 'ж/д_ст', 'с', 'м',
            'д', 'сл', 'ст', 'ст-ца', 'х', 'рзд', 'у', 'клх', 'свх', 'зим', 'мкр']

STREET_TYPES = ['аллея', 'бульвар', 'б-р', 'в/ч', 'городок', 'гск', 'кв-л', 'линия', 'наб', 'пер', 'переезд', 'пл',
                'пр-кт', 'проезд', 'тер', 'туп', 'ул', 'ш', ]

HOUSE_CUT_NAME = ['дом', 'д.', 'д']
CORPUS_CUT_NAME = ['корпус', 'корп', ]
APARTMENT_CUT_NAME = ['кв']
########################################################################################################################
# ЗНАЧЕНИЕ В ПОЛЕ "ПОЛ" В ИСХОДНОМ ФАЙЛЕ
FEMALE_GENDER_VALUE = '1'
MALE_GENDER_VALUE = '0'

########################################################################################################################
# ИМЕНА ДЛЯ КЛЮЧЕЙ СЛОВАРЕЙ И ДЛЯ ПОРЯДКА ВЫВОД СЛОВАРЯ

FULL_ADRESS_LABELS = ['Индекс', 'Регион', 'Тип_региона', 'Район', 'Тип_района', 'Город', 'Тип_города',
                      'Населенный_пункт', 'Тип_населенного_пункта', 'Улица', 'Тип_улицы', 'Дом', 'Корпус', 'Квартира']

PASSPORT_LABELS = ['Серия', 'Номер', 'Дата_выдачи', 'Кем_выдан', 'Код_подразделения']

FIO_LABELS = ['Фамилия', 'Имя', 'Отчество']

BIRTH_PLACE_LABELS = ['Страна', 'Область', 'Район', 'Город']
########################################################################################################################

import string
import re


class BaseClass:

    def __setattr__(self, name, value):
        if isinstance(value, (int, str)):
            self.__dict__[name] = str(value).strip()
        else:
            self.__dict__[name] = value


def normalize(*args):
    result = []
    for arg in args:
        if arg == NULL_VALUE:
            result.append(NEW_NULL_VALUE)
        else:
            result.append(str(arg).strip())
    return result


def normalize_snils(snils):
    snils = str(snils).strip()
    snilsX = ''
    if snils != NULL_VALUE and snils != '' and isinstance(snils, str):
        try:
            for cc in snils:
                if cc in string.digits:
                    snilsX = snilsX+cc
                else:
                    raise TypeError
            if len(snilsX) < LEN_SNILS:
                snilsX = '0' * (LEN_SNILS - len(snilsX)) + snilsX
            elif len(snilsX) == LEN_SNILS:
                pass
            else:
                return ERROR_VALUE
            return snilsX
        except TypeError:
            return ERROR_VALUE
    else:
        return ERROR_VALUE

def normalize_float(my_float):
    my_float = str(my_float).strip()
    x_float = ''
    if my_float != NULL_VALUE and my_float != '' and isinstance(my_float, str):
        for cc in my_float:
            if (cc in string.digits) or cc == '.':
                x_float = x_float + cc
            elif cc == ',':
                cc = '.'
                x_float = x_float + cc
        return x_float
    else:
        return '0'


def field2fio(field):
    if len(field) > 0 and field != NULL_VALUE:
        first_name, second_name, third_name = '', '', ''
        field = field.strip().split(' ')
        for i, word in enumerate(field):
            if i == 0:
                first_name = field[i]
            elif i == 1:
                second_name = field[i]
            else:
                third_name += field[i] + ' '
        if len(third_name) > 0:
            third_name = third_name[:-1]
        return first_name, second_name, third_name
    else:
        return ERROR_VALUE


#class Gender(BaseClass):
#    def __init__(self, third_name='', gender_field_exists=False, gender=''):
#        self.female_gender_value = FEMALE_GENDER_VALUE
#        self.male_gender_value = MALE_GENDER_VALUE
#        self.third_name = str(third_name).strip()
#        self.gender_field_exists = gender_field_exists
#        self.gender = gender.strip()

#    def gender_from_fio(self):
#        if self.third_name == '':
#            return ERROR_VALUE
#        third_name = self.third_name
#        third_name = third_name.split(' ')
#        if len(third_name) == 1:
#            if ''.join(third_name[0][-3:]).lower() == 'вна':
#                gender = '0'
#            elif ''.join(third_name[0][-3:]).lower() == 'вич':
#                gender = '1'
#            else:
#                gender = ERROR_VALUE
#        elif len(third_name) == 2:
#            if third_name[-1].lower() in EAST_GENDER[0]:  # женщина
#                gender = '0'
#            elif third_name[-1].lower() in EAST_GENDER[1]:  # мужчина
#                gender = '1'
#            else:
#                gender = ERROR_VALUE
#        else:
#            gender = ERROR_VALUE
#        return gender

#    def set_gender_value(self, male_value, female_value):
#        self.female_gender_value = female_value.lower()
#        self.male_gender_value = male_value.lower()

#    def get_gender_value(self):
#        return self.female_gender_value, self.male_gender_value

#    def normalize_gender(self):
#        gender = self.gender
#        gender = gender.lower()
#        if gender == self.female_gender_value:
#            return '0'
#        elif gender == self.male_gender_value:
#            return '1'
#        else:
#            return self.gender_from_fio()

#    def get_value(self):
#        if self.gender_field_exists:
#            return self.normalize_gender()
#        else:
#            return self.gender_from_fio()

def normalize_gender(gender):
    gender = str(gender).strip()
    if gender =='':
        return NEW_NULL_VALUE_FOR_GENDER
    elif len(gender) > 1 and (gender[0]!='1' or gender[0]!='0'):
        return NEW_NULL_VALUE_FOR_GENDER
    else:
        if gender[0] == '0':
            return '1'
        else:
            return '0'


def normalize_text(tx):
    tx = str(tx).strip()
    if len(tx) <= 1:
        return NEW_NULL_VALUE_FOR_ALL_TEXT
    else:
        return tx

def normalize_date(date):
    date = str(date)
    result = re.findall(r'\b(\d{4}|\d{2})[\.:-](\d{2})[\.:-](\d{4}|\d{2})\b', date)
    if len(result) > 0:
        if result[0] == NULL_VALUE:
            return NEW_NULL_VALUE_FOR_DATE
        if len(result[0][0]) == 4:
            result[0] = result[0][::-1]
        elif len(result[0][2]) == 2:
            if result[0][2] < 20:
                result[0][2] = '20' + result[0][2]
            elif result[0][2] > 20:
                result[0][2] = '19' + result[0][2]
        return '.'.join(result[0])
    else:
        return NEW_NULL_VALUE_FOR_DATE


# print(normalize_date('01.09.2003'))

# normalize место рождения


class Passport(BaseClass):
    def __init__(self, seriya='', nomer='', date='', who='', cod=''):
        self.seriya = str(seriya).strip()
        self.nomer = str(nomer).strip()
        self.date = normalize_date(date)
        self.who = normalize_text(who)
        self.cod = str(cod).strip()

    def __setattr__(self, name, value):
        if name == 'date':
            self.__dict__[name] = normalize_date(value)
        else:
            if isinstance(value, (int, str)):
                self.__dict__[name] = str(value)
            else:
                self.__dict__[name] = value

    def normalize_seriya(self):
        if self.seriya != NULL_VALUE and self.seriya != '' and isinstance(self.seriya, str):
            try:
                self.seriya = ''.join([char for char in self.seriya if char in string.digits])
                if len(self.seriya) == 3:
                    self.seriya = '0' + self.seriya
                elif len(self.seriya) == 4:
                    pass
                else:
                    return NEW_NULL_VALUE_FOR_SERIYA_PASSPORTA
#                   return ERROR_VALUE
                self.seriya = self.seriya[:2] + ' ' + self.seriya[2:]
                return self.seriya
            except TypeError:
                return NEW_NULL_VALUE_FOR_SERIYA_PASSPORTA
        else:
            return NEW_NULL_VALUE_FOR_SERIYA_PASSPORTA

    def normalize_nomer(self):
        if self.nomer != NULL_VALUE and self.nomer != '' and isinstance(self.seriya, str):
            try:
                self.nomer = ''.join([char for char in self.nomer if char in string.digits])
                if len(self.nomer) < LEN_PASSPORT_NOMER:
                    self.nomer = '0' * (LEN_PASSPORT_NOMER - len(self.nomer)) + self.nomer
                elif len(self.nomer) == LEN_PASSPORT_NOMER:
                    pass
                else:
                    return NEW_NULL_VALUE_FOR_NOMER_PASSPORTA
#                    return ERROR_VALUE
                return self.nomer
            except TypeError:
                return NEW_NULL_VALUE_FOR_NOMER_PASSPORTA
        else:
            return NEW_NULL_VALUE_FOR_NOMER_PASSPORTA


    def normalize_who(self):
        if self.who == NULL_VALUE:
            self.who = NEW_NULL_VALUE
        return self.who

    def normalize_cod(self):
        if self.cod != NULL_VALUE and self.cod != '':
            self.cod = ''.join([char for char in self.cod if char in string.digits])
            if len(self.cod) < LEN_PASSPORT_COD:
                self.cod = '0' * (LEN_PASSPORT_COD - len(self.cod)) + self.cod
            elif len(self.cod) == LEN_PASSPORT_COD:
                pass
            else:
                return NEW_NULL_VALUE_FOR_COD_PASSPORTA
#                return ERROR_VALUE
            self.cod = self.cod[:3] + '-' + self.cod[3:]
            return self.cod
        else:
            return NEW_NULL_VALUE_FOR_COD_PASSPORTA

    def get_values(self):
        return self.normalize_seriya(), self.normalize_nomer(), self.date, self.normalize_who(), self.normalize_cod()


def normalize_index(index):
    index = str(index).strip()
    if index != NULL_VALUE and index != '' and isinstance(index, str):
        try:
            index = ''.join([char for char in index if char in string.digits])
            if len(index) < LEN_INDEX_NOMER:
                index = '0' * (LEN_INDEX_NOMER - len(index)) + index
            elif len(index) == LEN_INDEX_NOMER:
                pass
            else:
                return NEW_NULL_VALUE_FOR_INDEX
#                return ERROR_VALUE
            return index
        except TypeError:
            return NEW_NULL_VALUE_FOR_INDEX
    else:
        return NEW_NULL_VALUE_FOR_INDEX

def normalize_home(tx):
        tx = str(tx).strip()
        numbers = True
        for i in range(len(tx)):
            if tx[i] not in string.digits:
                numbers = False
        if len(tx) < 1:
            return tx
        elif len(tx) > 10:
            return NEW_NULL_VALUE_FOR_HOME
        elif numbers:
            if int(tx) > 1500:
                return NEW_NULL_VALUE_FOR_HOME
        else:
            return tx


#class FullAdress(BaseClass):
#    def __init__(self, field=''):
#        self.field = str(field)
#        self.full_adress = []
#        self.FULL_ADRESS_DICT = {}
#        for label in FULL_ADRESS_LABELS:
#            self.FULL_ADRESS_DICT[label] = ''
#        self.iter_types = [DISTRICT_TYPES, CITY_TYPES, NP_TYPES, STREET_TYPES, HOUSE_CUT_NAME, CORPUS_CUT_NAME, APARTMENT_CUT_NAME]

#    def normalize_adress(self):
#        if len(self.field) != 0 and self.field != NULL_VALUE:
#            self.field = self.field.lower()
#            values = self.field.split(',')
#            for i, word in enumerate(values):
#                n = []
#                word = word.strip()
#                if i == 0:
#                    n = [char for char in word if char in string.digits]
#                    if len(n) != 6:
#                        return ERROR_VALUE
#                    self.FULL_ADRESS_DICT[FULL_ADRESS_LABELS[0]] = ''.join(n)
#                    continue
#                elif i == 1:
#                    self.FULL_ADRESS_DICT[FULL_ADRESS_LABELS[1]] = ' '.join(word.split(' ')[:-1])
#                    self.FULL_ADRESS_DICT[FULL_ADRESS_LABELS[2]] = word.split(' ')[-1]
#                    continue
#                else:
#                    for j, types in enumerate(self.iter_types):
#                        if j < 4:
#                            if word.split(' ')[-1] in types:
#                                self.FULL_ADRESS_DICT[FULL_ADRESS_LABELS[3 + 2 * j]] = ' '.join(word.split(' ')[:-1])
#                                self.FULL_ADRESS_DICT[FULL_ADRESS_LABELS[3 + 2 * j + 1]] = word.split(' ')[-1]
#                        elif j >= 4:
#                            for type in types:
#                                if word.find(type) != (-1):
#                                    word = word.replace(type, '').replace('.', '')
#                                    self.FULL_ADRESS_DICT[FULL_ADRESS_LABELS[11+j-4]] = word
#            return self.FULL_ADRESS_DICT
#        else:
#            if self.field == NULL_VALUE:
#                return NEW_NULL_VALUE
#            else:
#                return ERROR_VALUE

#    def create_output_list(self):
#        if self.field != '':
#            FULL_ADRESS_DICT = self.normalize_adress()
#        for label in FULL_ADRESS_LABELS:
#            self.full_adress.append(self.FULL_ADRESS_DICT[label].upper())
#        return self.full_adress

#    def get_values(self):
#        output_list = []
#        for elem in self.create_output_list():
#            output_list.append(elem.strip())
#        return output_list

#    # def __call__(self, *args, **kwargs):
#    #     return self.create_output_list()


## f = FullAdress('123592, Москва г, строгинский бульвар, д. 26, корпус 2, кв. 425')
## print(f.get_values())


class Phone(BaseClass):
    def __init__(self, tel_mob='', tel_rod='', tel_dom=''):
        self.tel_mob = str(tel_mob).strip()
        self.tel_rod = str(tel_rod).strip()
        self.tel_dom = str(tel_dom).strip()

    def normalize_tel_number(self, tel):
        tel = tel.strip()
        if tel == '' or tel == NULL_VALUE:
            return ERROR_VALUE
        tel = str(tel).strip()
        tel = ''.join([char for char in tel if char in string.digits])
        if len(tel) == 11:
            if tel[0] in ['8', '9']:
                tel = '7' + tel[1:]
        elif len(tel) == 10:
            tel = '7' + tel
        else:
            return ERROR_VALUE
        return tel

    def poryadoc(self, *tels):
        tels = sorted(tels)
#        tels.reverse()
        return list(tels)

    def get_values(self):
        self.tel_mob = self.normalize_tel_number(self.tel_mob)
        self.tel_rod = self.normalize_tel_number(self.tel_rod)
        self.tel_dom = self.normalize_tel_number(self.tel_dom)
#        if self.tel_rod == self.tel_mob:
#            self.tel_rod = ''
#        self.tel_dom = self.normalize_tel_number(self.tel_dom)
#        if self.tel_dom == self.tel_mob or self.tel_dom == self.tel_rod:
#            self.tel_rod = ''
        return self.poryadoc(self.tel_mob, self.tel_rod, self.tel_dom)

# p = Phone()
# p.tel_dom = 89040964007
# p.tel_rod = 89257349331
# p.tel_mob = 'dd'
# print(p.get_values())