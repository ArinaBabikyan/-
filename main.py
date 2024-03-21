# номер 1
import datetime
with open('songs.csv') as f:
    li = [i.strip().split(';') for i in f.readlines()]
    li[0][0] = 'streams'
    # рассчитаем кол-во прослушиваний по формуле из условия и заменим недостающие данные

    for i in range(1, len(li)):
        date = li[i][-1].split('.')
        if li[i][0] == '0': # проверяем, есть ли пропущенные данные
            t = 10000 * abs((int(str(datetime.date(day=12, month=5, year=2023) -
                             (datetime.date(day=int(date[0]), month=int(date[1]), year=int(date[2])))).split()[0]))) / \
                (len(li[i][1] + li[i][2])) # по формуле просчитываем их
            li[i][0] = t # и изменяем
        if (datetime.date(day=int(date[0]), month=int(date[1]), year=int(date[2])) <= datetime.date(day=1, month=1, year=2002)): # находим соответствие с условием
            print(f'{li[i][2]} - {li[i][1]} - {li[i][0]}') # выдаем ответ
    li1 = sorted(li[1:], key=lambda x: int(x[0]))
# номер 2, продолжим работу в этом файле
    for i in range(1, len(li) - 1): # делаем сортировку
        for j in range(i + 1, len(li)):
            date = li[i][-1].split('.')
            date1 = li[j][-1].split('.')
            if date >= date1:
                li[i], li[j] = li[j], li[i] # меняем местами больший и меньший
    cnt = 1
    for i in li[1:6]: # берем самые ранние пять песен
        print(f"{cnt} {i[2]}, {i[1]}, {i[3]}") # выводим данные
        cnt += 1 # считаем текущий рейтинг

