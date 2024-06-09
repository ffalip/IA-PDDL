import random as rand

seed = rand.randint(0, 1000000)
file_name = "joc" + str(seed) + ".pddl"

n = int(input("Enter the number of exercices: "))
mode = input("Enter the mode (B - basic, E1 - extent 1, E2 - exten 2): ")

with open(file_name, "w") as file:
    file.write("(define (problem jocdeproves)\n")
    file.write("\t(:domain domainP)\n")     #canviar jocdeproves pel nom del domini
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

    file.write("\t)\n")
    file.write("(:init\n")
    
    # Define initial state
   
    # preparadors
    # mode basic => màxim un preparador
    if (mode == "B"):
        for i in range(n):
            if (rand.randint(0, 1) == 1):
                id_prep = rand.randint(0, n)
                while id_prep == i: 
                    id_prep = rand.randint(0, n)

                file.write("\t\t(preparador ex" + str(id_prep) + " ex" + str(i) + ")\n")
            else:
                file.write("\t\t(noprep ex" + str(i) + ")\n")
    
    # dies anterior
    for i in range(16):
        file.write("\n")
        for j in range(i):
            file.write("\t\t(dia_abans dia" + str(j) + " dia" + str(i) + ")\n")
    # nivell
    for i in range(10):
        file.write("\t\t(nivell_ant n" + str(i) + " n" + str(i+1) + ")\n")
    # nivel max
    for i in range(n):
        file.write("\t\t(nivell_max ex" + str(i) + " n0)\n")

    file.write("\t)\n")
    file.write("\t(:goal\n")
    file.write("\t\t(and \n")
    # Define goal state
    for i in range(n):
        file.write("\t\t\t(nivell_max ex" + str(i) + " n" +str(rand.randint(1,10)) + ")\n")
    file.write("\t\t)\n")
    file.write("\t)\n")
    file.write(")\n")