import random

def get_color(color_number=4):
    # making sure is a number and not a string
    color_number = int(color_number)

    switcher={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    return switcher.get(color_number,"Invalid Color Number")


def get_allStudentColors(): ## se crea la funcion de get_allstudentcolors()

    students_array = []     ## se crea el arreglo students_array donde se       
                            ## guardara el arreglo de el ciclo

    #your loop here
    for i in range(10):      ## para i hasta 10 hace un ciclo de 0 - 10

        random_color_number = random.randint(0,4)   ## aqui en  
                                                    ##random_color_number se le agrega un numero del 0 - 4
        
        color = get_color(random_color_number)      ## el numero aleatorio que 
                                                    ##salio se multiplica con get_color y agarra uno de los del switcher de arriba luego se guarda en color

        students_array.append(color)                ## el color que salio del 
                                                    ##swicher agrega con el metodo append (agregar) al ultimo elemento de la lista

    return students_array   ##     devuelve el resultado al arreglo

print(get_allStudentColors())   ## imprime la funcion



