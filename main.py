# номер 1
import datetime
with open('songs.csv') as f:
    li = [i.strip().split(';') for i in f.readlines()]
    li[0][0] = 'streams'
    # рассчитаем кол-во прослушиваний по формуле из условия и заменим недостающие данные

    for i in range(1, len(li)):
        date = li[i][-1].split('.')
        if li[i][0] == '0': # проверяем, есть ли пропущенные данные
            t = abs((int(str(datetime.date(day=12, month=5, year=2023) -
                             (datetime.date(day=int(date[0]), month=int(date[1]), year=int(date[2])))).split()[0]))) / \
                (len(li[i][1] + li[i][2])) # по формуле просчитываем их
            li[i][0] = t # и изменяем
        if (datetime.date(day=int(date[0]), month=int(date[1]), year=int(date[2])) <= datetime.date(day=1, month=1, year=2002)): # находим соответствие с условием
            print(f'“{li[i][2]} - {li[i][1]} - {li[i][0]}”.') # выдаем ответ

