# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 18:07:19 2023

@author: Bahodir
"""
# def bahola(names):
#     rating = {}
#     for name in names:
#         ratio = (input(f"{name.title()} ning bahosini kiriting: "))
#         rating[name] =ratio
        
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# rating = bahola(talabalar)
# print(rating)
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)
# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir 
# matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.
def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()   

ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
print(ismlar)






