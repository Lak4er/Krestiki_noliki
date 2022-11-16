



pole=[[" "," "," "],
      [" "," "," "],
      [" "," "," "]
      ]
def pokazatb_pole():
      print(f"  | 0 | 1 | 2 |")
      print(f"0 | {pole[0][0]} | {pole[0][1]} | {pole[0][2]} |")
      print("---------------")
      print(f"1 | {pole[1][0]} | {pole[1][1]} | {pole[1][2]} |")
      print("---------------")
      print(f"2 | {pole[2][0]} | {pole[2][1]} | {pole[2][2]} |")
# pokazatb_pole()

def vvod_hoda():
      while True:
            try:
                  x,y=map(int,input("Введите координаты для хода").split())
                  if 0<=x<=2 and 0<=y<=2:

                        if pole[x][y] == " ":
                              return x, y
                        else:
                              print("Клетка занята, попробуй снова")
                  else:
                        print("Неверные координаты хода")
            except ValueError:
                  print("Ай-Ай Неверно введены координаты хода, попробуйте снова")
# vvod_hoda()

def proverka_win():
      win=[((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
      for hod in win:
            a=hod[0]
            b=hod[1]
            c=hod[2]
            if pole[a[0]][a[1]]==pole[b[0]][b[1]]==pole[c[0]][c[1]]!=" ":
                  pokazatb_pole()
                  print(f"Победа {pole[a[0]][a[1]]}")
                  print(f"Победа {pole[a[0]][a[1]]}")
                  print(f"Победа {pole[a[0]][a[1]]}")
                  return True

      return False

chislo_hodov=0
while True:
      chislo_hodov+=1
      pokazatb_pole()
      if chislo_hodov%2==1:
            print("Ход для крестика")
      else:
            print("Ход для нолика")
      x,y=vvod_hoda()
      if chislo_hodov%2==1:
            pole[x][y]="X"
      else:
            pole[x][y]="O"
      if proverka_win():
            break
      if chislo_hodov==9:
            pokazatb_pole()
            print("Ничья")
            break





