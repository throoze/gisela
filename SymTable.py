# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# gisela
#
# TAD SymTable para el lenguaje Gisela
# Julio Lopez (06-39821)
# Victor De Ponte (05-38087)
# ------------------------------------------------------------

# El TAD SymTable se hizo pensando en que cada bloque y cada función tendra su tabla por separado 
# la cual hará referencia al bloque o función inmediatamente exterior (osea el cual envuelve al actual)

class SymTable:
    def __init__(self):
        self._table = {}
        
    def insert(self,nombre,tipo,funcion,funcionExt,bloque,bloqueExt): #nombre,tipo,valor,pasaje,bloque,bloqueExt
        if nombre in self._table:
            exito = False
        else:
            self._table[nombre]=[tipo,funcion,funcionExt,bloque,bloqueExt]
            exito = True
        return exito

    def delete(self,nombre):
        if nombre in self._table:
            del self._table[nombre]
        return True

    def update(self,nombre,tipo,funcion,funcionExt,bloque,bloqueExt):
        if not nombre in self._table:
            exito = False
        else:
            self._table[nombre]=[tipo,funcion,funcionExt,bloque,bloqueExt]
            exito = True
        return exito

    def isMember(self,nombre):
        if nombre in self._table:
            return True

    def find(self,nombre):
        if nombre in self._table:
            return self._table[nombre] 
			
