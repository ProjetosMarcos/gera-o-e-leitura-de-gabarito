import random

# Função para gerar um gabarito aleatório com respostas A, B, C ou D para 10 questões
def gerar_gabarito():
    questoes = []
    respostas = ['A', 'B', 'C', 'D']
    
    for i in range(1, 11):
        questao = f'Questão {i}: {random.choice(respostas)}'
        questoes.append(questao)
    
    return questoes

# Função para ler e verificar respostas do aluno comparando com o gabarito
def ler_gabarito(gabarito):
    print("Bem-vindo ao sistema de leitura de gabaritos!")
    print("Por favor, insira suas respostas para as 10 questões (A, B, C ou D):")
    
    respostas_aluno = []
    for i in range(1, 11):
        resposta = input(f"Questão {i}: ").upper()  # Convertendo para maiúsculo para padronizar
        respostas_aluno.append(resposta)
    
    # Comparando respostas com o gabarito
    num_acertos = 0
    for i in range(10):
        if respostas_aluno[i] == gabarito[i][-1]:  # Compara apenas a letra da resposta
            num_acertos += 1
    
    # Mostrando o resultado ao aluno
    print(f"\nVocê acertou {num_acertos} questões de 10.")
    percentual_acertos = (num_acertos / 10) * 100
    print(f"Percentual de acerto: {percentual_acertos:.2f}%")

# Exemplo de uso
if __name__ == "__main__":
    gabarito = gerar_gabarito()
    for questao in gabarito:
        print(questao)
    
    ler_gabarito(gabarito)
