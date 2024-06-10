;Header and description

(define (domain domainP)

;remove requirements that are not needed
(:requirements :strips :typing :equality :adl)

(:types ;todo: enumerate types and their hierarchy here
    dia nivell exercici quantitat
)

; un-comment following line if constants are needed
;(:constants )

(:predicates ;todo: define predicates here
    (nivell_max ?ex - exercici ?n - nivell)  ;exercici ex te nivell n a dia2
    (fet ?dia - dia ?ex - exercici ?n - nivell)       ;exercici ex fet el dia dia amb nivell n
    (nivell_ant ?n - nivell ?n_1 - nivell)        ;exercici ex pot fer-se amb nivell n
    (preparador ?e2 - exercici ?ex - exercici)       ;exercici ex2 prepara exercici ex
    (noprep ?ex - exercici)                ;exercici ex no requereix preparacio
    (dia_abans ?dia2 ?dia) ;dia2 va abans que dia 
    (prep_fet ?dia - dia ?ex - exercici)
    (precursor ?ex2 - exercici ?ex - exercici)
    (ultim_ex_fet_dia ?dia - dia ?ex - exercici)
    (noprec ?ex - exercici)
    (quant_ex_fets ?dia - dia ?quant - quantitat)
    (quant_seg ?q1 - quantitat ?q2 - quantitat) ;q1 < q2
)   

;n0 <- n1 <- n2 <- n3 <- n4 <- n5 <- n6 <- n7 <- n8 <- n9 <- n10

;(:functions ;todo: define numeric functions here
;)

;define actions here

(:action entrenar_exercici
    :parameters (?dia - dia ?ex - exercici ?n - nivell)
    :precondition (and 
            (not (quant_ex_fets ?dia q6))
            (not (fet ?dia ?ex ?n))
            (exists (?n_ant - nivell ?dia2 - dia)
                (and
                    (nivell_ant ?n_ant ?n)
                    (dia_abans ?dia2 ?dia)
                    (or
                        (fet ?dia2 ?ex ?n_ant)
                        (fet ?dia2 ?ex ?n)
                        (= ?n n1)
                    )

                )
            )
            (or
                (noprep ?ex)
                (forall (?ex2 - exercici)
                    (or
                        (not (preparador ?ex2 ?ex))
                        (and
                            (preparador ?ex2 ?ex)
                            (prep_fet ?dia ?ex2) 
                        )
                    )
                )
            )
            (or
                (noprec ?ex)
                (and
                    (exists (?ex_prec - exercici)
                        (and
                            (precursor ?ex_prec ?ex)
                            (ultim_ex_fet_dia ?dia ?ex_prec) 
                        )
                    )
                )
            )
            
        )

    :effect (and
                (fet ?dia ?ex ?n) 
                (nivell_max ?ex ?n)
                (prep_fet ?dia ?ex) 
                (forall (?ex_prec - exercici)
                    (when (ultim_ex_fet_dia ?dia ?ex_prec)
                    (not (ultim_ex_fet_dia ?dia ?ex_prec)))
                )
                (ultim_ex_fet_dia ?dia ?ex)
                (forall (?q1 - quantitat ?q2 - quantitat)
                    (when(and (quant_ex_fets ?dia ?q1) (quant_seg ?q1 ?q2))
                        (and
                            (not (quant_ex_fets ?dia ?q1))
                            (quant_ex_fets ?dia ?q2)
                        )
                    )
                )
            )

)
)