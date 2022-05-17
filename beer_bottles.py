word = "bottles"

for beer_num in range(99, 0, -1):
    print(beer_num, word, "of beer on the wall.")  # Печатает текущее кол-во пива
    print(beer_num, word, "of beer.")  # Печатает кол-во пива
    print("Take one down.")  # Просит взять бутылочку пива
    print("Pass it around.")  # Просит выпить бутылочку пива

    if beer_num == 1:  # Последняя ли бутылка осталась?
        print("No more bottles of beer on the wall.")  # Печатает, что пива нет
    else:  # Пиво еще есть
        new_num = beer_num - 1  # Кол-во пива за минусом выпитой бутылки
        if new_num == 1:  # Если осталась последняя бутылка пива
            word = "bottle"  # Бутылки -> Бутылка
        print(new_num, word, "of beer on the wall.")  # Печать кол-ва оставшегося пива

    print()  # Отступ
