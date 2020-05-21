import time
from functools import wraps

# Definindo decorator
def calcula_duracao(funcao):
    @wraps(funcao) # Mantém as props da função passada (Ex.: __name__, __docstring__, etc)
    def wrapper(*args, **kwargs):
        # Calcula o tempo de execução
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()
        
        # Formata a mensagem que será mostrada na tela
        print("[{funcao}] Tempo total de execução: {tempo_total}".format(
            funcao=funcao.__name__, 
            tempo_total=str(tempo_final-tempo_inicial))
        )
    
    return wrapper()

# Decora a função com o decorator
@calcula_duracao
def main():
    for n in range(0, 100000000):
        pass
    
main