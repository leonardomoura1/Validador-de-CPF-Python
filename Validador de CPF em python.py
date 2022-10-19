from tkinter import *


# Este codigo e um Validador de CPF em Python com interface grafica
def todos_numeros_iguais(cpf):
# Função que verifica se todos os números do CPF são iguais.
    i = 0
    while i < len(cpf):
        if cpf[i - 1] != cpf[i]:
            return False
        i += 1
    return True

def recupera_soma(cpf, fator):
    # Esta função serve para auxiliar no cálculo do primeiro é segundo dígito.
    resultado = 0
    for n in cpf[:9]:
        resultado += int(n) * fator
        fator -= 1
    return resultado   

def recupera_primeiro_digito(cpf):
    #Função que verifica o primeiro digito do CPF
    soma = recupera_soma(cpf, 10)
    resultado = (soma * 10) % 11
    if resultado == 10:
        return 0
    return resultado   

def recupera_segundo_digito(cpf, primeiro_digito):
    #Função que verifica o segundo digito do CPF
    soma = recupera_soma(cpf, 11)
    soma += (primeiro_digito * 2)
    resultado = (soma * 10) % 11
    if resultado == 10:
        return 0
    return resultado    

def cpf_valido(cpf):
    #Função que verifica se o CPF é valido
    cpf = cpf.replace('.', '').replace('-', '')
    if len(cpf) != 11 or not cpf.isnumeric() or todos_numeros_iguais(cpf):
        return False
    digito1 = recupera_primeiro_digito(cpf)
    digito2 = recupera_segundo_digito(cpf, digito1)
    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])  

def resposta():
    cpf = cpf_entry.get()
    if cpf_valido(cpf):
        lb = Label(janela, fg=co3, text=" CPF é Válido ")
        lb.grid(column=0, row=2, padx=(230,0), pady=5)
    else:
        lb = Label(janela, fg=co2, text=" CPF Inválido ")
        lb.grid(column=0, row=2, padx=(230,0), pady=5)

def limitar_tamanho(p):
    #Função que limita o tamanho do CPF
    if len(p) > 14:
        return False
    return True
   
################# definindo algumas cores ##############

co0 = "#000000"  # preta
co1 = "#feffff"  # branca
co2 = "#f04141"  # vermelho
co3 = "#59b356"  # verde
co4 = "#0000FF"    # azul

################# Criando Janela principal ##############

janela = Tk()
janela.resizable(0, 0)
janela.title("Validador de CPF em Python")
janela.geometry("600x350")
janela.resizable(False, False)
vcmd = janela.register(func=limitar_tamanho)

lb = Label(janela, text="Validador de CPF")
lb.grid(column=0, row=1, padx=(230,0), pady=(10,5))

lb = Label(janela, text="Digite o CPF")
lb.grid(column=0, row=2, padx=(230,0), pady=5)

cpf_entry = Entry(janela, width=20, validate='key', validatecommand=(vcmd, '%P'))
cpf_entry.grid(row=3, column=0, sticky=NSEW, padx=(230,0), pady=10)

lb = Label(janela, text="exemplo: 000.000.000-00")
lb.grid(column=0, row=4, padx=(230,0), pady=5)

lb = Label(janela, text="exemplo: 00000000000")
lb.grid(column=0, row=5, padx=(230,0), pady=5)

botao_validar = Button(janela, text="Validar", command=resposta)
botao_validar.grid(column=0, row=6, padx=(230,0), pady=20)

botao_sair = Button(janela, text="Sair", command=exit)
botao_sair.grid(column=0, row=7, padx=(230,0))

lb = Label(janela, fg=co4, text="Leonardo de Aguiar de Moura")
lb.grid(column=0, row=8, padx=(230,0), pady=(30,5))

janela.mainloop()