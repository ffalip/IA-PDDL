import re

def process_file(file_path):
    # Llegir el fitxer i obtenir les línies
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    data_dict = {}

    # Processar cada línia
    for line in lines:
        num = line.split(":")[0]
        day = line.split(":")[1].split()[1]
        exercise = line.split(":")[1].split()[2]
        level = line.split(":")[1].split()[3]
        
        # Si el dia no existeix en el diccionari, inicialitzar-lo amb una llista buida
        if day not in data_dict:
            data_dict[day] = []
        
        # Afegir la informació a la llista del dia corresponent
        data_dict[day].append((num, exercise, level))
    
    # Imprimir les dades separades per dia i ordenades
    for day in sorted(data_dict.keys()):
        print(f"{day}:")
        for item in sorted(data_dict[day], key=lambda x: int(x[0])):
            print(f"  {item[0]}: {item[1]} {item[2]}")
    
file_path = 'result.txt'
process_file(file_path)

