import requests
import urllib
# import telebot
import random
import string
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

import asyncio
from threading import Thread
from functools import partial as functools_partial

# def start_loop(loop):
#     try:
#         asyncio.set_event_loop(loop)
#         loop.run_forever()
#     except (KeyboardInterrupt, SystemExit):
#         loop.stop()
#
#
# worker_loop = asyncio.new_event_loop()
# t = Thread(target=start_loop, args=(worker_loop,))
# t.start()

def is_json(myjson):
    return type(myjson) == type({})


def sendMail(receiver, template, required_data):
    templates_data = {}
    templates_data['account_register'] = {'template': 'email/account_register.html',
                                          'subject': 'Потверждение регистрации',
                                          'title': 'Потверждение регистрации'}
    templates_data['account_password_recovery'] = {'template': 'email/account_password_recovery.html',
                                                   'subject': 'Восстановление пароля',
                                                   'title': 'Восстановление пароля'}
    if template == 'noty_products_in_cart':
        templates_data['noty_products_in_cart'] = {'template': 'email/noty_products_in_cart.html',
                                                   'subject': required_data['user']['name']+', Вы хотели сделать заказ на Abad.uz?',
                                                   'title': 'В Вашей корзине есть товары!'}

    html_content = render_to_string(templates_data[template]["template"],
                                    dict(subject=templates_data[template]['subject'], title=templates_data[template]['title'], data=required_data))

    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(templates_data[template]['subject'], text_content, 'Abad <no-reply@abad.uz>', [receiver])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


# def msgTGtouniversal(to, msg, keyboard=None, disable_web_page_preview=False):
#     # bot = telebot.TeleBot("355989935:AAGGHyAYm-YxU650F3zV-BhL0wM9cE654AI")
#     bot = telebot.TeleBot("1203158555:AAE54GGECtPtz71vIqsqTGnz5VTVYRu39o0")
#     try:
#         bot.send_message(to, msg, parse_mode="Markdown", reply_markup=keyboard, disable_web_page_preview=disable_web_page_preview)
#     except:
#         pass


def get_random_code(number):
    N = number
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

def get_random_integer(number):
    N = number
    return ''.join(random.choices(string.digits, k=N))

class EmptyClass(object):
    pass


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def split_str(seq, chunk, skip_tail=False):
    lst = []
    if chunk <= len(seq):
        lst.extend([seq[:chunk]])
        lst.extend(split_str(seq[chunk:], chunk, skip_tail))
    elif not skip_tail and seq:
        lst.extend([seq])
    return lst


_eng_chars = u"~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:^|ZXCVBNM<>?"
_rus_chars = u"ё!^№;%:?йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"
_trans_table_en = dict(zip(_eng_chars, _rus_chars))
_trans_table_ru = dict(zip(_rus_chars, _eng_chars))


def fix_keyboard_ru(s):
    lst = s.split()
    result_list = []
    for l in lst:
        res = u''.join([_trans_table_en.get(c, c) for c in l])
        # res = u''.join([_trans_table_ru.get(c, c) for c in l])
        result_list.append(res)
    return ' '.join(result_list)


def fix_keyboard_en(s):
    lst = s.split()
    result_list = []
    for l in lst:
        res = u''.join([_trans_table_ru.get(c, c) for c in l])
        result_list.append(res)
    return ' '.join(result_list)

def number_to_smilenumber(number):
    N = str(number)
    smiles = [
        "0️⃣",
        "1️⃣",
        "2️⃣",
        "3️⃣",
        "4️⃣",
        "5️⃣",
        "6️⃣",
        "7️⃣",
        "8️⃣",
        "9️⃣",
    ]
    return_str = ""
    for d in range(len(N)):
        return_str += smiles[int(N[d])]

    return return_str