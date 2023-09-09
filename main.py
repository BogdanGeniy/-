meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЧЕЛ": "Обращение к человеку"
            }
word = input("Введите непонятное слово (большими буквами!): ")
print(meme_dict.keys())



if word in meme_dict.keys():
    print(name_dict[word])
else:
    print('я не знаю такого слова')
