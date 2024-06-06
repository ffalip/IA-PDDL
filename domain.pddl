;Header and description

(define (domain domain_name)

;remove requirements that are not needed
(:requirements :strips :typing :equality :adl :fluents)

(:types ;todo: enumerate types and their hierarchy here
    dia nivell exercici
)

; un-comment following line if constants are needed
;(:constants )

(:predicates ;todo: define predicates here
    (nivell_max ?ex - exercici ?n - nivell)  ;exercici ex te nivell n
    (fet ?dia - dia ?ex - exercici ?n - nivell)       ;exercici ex fet el dia dia amb nivell n
    (nivell_ant ?n - nivell ?n_1 - nivell)        ;exercici ex pot fer-se amb nivell n
    (preparador ?ex - exercici ?ex2 - exercici)       ;exercici ex2 prepara exercici ex
    (noprep ?ex - exercici)                ;exercici ex no requereix preparacio
)   

;n0 <- n1 <- n2 <- n3 <- n4 <- n5 <- n6 <- n7 <- n8 <- n9 <- n10

(:functions ;todo: define numeric functions here
)

;define actions here

(:action entrenar_exercici
    :parameters (?dia - dia ?ex - exercici ?ex2 - exercici ?n - nivell ?n_ant - nivell)
    :precondition (and 
        (not (fet ?dia ?ex ?n))
        (nivell_ant ?n ?n_ant)
        (or (nivell_max ?ex ?n_ant)  (nivell_max ?ex ?n))
        (or (and (preparador ?ex ?ex2) (fet ?dia ?ex2 ~)) (noprep ?ex))
        )
    :effect (and (nivell_max ?ex ?n) (fet ?dia ?ex ?n) (not (nivell_max ?ex ?n_ant)))
)


)