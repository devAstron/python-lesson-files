# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 11:46:12 2023

@author: Bahodir
"""
''';
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
ismlar = [] # bo'sh ro'yxat
print(mevalar)
print(narhlar)
print(sonlar)
print(ismlar)
'''
'''
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
print("Birinchi meva: ", mevalar[-1])
print("Ikkinchi meva: ", mevalar[3])
'''
'''
mevalar = ['OlMa', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
print("Birinchi meva: ", mevalar[-1].lower())
print("Ikkinchi meva: ", mevalar[2].title())
'''
'''
narhlar = [12000, 18000, 10900, 22000]
print(narhlar[2] + narhlar[3])
'''
'''
narhlar = [12000, 18000, 10900, 22000]
narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
print(narhlar)
'''
'''
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
mevalar.append("anor") # mevalar ga tarvuz qo'shamiz
mevalar.append("Nok")
mevalar.append("olxo\'ri")
mevalar.append("uzum")
print(mevalar[-3])
print(mevalar)
'''
'''
cars = ['Lacetti', 'Nexia 3', 'Cobalt']
cars.insert(2, 'Malibu') # 1-o'ringa yangi qiymat qo'shamiz
cars.insert(2, 'Trailbazer')
cars.insert(-1, 'Tico')
cars.insert(-2, 'Matiz')
del cars[-1]
del cars[-2]
cars.remove('Tico')
cars.remove('Trailbazer')
print(cars)
'''
'''

ismlar = ['Sherali', 'Azizxon', 'Asror', 'Temur']
print('Salom' +ismlar[0]+ 'Bugun o\'tirmaymizmi')
print('Nima gap ' +ismlar[1])
print('Yaxshimisan bormisan ' +ismlar[2])
'''
'''
sonlar = [1, -2, 0.5, -3.14]

plus = sonlar[0] + sonlar[1]

kptrsh = sonlar[1] * sonlar[2]
print(kptrsh)
blsh = sonlar[-1] / sonlar[2]
sonlar[3] = sonlar[0] + sonlar[3]
print(blsh)
print(plus)
print(sonlar)
 '''
"""
t_shaxslar = ['Imom Buxoriy', "imom at-Termiziy", " Alisher Navoiy", "Amir Temur"]
z_shaslar = ['Stiv Jobs', 'Albert Eynshteyn', 'Kell Nyuport']
print("Men sarkarda sifatida " +t_shaxslar.pop(-1)+ " ni xurmat qilaman")
print("Men amerika yozuvchilaridan " +z_shaslar.pop(-1)+ " ni taniyman")
"""

friends = []
friends.append('Sherali')
friends.append('Asror')
friends.append('Azizxon')
friends.append('Temur')
friends.append('Tohirjon')
friends.append('Diyorbek')
friends.append('Aziz')
friends.append('Mansur')
print(friends)
friends.remove('Mansur')
friends.remove('Diyorbek')
friends.remove('Asror')
friends.insert(-1, 'Sarvar')
friends.insert(0, 'Tommy')
print(friends)

              














