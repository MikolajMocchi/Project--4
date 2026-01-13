import random
import os
import time

def numguesser():
    PLAYING = 1
    zakres = int(input("Wprowadz do jakiej liczby chcesz zgadywać: "))
    losowa = random.randint(1,zakres)
    liczba_prob = 0 # Jeśli 3 to przegrywa.
    while (PLAYING == 1):
        if liczba_prob != 3:

            wybor = int(input("Zgadnij liczbę: "))
        
            if wybor == losowa:
                print(f'Zgadłeś ukrytą liczbę! to liczba {losowa}')
                PLAYING = 0
            else:
                liczba_prob += 1
                print(f'pozostało ci prób {3-liczba_prob}')
        else:
            print("Nie udało Ci się zgadnąć")
            PLAYING = 0


def pkn():

    SCORE = 0

    while(True):

        x = random.randint(0,2)

        opcje = ['kamień', 'papier', 'nożyce']

        komputer = opcje[x]

        wybor = input('co wyrzucasz? [kamień, kapier, nożyce]: ')

        if wybor == komputer:
            SCORE -= 1
            print('Remis! -1 punkt')
        elif wybor == 'kamień' and komputer == 'papier':
            SCORE = 0
            print(f'Przegrałeś! Tracisz wszystkie {SCORE} punktów')
        elif wybor == 'nożyce' and komputer == 'kamień':
            SCORE = 0
            print(f'Przegrałeś! Tracisz wszystkie {SCORE} punktów')
        elif wybor == 'papier' and komputer == 'nożyce':
            SCORE = 0
            print(f'Przegrałeś! Tracisz wszystkie {SCORE} punktów')

        else:
            SCORE += 1
            print(f'Wygrałeś! Zyskujesz 1 punkt do puli {SCORE}')
            
def color_text(text, color = 'RED'):
    """
    Take text as string, and color as string, returns colored text, can be used in terminal.
    """
    # BLUE = '\033[94m'
    # CYAN = '\033[96m'
    # GREEN = '\033[92m'
    # ORANGE = '\033[93m'
    # RED = '\033[91m'

    if color == "RED":
        return '\033[91m'+text+'\033[0m'
    
    elif color == "CYAN":
        return '\033[96m'+text+'\033[0m'
    
    elif color == 'BLUE':
        return '\033[94m'+text+'\033[0m'
    
    elif color == 'GREEN':
        return '\033[92m'+text+'\033[0m'
    
    elif color == 'ORANGE':
        return '\033[93m'+text+'\033[0m'
    
print(color_text('mi bombo', 'ORANGE'))

WIDTH = 20
HEIGHT = 10

# startowe pozycje
snake = [(5, 5), (4, 5), (3, 5)]
direction = 'd'

food = (random.randint(0, HEIGHT-1), random.randint(0, WIDTH-1))

Sfood = (random.randint(0, round((HEIGHT-1)/2)), random.randint(0, round((WIDTH-1)/2)))


def render_board(HEIGHT = HEIGHT, WIDTH = WIDTH):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if(y,x) == food:
                print(color_text("@"), end='')
            elif (x,y) in snake:
                print(color_text('#', 'BLUE'))
            else:
                print('', end='')
        print()

wartosc_proc = (random.randint(1, 100))

def Supafut(wartosc_proc, Sfood, proc):
    if wartosc_proc >= proc:
        return(Sfood)
    else:
        pass




def draw():
    os.system("cls" if os.name == "nt" else 'clear')

    render_board()



while True:
    draw()
    print('Sterowanie: w/s/a/d + Enter')

    move = input('Ruch: ').lower()
    if move in ['w', 's','a', 'd']:
        direction = move
    
    head_y, head_x = snake[0]

    if direction == 'a':
        head_y -= 1
    elif direction == 'd':
        head_y += 1
    elif direction == 'w':
        head_x -= 1
    elif direction == 's':
        head_x += 1
    
    new_head = (head_y, head_x)

    # kolizje
    if (
        head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT or
        new_head in snake
    ):
        draw()
        print('GAME OVER!')
        break

    snake.insert(0,new_head)
    
    if new_head == food:
        food = (random.randint(0,HEIGHT-1), random.randint(0, WIDTH-1))
    elif new_head == Sfood:
        Sfood = (random.randint(0, round((HEIGHT-1)/2)), random.randint(0, round((WIDTH-1)/2)))
        
    else:
        snake.pop()

    time.sleep(0.1)



print('>  Mini.Games  <')
print('> Wybierz opcje <')
print('1) Numguesser')
print('2) Papier, Kamień, Nożyce')
print('3) Snake 🥀')
lol = input('Opcjia nr: ')

if lol == '1':
    print(numguesser())

elif lol == '2':
    print(pkn())
elif lol == '3':
    print(draw())