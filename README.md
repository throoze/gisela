Universidad Simón Bolivar

Departamento de Computación y Tecnología de la Información

CI-3725 - Traductores e Interpretadores

Autores:

    * Victor De Ponte (05-38087)
    * Julio Lopez (06-39821)


GISELA
================================================================================

Gisela es un lenguaje imperativo inspirado en GCL [[1]](http://en.wikipedia.org/wiki/Guarded_Command_Language), con algunos elementos
adicionales apropiados para los conceptos que deben aprenderse en este curso.

Puede leer la [definición del lenguaje](http://ldc.usb.ve/~07-40983/ci3725/sd2012/definicion.html)
junto con algunos [ajustes posteriores](http://ldc.usb.ve/~07-40983/ci3725/sd2012/actualizacion.html)
que se le hicieron.

El lenguaje Gisela, está especificado por la gramática a continuación, siendo
las precedencias y asociatividades de los operadores, las señaladas en la
definición del lenguaje y en los ajustes, ambos antes mencionados:

    ''' gisela : globaldec main '''

    ''' globaldec : lglobals
                  | lambda
    '''

    ''' lglobals : globals
                 | lglobals globals
    '''

    ''' globals : globvardec
                | procdef
    '''

    ''' globvardec : vardec TkSecuenciador
    '''

    ''' procdef : TkProc TkIdent TkParAbre larg TkParCierra localdec inst
    '''

    ''' larg : lambda
             | args
    '''

    ''' args : arg
             | args TkComa arg '''

    ''' arg : tvar type TkIdent '''

    ''' tvar : TkVar
             | lambda '''

    ''' main : TkLets block '''

    ''' block : TkGo localdec instructions TkOg '''

    ''' instructions : linst
                     | lambda
    '''

    ''' localdec : localvars TkSecuenciador
                 | lambda
    '''

    ''' localvars : vardec
                  | localvars TkSecuenciador vardec
    '''

    ''' vardec : type lid'''

    ''' type : TkChar
             | TkBool
             | TkInt '''

    ''' lid : TkIdent
            | lid TkComa TkIdent '''

    ''' linst : inst
              | linst TkSecuenciador inst
    '''

    ''' inst : simple
             | block
             | selector
             | repeat
    '''

    ''' simple : TkSkip
               | TkAbort
               | TkReturn
               | asign
               | io
               | proc '''

    ''' asign : TkIdent TkAsignacion exp
              | TkIdent TkComa asign TkComa exp '''

    ''' exp : boolexp
            | arexp
            | char '''

    ''' boolexp : TkTrue
                | TkFalse
                | TkIdent
                | boolexp boolop boolexp
                | TkNot boolexp
                | arexp comp arexp
                | char comp char
                | isop char
                | TkParAbre boolexp TkParCierra '''

    ''' boolop : TkXor
               | TkAnd
               | TkOr '''

    ''' comp : TkMayor
             | TkMayorIgual
             | TkMenor
             | TkMenorIgual
             | TkIgual
             | TkDesIgual '''

    ''' arexp : arexp TkSuma arexp
              | arexp TkResta arexp
              | arexp TkProducto arexp
              | arexp TkDiv arexp
              | arexp TkMod arexp
              | arexp TkPotencia arexp
              | TkParAbre arexp TkParCierra
              | TkIdent
              | TkNumero
              | TkOrd char
              | TkResta arexp %prec UMINUS '''

    ''' char : TkChr arexp
             | TkCaracter
             | TkIdent '''

    ''' isop : TkIsup
             | TkIsal
             | TkIsdig
             | TkIsspa '''

    ''' io : TkRead msg TkIdent
           | TkPrint msg TkIdent '''

    ''' msg : TkMsg
            | TkCaracter
            | lambda '''

    ''' proc : TkIdent TkParAbre lexp TkParCierra '''

    ''' lexp : exp
             | lexp TkComa exp '''

    ''' guarded : boolexp TkGuardia inst '''

    ''' lguarded : guarded
                 | lguarded TkPipe guarded '''

    ''' selector : TkIf lguarded TkFi '''

    ''' repeat : TkDo lguarded TkOd '''

    ''' lambda : '''
