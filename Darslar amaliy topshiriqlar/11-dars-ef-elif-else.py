# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 17:54:37 2023

@author: Bahodir
"""
'''--------------------------------------------------------------------------
                    #Amaliy topshiriq 1
k = int(input('Juft son kiriting >>>'))
if k % 2 == 0:
    print('Rahmat')
else:
    print('Suka o\'qishni bilmisanmi juft son kirit dalban')
    ------------------------------------------------------------------------
'''
'''
---------------------------------------------------------------------------
                #Amaliy topshiriq 2
age = int(input('Iltimos, yoshingizni kiriting: >>>'))
narx = 0
if age <= 4 or age>=60:
    narx = 0
elif age <= 18: 
    narx = 10000
else:
    narx = 20000
print(f"Sizga kirish narxi {narx} so\'m")
-------------------------------------------------------------------------
'''
'''
-------------------------------------------------------------------------
                    #Amalioy topshiriq 3
                
a =int(input(' ixtiyoriy 2 ta son kiriting \n1-son >>>'))
b = int(input('2-son >>>')) 
if a == b: print('Ikki son bir biriga teng')
elif a > b: print(' 1-son 2-sonda katta') 
else: print('2-son 1-sondan katta') 
-----------------------------------------------------------------------
'''
'''
mahsulotlar = ['Telefon', 'Kompyuter', 'Aksesuarlar', 'Ko\'zoynak', 'sichqoncha', 'Klaviatura', 'Ish stoli' , 'Televizor', 'Muzlatgich', 'Kir yuvish moshinasi',]
buyurtma= []
buyurtma.append(input('Assalomu alaykum, xush kelibsiz. marhamat buyurtmalaringiz \n1-buyurtma >>>'))
buyurtma.append((input('2-buyurtma >>>')))
buyurtma.append(input('3-buyurtma >>>'))
buyurtma.append(input('4-buyurtma >>>'))
buyurtma.append(input('5-buyurtma >>>'))

for zakaz in buyurtma:
    if zakaz in mahsulotlar: print(f'Bizning do\'konimizda {zakaz} bor')
    else: print(f'Kechirasiz {zakaz} bizning do\'konda yo\'q')
'''
'''

mahsulotlar = ['Telefon', 'Kompyuter', 'Aksesuarlar', 'Ko\'zoynak', 'sichqoncha', 'Klaviatura', 'Ish stoli' , 'Televizor', 'Muzlatgich', 'Kir yuvish moshinasi',]
buyurtma= []
buyurtma.append(input('Assalomu alaykum, xush kelibsiz. marhamat buyurtmalaringiz \n1-buyurtma >>>'))
buyurtma.append((input('2-buyurtma >>>')))
buyurtma.append(input('3-buyurtma >>>'))
buyurtma.append(input('4-buyurtma >>>'))
buyurtma.append(input('5-buyurtma >>>'))
bor_mahsulotlar = []
yoq_mahsulotlar = []

for zakaz in buyurtma:
    if zakaz in mahsulotlar: 
        bor_mahsulotlar.append(zakaz) 
        print(f'Bizning do\'konda {bor_mahsulotlar} bor')
    else: 
        yoq_mahsulotlar.append(zakaz)
        print(f'Bizning do\'konda {yoq_mahsulotlar} yo\'q ekan, kechirasiz ')s
'''
'''
foydalanuvchilar = ['anvarbek', 'sadulla', 'abduvali', 'shamsiddin1254', 'unknown_user']
new_login = input('Assalomu alaykum, iltimos login tanlang \n>>> ')
if new_login.lower() in foydalanuvchilar:
    print(f'Kechirasiz {new_login} avvaldan band qilingan, boshqa login kiriting')
else:
    print(f'Tizimga xush kelibsiz!!! {new_login}')
'''
"""
k = int(input("Assaloimu alaykum butun son kiriting: "))
sonlar = list(range(2,11))
for son1 in sonlar:
    if k % son1 == 0:
        print(f'{k} son {son1} ga bo\'linadi')
    else: print(f'{k} son {son1} bo\'linmaydi')
"""
   

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    