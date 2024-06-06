import random as rand

seed = rand.randint(0, 1000000)
file_name = "jocdeproves" + str(seed) + ".txt"

n = int(input("Enter the number of exercices: "))

with open(file_name, "w") as file:
    file.write("(define (problem jocdeproves)\n")
    file.write("  (:domain jocdeproves)\n")     #canviar jocdeproves pel nom del domini
    file.write("  (:objects\n")
    
    # Define objects
    for i in range(n):
        file.write("e" + str(i) + " ")
    file.write("- exercici\n")

    file.write(")\n")
    file.write("(:init\n")
    
    # Define initial state
    # precursors

    # preparadors

    # nivell

    file.write(")\n")
    file.write("(:goal\n")

    # Define goal state

    file.write(")\n")