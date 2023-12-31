# /*
#  * Crea una función que dibuje una espiral como la del ejemplo.
#  * - Únicamente se indica de forma dinámica el tamaño del lado.
#  * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
#  *
#  * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
#  * ════╗
#  * ╔══╗║
#  * ║╔╗║║
#  * ║╚═╝║
#  * ╚═══╝
#  */

'''
Matriz 5 filas x 5 columnas 
(0, 0) (0, 1) (0, 2) (0, 3) (0, 4)
(1, 0) (1, 1) (1, 2) (1, 3) (1, 4)
(2, 0) (2, 1) (2, 2) (2, 3) (2, 4)
(3, 0) (3, 1) (3, 2) (3, 3) (3, 4)
(4, 0) (4, 1) (4, 2) (4, 3) (4, 4)
'''

def draw_spiral(size):

    for row in range(0, size):
        spiral = ""
        horizontal = row == 0
        for col in range(0, size):
            if row + col == size - 1:#diagonal
                spiral += "╗" if col >= row else "╚" #si col >= a row es lado sup derecho, sino inf izq
                horizontal = col < row #no llegué a la diagonal en caso de ser lado sup
            elif row - col == 1 and row < (size / 2):# si voy por la diagonal sup izq
                spiral += "╔"
                horizontal = True
            elif row == col and row >= (size / 2):#diagonal inf derecha
                spiral += "╝"
                horizontal = False
            else: 
                spiral += "═" if horizontal else "║"
        
        print(spiral)


draw_spiral(0)
draw_spiral(1)
draw_spiral(2)
draw_spiral(3)
draw_spiral(5)
draw_spiral(20)
draw_spiral(50)