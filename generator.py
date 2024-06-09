import random as rand

seed = rand.randint(0, 1000000)
file_name = "joc" + str(seed) + ".pddl"

n = int(input("Enter the number of exercices: "))
mode = input("Enter the mode (B - basic, E1 - extent 1, E2 - exten 2): ")

with open(file_name, "w") as file:
    file.write("(define (problem jocdeproves)\n")
    file.write("\t(:domain domainP1)\n")     #canviar jocdeproves pel nom del domini
    file.write("\t(:objects\n")
    
    # Define objects
    #nivells
    file.write("\t\t")
    for i in range(11):
        file.write("n" + str(i) + " ")
    file.write("- nivell\n")

    #dies
    file.write("\t\t")
    for i in range(16):
        file.write("dia" + str(i) + " ")
    file.write("- dia\n")

    #exercicis
    file.write("\t\t")
    for i in range(n):
        file.write("ex" + str(i) + " ")
    file.write("- exercici\n")

    #quantitat 
    file.write("\t\t")
    for i in range(7):
        file.write("q" + str(i) + " ")
    file.write("- quantitat\n")

    file.write("\t)\n")
    file.write("\t(:init\n")
    
    # Define initial state
   
    # preparadors
    # mode basic => màxim un preparador
    if (mode == "B"):
        for i in range(n):
            if (rand.randint(0, 1) == 1):
                id_prep = rand.randint(0, n-1)
                while id_prep == i: 
                    id_prep = rand.randint(0, n-1)

                file.write("\t\t(preparador ex" + str(id_prep) + " ex" + str(i) + ")\n")
            else:
                file.write("\t\t(noprep ex" + str(i) + ")\n")
    # mode exetensio 1 => entre 0 i n-1 preparadors 
    elif (mode == "E1" or mode == "E2"):
        for i in range(n):
            if (rand.randint(0, 1) == 1):
                prep = list(map(int, input(f"Entre els preparadors de l'exercici e{i}: ").split()))
                for j in prep:
                    file.write("\t\t(preparador ex" + str(j) + " ex" + str(i) + ")\n")
            else:
                file.write("\t\t(noprep ex" + str(i) + ")\n")
    if (mode == "E2"):
        for i in range(n):
            if (rand.randint(0, 1) == 1):
                id_prec = rand.randint(0, n-1)
                while id_prec == i:
                    id_prec = rand.randint(0, n-1)
                file.write("\t\t(precursor ex" + str(id_prec) + " ex" + str(i) + ")\n")
            else:
                file.write("\t\t(noprec ex" + str(i) + ")\n")   

    # dies anterior
    for i in range(16):
        for j in range(i):
            file.write("\t\t(dia_abans dia" + str(j) + " dia" + str(i) + ")\n")
    # nivell
    file.write("\n")
    for i in range(10):
        file.write("\t\t(nivell_ant n" + str(i) + " n" + str(i+1) + ")\n")
    # nivel max
    file.write("\n")
    for i in range(n):
        file.write("\t\t(nivell_max ex" + str(i) + " n0)\n")
    # quant_seg
    file.write("\n")
    for i in range(6):
        file.write("\t\t(quant_seg q"+ str(i)+ " q" + str(i+1) +")\n")
    # quant_ex_fets
    file.write("\n")
    for i in range(16):
        file.write("\t\t(quant_ex_fets dia" + str(i) + " q0)\n")
    
    file.write("\t)\n")
    file.write("\t(:goal\n")
    file.write("\t\t(and \n")
    # Define goal state
    for i in range(n):
        file.write("\t\t\t(nivell_max ex" + str(i) + " n" +str(rand.randint(1,10)) + ")\n")
    file.write("\t\t)\n")
    file.write("\t)\n")
    file.write(")\n")