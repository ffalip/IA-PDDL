import re

def func_sort(str):
    return len(str) 

def process_file(file_path):
    # Llegir el fitxer i obtenir les línies
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    data_dict = {}
    for i in range(1, 16):
        data_dict[f"DIA{i}"] = []
    # Processar cada línia
    for line in lines:
        line = line.strip()
        num = line.split(":")[0]
        day = line.split(":")[1].split()[1]
        exercise = line.split(":")[1].split()[2]
        level = line.split(":")[1].split()[3]
        
        
        
        data_dict[day].append((num, exercise, level))
    
    for day in sorted(data_dict.keys(), key=func_sort):
        print(f"{day}:")
        for item in sorted(data_dict[day], key=lambda x: int(x[0])):
            print(f"  {item[0]}: {item[1]} {item[2]}")
    
file_path = 'result.txt'
process_file(file_path)

