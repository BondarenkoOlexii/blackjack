import random
import time


def write_text(t):
    print()
    for z in t:
        print(z, end='')
        time.sleep(0.1)

karta = {'6':6, '7':7, '8':8,
         '9':9, '10':10, 'Valet':2,
         'Queen':3, 'King':4, 'Tus': 11}

igroku = []


x_player_ochki = 0

def player_cards():
    igroku.clear()
    for card in karta.keys():
        igroku.append(card)
    return igroku

def shuffel_list():
    player_cards()
    random.shuffle(igroku)
    return igroku


chislo_igrokov = int(input("Введіть кількість ігроки"))
chuslo_ochkov = 0
dict_ochkov_igrokov = {0:0}


for igrok_x in range(chislo_igrokov):
    write_text(f"Щас іграє ігрок {igrok_x + 1} \n")
    dict_ochkov_igrokov[igrok_x] = 0
    input_igru = input("More/Pass? (In input write only M or P)")


    while input_igru != 'P':
        shuffel_list()
        x_player_ochki = igroku[0]
        write_text(f"{igroku[0]}\n")
        chuslo_ochkov += karta[x_player_ochki]
        write_text(f'{chuslo_ochkov} - обще количество очков\n')
        igroku.pop(0)
        input_igru = input("More/Pass? (In input write only M or P)")
    if chuslo_ochkov > 21:
        write_text("Ви проиграли набравши більше 21 очка")
        chuslo_ochkov = 0
        input_igru = 'P'
    if chuslo_ochkov < 21:
        dict_ochkov_igrokov[igrok_x] = chuslo_ochkov
        chuslo_ochkov = 0


sorted_by_values_desc = dict(sorted(dict_ochkov_igrokov.items(), key=lambda item: item[1] if item[1] is not None else float('-inf'),  reverse=True))
winner = next(iter(sorted_by_values_desc))

write_text(f'Виграв ігрок {winner + 1}')