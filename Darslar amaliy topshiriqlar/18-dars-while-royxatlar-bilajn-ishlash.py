# print('do`stlar ro`yxati')
# n = 1
# ismlar = [ ]
# while True :
#         ism = input(f"{n}- do`stingizni kiriting \n>>>")
#         ismlar.append(ism)
#         repeat = input('Yana do`stlaringizni qo`shasiz,i ha\yo`q \n>>>')
#         n +=1
#         if repeat == 'yo`q':
#             break
# print('Do`stlaringiz: ')
# for ism in ismlar:
#     print(ism.title())
# students = ['azizxon', 'sherxon', 'asrorxon', 'temurxon']
# baholangan_talabalar = { }
# while students:
    # talaba = students.pop()
    # baho = input(f"{talaba.title()} ga nechi baho qo`ydingiz: ")
    # print(f"{talaba.title()} {int(baho)} oldi")
    # baholangan_talabalar[talaba] = int(baho)
# buyurtma = [ ]
# target = True
# while target:
#     buyurtma.append(input('Buyurtmangiz: '))
#     nishon = input('Yana buyurtma qilasizmi ha/yo`q \n>>>')
#     if nishon == 'yo`q':
#         target = False
#     continue
# print(f"Sizning buyurtmalaringiz: ")
# for zakaz in buyurtma:
#     print(zakaz.title())
baza = { }
print('Assalomu alaykum qanday mahsulotlarni ro`yxatga kiritamiz: ')
target = True
while target:
    baza.keys().append(input('Mahsulot nomini kiriting \n>>>'))
    baza.values().append(input('Mahsulot narxini kiriting  \n>>>'))
    nishon = input('Yana mahsulot qo`shasizmi? ha/yo`q  \n>>>')
    if nishon == 'yo`q':
        target = False
    continue
print('siz kiritigan mahsulotlar: ')
for mahsulot in baza:
    print(f" { baza.keys().title()   } - { baza.values()  }    ")
        









