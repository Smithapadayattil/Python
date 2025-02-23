phonebook={"Alan":7865456781,"Bob":5689745621,"Charles":8974561234,"David":456871235,
           "Francis":74108529637,"George":8976564623,"Ethan":8423697812}
# print(phonebook)
# #Adding
# phonebook={"jimmy":5689745213}
# print(phonebook)
# del phonebook["David"]
# print(phonebook)
#update
# phonebook.update({"Bob" :6589635218})
# print
# if "Charles" in phonebook:
#     print("yes")
# else:
#     print("contact doesn't exists")
#sorting my name
alphabetic_order=dict(sorted(phonebook.items()))
for key,value in alphabetic_order.items():
    print(f"{key}:{value}")