def run():
    squares2 = []

    for i in range(1, 11):
        if i % 3 != 0:
            squares2.append(i**2)
            
    # list comprehension
    #[element for element in iterable if condition]
    """ 
    squares = [i**2 for i in range(1, 11) if i % 3 != 0]
    print(squares)
    i**2 : representa a cada uno de los elementos a poner en la nueva lista
    range(1, 11) : representa a la lista original
    if i % 3 != 0 : representa a la condición que debe cumplir cada elemento de la lista original para ser incluido en la nueva lista
    
    como se lee ? 
    R: para cada i en el rango/lista se guarda si se cumple condicion
    """
    squares = [i**2 for i in range(1, 11) if i % 3 != 0]
    
    print(squares2)  # [1, 4, 16, 25, 49, 64, 100]
    print(squares)  # [1, 4, 16, 25, 49, 64, 100]


if __name__ == "__main__":
    run()