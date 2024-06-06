;Header and description

(define (domain domainP)

;remove requirements that are not needed
(:requirements :strips :typing :equality :adl)

(:types ;todo: enumerate types and their hierarchy here
    dia nivell exercici
)

; un-comment following line if constants are needed
;(:constants )

(:predicates ;todo: define predicates here
    (nivell_max ?ex - exercici ?n - nivell)  ;exercici ex te nivell n a dia2
    (fet ?dia - dia ?ex - exercici ?n - nivell)       ;exercici ex fet el dia dia amb nivell n
    (nivell_ant ?n - nivell ?n_1 - nivell)        ;exercici ex pot fer-se amb nivell n
    (preparador ?ex - exercici ?ex2 - exercici)       ;exercici ex2 prepara exercici ex
    (noprep ?ex - exercici)                ;exercici ex no requereix preparacio
    (dia_abans ?dia2 ?dia) ;dia2 va abans que dia 
)   

;n0 <- n1 <- n2 <- n3 <- n4 <- n5 <- n6 <- n7 <- n8 <- n9 <- n10

;(:functions ;todo: define numeric functions here
;)

;define actions here

(:action entrenar_exercici
    :parameters (?dia - dia ?ex - exercici ?n - nivell)
    :precondition (and 
            (not (fet ?dia ?ex ?n))

            (exists (?n_ant - nivell ?dia2 - dia ?ex2 - exercici)
                (and
                    (nivell_ant ?n_ant ?n)
                    (dia_abans ?dia2 ?dia)
                    (or
                        (fet ?dia2 ?ex ?n_ant)
                        (fet ?dia2 ?ex ?n)
                        (= ?n n1)
                    )
                    (or 
                        (noprep ?ex)
                        (and
                            (preparador ?ex2 ?ex)
                            (exists (?nivell - nivell)
                                (fet ?dia ?ex2  ?nivell)
                            )
                        )
                    )
                )
            )
        )
    :effect (and(fet ?dia ?ex ?n) (nivell_max ?ex ?n))


)
)