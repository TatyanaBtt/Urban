def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
    return same_words
rezalt_1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
rezalt_2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(rezalt_1)
print(rezalt_2)
