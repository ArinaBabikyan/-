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

# номер 3
    a = input()
    while a != "0":
        for i in li[1:]: # ходим по считанному списку и ищем нашего артиста
            if i[1] == a:
                print(f"У {i[1]} найдена песня: {i[2]}")  # как только находим его, то рассказываем пользователю и выходим из цикла
                break
        else:
            print('К сожалению, ничего не удалось найти') # срабатывает если артиста не было найдено
        a = input()
# номер 4
with open('russian_artists.txt', 'w') as f, open('foreign_artists.txt', 'w') as f1:
    letter = 'йцукенгшщзхъёфывапролджэячсмитьбю'# выписали русский алфавит, чтобы осуществлять проверку
    russian_artists = []
    foreign_artists = []
    for i in li[1:]:
        for j in i[1]:
            if j in letter:
                if i[1] not in russian_artists: # проверяем нет ли такого артиста в списке
                    russian_artists.append(i[1]) # создаем список русских артистов если хоть одна буква в имени артиста русская
                break
        else:
            if i[1] not in foreign_artists:
                foreign_artists.append(i[1]) # иначе добавляем имя в список иностранных артистов
    print('Количество российских исполнителей:', len(russian_artists)) # распечатываем по условию ответ, кол-во рос. исполнителей
    print('Количество иностранных исполнителей:', len(foreign_artists)) # кол-во иностранных исполнителей
    for i in russian_artists:
        print(i, file=f) # записываем в файлы имена артистов соответственно
    for i in foreign_artists:
        print(i, file=f1) # записываем в файлы имена артистов соответственно



