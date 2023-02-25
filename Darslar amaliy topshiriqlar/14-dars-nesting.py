# # -*- coding: utf-8 -*-
# """
# Created on Tue Feb 14 22:02:40 2023

# @author: Bahodir
# """
# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2018,
#         'narh':13000,
#         'km':50000,
#         'korobka':'avtomat'
#         }

# car1 = {
#         'model':'nexia 3',
#         'rang':'qora',
#         'yil':2015,
#         'narh':9000,
#         'km':89000,
#         'korobka':'mexanika'
#         }

# car2 = {
#         'model':'gentra',
#         'rang':'qizil',
#         'yil':2019,
#         'narh':15000,
#         'km':20000,
#         'korobka':'mexanika'
#         }
# # cars = [car0, car1, car2]
# # for car in cars:
# #     print(f"{car['model'].title()}, "
# #           f"{car['rang']} rang, "
# #           f"{car['yil']}-yil, {car['narh']}$")
# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
#     }

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper(), end = ' ')    
      
# man1 = {
#         'name': 'muhammad mustafo sallollohu alayxissalom',
#         'tyil': 571,
#         'shaxar': 'madina'
#         }
# man2 = {
#         'name': 'amir temur',
#         'tyil': '1336',
#         'shaxar': 'qashqadaryo'
        
#         }
# man3 = {
#         'name': 'alisher navoiy',
#         'tyil': '1441',
#         'shaxar': 'hirot'
#         }
# mans = [ man1, man2, man3 ]
# for man in mans:
#     print(f"{ man['name'].title()}, {man['tyil']}- yilda {man['shaxar'].title()}da tug`ilgan")
# shanu = {
#         'serial':'senga oshiqman',
#         'kino': 'spartak 18+',
#         'musiqa': 'ey gul jaloliddin ahmadaliyev'
    
#         }    
# azizxon = {
#             'serial': 'umar ib-xattob',
#             'kino': 'imtihon o`yinlari',
#             'musiqa': 'gulim sardor rahimxon'
#             }
# asror = {
#         'serial': 'afsungar',
#         'kino': 'aqillilar',
#         'musiqa': 'modniylarga doston ergashev'
        
#         }
# friends [shanu, azizxon, asror]
# for choos in friends:
# print( f"{choos['serial'].title }")  
davlatlar = {
    "O'zbekiston": {
        "poytaxt": "Toshkent",
        "hudud": "448,978 km²",
        "aholi_soni": "34,197,400"
    },
    "AQSH": {
        "poytaxt": "Washington, D.C.",
        "hudud": "9,826,630 km²",
        "aholi_soni": "331,449,281"
    },
    "Rossiya": {
        "poytaxt": "Moskva",
        "hudud": "17,098,242 km²",
        "aholi_soni": "144,471,159"
    },
    "Kanada": {
        "poytaxt": "Ottawa",
        "hudud": "9,984,670 km²",
        "aholi_soni": "38,048,738"
    },
    "Fransiya": {
        "poytaxt": "Parij",
        "hudud": "643,801 km²",
        "aholi_soni": "67,408,000"
    }
}

for davlat, malumotlar in davlatlar.items():
    print(f"{davlat} haqida malumotlar: \nPoytaxt: {malumotlar['poytaxt']} \nHudud: {malumotlar['hudud']} \nAholi soni: {malumotlar['aholi_soni]}"
          )



# # Bo'sh lug'at tuzamiz
# sevimli_kinolar = {}

# # Do'stingiz ismini so'raymiz
# ism = input("Ismingiz nima?\n")

# # Do'stingizdan 3 ta sevimli kino-serialni so'raymiz va lug'atga saqlaymiz
# for i in range(3):
#     kinoning_nomi = input(f"{ism}, {i+1}-chi sevimli kino-serialingiz nima?\n")
#     sevimli_kinolar[kinoning_nomi] = True

# # Natijalarni chiqaramiz
# print(f"{ism} ning sevimli kinolari:")
# for kinoning_nomi in sevimli_kinolar:
#     print(f"\t- {kinoning_nomi}")


















       