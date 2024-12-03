import json
import os

cadastroGeral = "cadastro.json"

def carregarDadosCadastro():
    if os.path.exists(cadastroGeral):
        try:
            with open(cadastroGeral, "r") as infile:
                json.load(infile)
        except json.JSONDecodeError:
            return []
    return []

def salvarDadosCadastro(dados):
    with open(cadastroGeral, "w") as outfile:
        json.dump(dados, outfile, indent=4)

def criarUsuario():


