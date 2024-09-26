def capital_indexes(word):
    wordList = []
    for index,i in enumerate(word):
        if i.isupper():
            wordList.append(index)

    return wordList

print(capital_indexes('AmAr'))
print(capital_indexes('AmAr'))
