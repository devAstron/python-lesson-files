# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:47:46 2023

@author: Bahodir
# """
# def toliq_ism_yasa(ism, familya, sharif = ''):
#     """To`liq ism qaytaruvchi funksiya"""
#     if sharif:
#         toliq_ism = f"{ism.title()} {familya.title()} {sharif.title()}"
#     else:
#         toliq_ism = f"{ism.title()} {familya.title()}"
#     print(toliq_ism)
# ism = input("Ismingizni kiriting: ")
# familya = input(f"{ism.title()} familyangiz nima: " )
# sharif = input(f"{ism.title()} {familya.title()} sharifingizni yozing: ")
# toliq_ism_yasa(ism, familya, sharif)
# def oraliq(a, b):
#     """a dan b oraliqqacha bo`lgan sonlarni qaytaradi"""
#     sonlar = [ ]
#     while a < b:
#         sonlar.append(a)
#         a+=qadam
#     for son in sonlar:
#         print(f"{ son }"  , end=" ")
# a = int(input("a sonni kiriting: "))
# b = int(input("b sonni kiriting: "))
# qadam = int(input("Qadamni kiriting:"))

# if a > b:
    
#     print("Oraliq notog`ri kiritilgan(a>b bo`lishi kerak)")
# else:
#     oraliq(a, b)
# oraliq(a, b)        

# def avto_info(kompaniya, model, rang, karobka, yil, narx):
#     avto = {
#             'kompaniya':'kompaniya',
#             'model':'model',
#             'rang': 'rang',
#             'yil':'yil',
#             'karobka':'karobka',
#             'narx':'narx'
#             }
#     return avto
# print('Saytdagi avtomoshinalar ro`yxatini shakllantiramiz: ')
# avtolar = [ ]
# while True:
#     print("Maluimotlarni kiriting: ")
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Avtomobil modeli: ")
#     rang = input("Avtomobil rangi: ")
#     karobka = input("Karobka turi: ")
#     yil = input("Ishlab chiqarilgan yili: ")
#     narx = input("Narxi: ")
#     avtolar.append[avto_info(kompaniya, model, rang, karobka, yil, narx])
#     target = input("Yana avtomobil qo`shilsinmi (yes/no):  ")
#     if target == "no":
#         break
#  print("salonimizdagi avtomashinalar: ")
# for avto in avtolar:
#     if avto['narx']:
#         narx = avto['narx']
#     else: 
#         narx = "Belgilanmagan"
#     print(f"Kompaniya: {avto['kompaniya'].title()} Model: {avto['model'].title()} Rangi: {avto['rang']}.title() Yili: {avto['yil']} Karobka turi: {avto['karobka'].title()} Narxi: {avto['narx']}")
        
        
# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi 
# funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
# def for_user(name, surname, birth_date, place_of_birth, mail = '', phone_number = ''):
#     user = [ ]       
#     user.append(name)
#     user.append(surname)
#     user.append(birth_date)
#     user.append(place_of_birth)
#     user.append(mail)
#     user.append(phone_number)
#     for user_data in user:
#         print(f"User name: {user_data.title()}")
#         print(f"User surname: {user_data.title()}")
#         print(f"User date of birth: {user_data}")
#         print(f"User place of birth: {user_data.title()}")
#         print(f"User mail adress: {user_data}")
#         print(f"User phone number: {user_data}")
    
# name = input("Enter your name \n>>>")
# surname = input("Please enter your surname \n>>>")
# birth_date = input("Enteryour date of birth \n>>>")
# place_of_birth = input("Enter your place of birth \n>>>")
# request1 = input("Do you want add email? (yes or no)\n>>>")
# if request1 != 'no' or request1 != 'No':
#     mail = input('Your email adress \n>>>')
# request2 =  input("Do you want add phone number? (yes or no)\n>>>")
# if request2!= 'no' or request2 != 'No':
#     phone_number = input("Enter your phone number \n>>>")
# for_user(name, surname, birth_date, place_of_birth)
# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
# def protector(a, b,c):
#   if a > b and a > c:
#       print(f"{a}, {b}, {c} sonlar orasida {a} eng kattasi")
#   if b> a and b > c:
#       print(f"{a}, {b}, {c} sonlar orasida {b} eng kattasi")
#   if c > a and c > b:
#       print(f"{a}, {b}, {c} sonlar orasida {c} eng kattasi")
           

# a =int(input("a ni kiriting\n>>>"))
# b =int(input("b ni kiriting\n>>>"))
# c =int(input("c ni kiriting\n>>>"))
# protector(a, b, c)
# Berilgan oraliqdagi tub sonlar
 # ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
# def tub_sonlar(a, b):
   
#     if a > b:
#         print("Oraliqni noto`g`ri kiritdingiz!!!")
#     else:
#         sonlar = list(range(a, b+1))
#         while True:
#             for son in sonlar:
#                 if son % 1 == 0 and son % son == 0:
#                     print(f"({a},{b}) oraliqdagi tub sonlar: {son} ", end= '')
#                 else:
#                     print(f"({a},{b}) oraliqda birorta ham tub son yo`q")
# print("Salom bu dastur kiritilgan a va b sonlar oralig`idagi tub sonlarni chiqaradi dasturni ishga tushirish uchun a ni kiriting")
# a = int(input('>>>'))
# b = int(input("b ni kiriting \n>>>"))
# tub_sonlar(a, b)
# def tub_sonlar_top(min,max):    
#     tub_sonlar = []    
#     for n in range(min,max+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif(n==2):
#             tub = True
#         else:
#             for x in range(2,n):
#                 if(n%x==0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
                
#     return tub_sonlar

# tub_sonlar_top(1,20)

def aylana(r, PI = 3.141592):
    circle = {
                'Radius': r,
                'Diametr': 2*r,
                'Perimetr': 2*PI*r,
                'Yuza': PI*r**2
        
            }
    print(circle)
    return circle

aylana(10)














