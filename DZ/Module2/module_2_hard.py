import random
def final_pairs():
    first = random.randint(3,20)
    print(f'Первое число: {first}')
    valid_pairs = []
    for i in range(1,20):
        for j in range(1,20):
            pair_sum = i + j
            if first not in (i,j) and pair_sum != 0 and first % pair_sum == 0:
                valid_pairs.append((i,j))
    return valid_pairs
rezalt = final_pairs()
print(f'Нужный пароль {rezalt}')