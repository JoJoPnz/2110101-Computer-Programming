n = int(input()) #size
m = int(input())
info = []
for i in range(n):
    info.append([e for e in input().split() if e != ''])
    
def win_horizontal(n,m,player): # player is string
    for i in range(n):
        c = 0
        for j in range(n):
            if info[i][j] == player:
                c += 1
            else:
                c = 0

            if c == m:
                return True
    return False

def win_vertical(n,m,player): # player is string
    for j in range(n):
        c = 0
        for i in range(n):
            if info[i][j] == player:
                c += 1
            else:
                c = 0

            if c == m:
                return True
    return False

def win_cross1(n,m,player):
    for i in range(n):
        for j in range(n):
            #start
            row = i
            col = j
            c = 0
            while row+1 <= n and col+1 <= n:
                #00 11 22 33 44 , 01 12 23 34 , 02 13 24, 03,14 , 04
                if info[row][col] == player:
                    c += 1
                else:
                    c = 0
                if c == m:
                    return True
                row += 1
                col += 1
    return False

info_cross2 = info[::-1]
def win_cross2(n,m,player):
    for i in range(n):
        for j in range(n):
            #start
            row = i
            col = j
            c = 0
            while row+1 <= n and col+1 <= n:
                #00 11 22 33 44 , 01 12 23 34 , 02 13 24, 03,14 , 04
                if info_cross2[row][col] == player:
                    c += 1
                else:
                    c = 0
                if c == m:
                    return True
                row += 1
                col += 1
    return False

def player_win(n,m,player):
    return win_horizontal(n,m,player) or win_vertical(n,m,player) or win_cross1(n,m,player) or win_cross2(n,m,player)

def error(info):
    for i in range(n):
        for j in range(n):
            if info[i][j] not in '012':
                return True
    return False

def notover(info):
    for i in range(n):
        for j in range(n):
            if info[i][j] == '0':
                return True
    return False

if ( player_win(n,m,'1') and player_win(n,m,'2') ) or error(info):
    print('ERROR')
elif player_win(n,m,'1'):
    print('1 WIN')
elif player_win(n,m,'2'):
    print('2 WIN')
elif notover(info):
    print('NOT OVER')
else:
    print('DRAW')

#print(win_horizontal(n,m,'1'))
#print(win_horizontal(n,m,'2'))
#print(win_vertical(n,m,'1'))
#print(win_vertical(n,m,'2'))
#print(win_cross1(n,m,'1'))
#print(win_cross2(n,m,'1'))