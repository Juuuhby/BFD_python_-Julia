from fmethod2 import Logistica, LogisticaMarítima, LogisticaTerrestre

def escolher_transporte(meio: Logistica):
    meio.planejar_entrega()

print("--- Opção 1 ---")
meio_navio = LogisticaMarítima()
escolher_transporte(meio_navio)
print("-"*20)

print("--- Opção 2 ---")
meio_caminhao = LogisticaTerrestre()
escolher_transporte(meio_caminhao)
print("-"*20)