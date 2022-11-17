def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {
                "firstname": "Facundo", 
                "lastname": "García"
               }

    super_list = [
        {"firstname": "Facundo", "lastname": "García"},
        {"firstname": "Miguel", "lastname": "Rodriguez"},
        {"firstname": "Pablo", "lastname": "Trinidad"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "José", "lastname": "Fernandez"},
    ] # lista de diccionarios

    super_dict = {
        "\nnatural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 3, 0, 1],
        "floating_nums": [1.1, 4.55, 6.43],
    } # diccionario de listas

    for key, value in super_dict.items():
        print(key, ">", value)


if __name__ == '__main__':
    run()
    
""" 
    Output: 
    natural_nums > [1, 2, 3, 4, 5]
    integer_nums > [-1, -2, 3, 0, 1]
    floating_nums > [1.1, 4.55, 6.43]
"""
""" 
En consola
source c:/xampp/htdocs/fer/venv_python/venv/Scripts/activate
source /venv/Scripts/activate
source ./venv/Scripts/activate
ipython
desactivate
venv venv 
 
python -m venv venv
source venv/bin/activate
source venv/Script/activate
pip install -r requirements.txt
pip freeze > requirements.txt
pip install -r requirements.txt
 
"""