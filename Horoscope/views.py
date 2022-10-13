from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

# def leo(request):
#     return HttpResponse('Знак зодиака лев')
#
#
# def scorpio(request):
#     return HttpResponse('Знак зодиака скорпион')

#
# def get_info_about_zodiac_sign(request, sign_zodiac):
#     if sign_zodiac == 'leo':
#         return HttpResponse('Лев 23 июля – 21 августа')
#     elif sign_zodiac == 'scorpio':
#         return HttpResponse('Рак 22 июня – 22 июля')
#     elif sign_zodiac == 'taurus':
#         return HttpResponse('Телец 21 апреля – 21 мая')
#     else:
#         return HttpResponseNotFound(f'Неизвестный знак зодиака - {sign_zodiac} ')
#
dict_zodiac = {
    'aries': '♈	21 марта — 20 апреля	21 марта — 19 апреля	19 апреля — 13 мая',
    'taurus': '♉	21 апреля — 21 мая	20 апреля — 20 мая	14 мая — 19 июня',
    'gemini': '♊	22 мая — 21 июня	21 мая — 20 июня	20 июня — 20 июля',
    'cancer': '♋	22 июня — 22 июля	21 июня — 22 июля	21 июля — 9 августа',
    'leo': '♌	23 июля — 21 августа	23 июля — 22 августа	10 августа — 15 сентября',
    'virgo': '♍	22 августа — 23 сентября	23 августа — 22 сентября	16 сентября — 30 октября',
    'libra': '♎	24 сентября — 23 октября	23 сентября — 22 октября	31 октября — 22 ноября',
    'scorpio': '♏	24 октября — 22 ноября	23 октября — 21 ноября	23 ноября — 29 ноября',
    'sagittarius': '♐	23 ноября — 22 декабря	22 ноября — 21 декабря	18 декабря — 18 января',
    'capricorn': '♑	23 декабря — 20 января	22 декабря — 19 января	19 января — 15 февраля',
    'aquarius': '♒	21 января — 19 февраля	20 января — 18 февраля	16 февраля — 11 марта',
    'pisces': '♓	20 февраля — 20 марта	19 февраля — 20 марта	12 марта — 18 апреля'
}


# def get_info_about_zodiac_sign(request, sign_zodiac: str):
#     description = dict_zodiac.get(sign_zodiac, None)
#     if description:
#         return HttpResponse(description)
#     else:
#         return HttpResponseNotFound(f'Неизвестный знак зодиака - {sign_zodiac} ')

# def get_info_about_zodiac_sign(request, sign_zodiac: str):
#     response = render_to_string('Horoscope/info_zodiac.html')
#     return HttpResponse(response)

def get_info_about_zodiac_sign(request, sign_zodiac: str):
    description = dict_zodiac.get(sign_zodiac)
    zodiacs = list(dict_zodiac)
    data = {
        'description': description,
        'sign': sign_zodiac.title(),
        'zodiacs': zodiacs,
        # 'my_int': 111,
        # 'my_float': 105.2,
        # 'my_list': [],
        # 'my_tuple': (1, 2, 3),
        # 'my_dict': {'name': 'Jack'}
    }
    return render(request, 'Horoscope/info_zodiac.html', context=data)


# def get_info_about_zodiac_sign_by_number(request, sign_zodiac: int):
#     return HttpResponse(f'This is Number {sign_zodiac}')

def get_info_about_zodiac_sign_by_number(request, sign_zodiac: int):
    zodiacs = list(dict_zodiac)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope_name', args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)
    # return HttpResponseRedirect(f'/horoscope/{name_zodiac}')


# def index(request):
#     zodiacs = list(dict_zodiac)
#     li_elements = ''
#     for sign in zodiacs:
#         redirect_path = reverse('horoscope_name', args=[sign])
#         li_elements += f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"
#     response = f'''
#     <ul>
#     {li_elements}
#     </ul>
#     '''
#     return HttpResponse(response)


def index(request):
    zodiacs = list(dict_zodiac)
    contex = {
        'zodiacs': zodiacs,
        'dict_zodiac': dict_zodiac  # если сделать {} – то выведет что словарь пуст
    }
    # li_elements += f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"
    return render(request, 'Horoscope/index.html', context=contex)
