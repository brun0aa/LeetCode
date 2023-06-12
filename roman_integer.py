class Solution(object):
    def romanToInt(self, s):
       ent = list(s)
       tam = len(ent)
       atual = 0
       anterior = 0
       saida = 0
       for i in range(tam):
           anterior = atual
           if ent[i] == "M":
               atual = 1000
           elif ent[i] == "D":
               atual = 500
           elif ent[i] == "C":
               atual = 100
           elif ent[i] == "L":
               atual = 50 
           elif ent[i] == "X":
               atual = 10
           elif ent[i] == "V":
               atual = 5
           elif ent[i] == "I":
               atual = 1
           if atual > anterior:
               saida = saida + atual - 2*anterior
           else:
               saida = saida + atual
       return saida