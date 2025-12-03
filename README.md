
# Organizador de Arquivos em Python

Pequeno projeto em Python que organiza arquivos de uma pasta em subpastas por tipo  
(imagens, documentos, planilhas, vídeos, compactados, outros).

## Tecnologias usadas

- Python 3
- `pathlib` para trabalhar com caminhos
- `shutil` ou `Path.rename` para mover arquivos
- Dicionário para mapear extensões → categorias

## Conceitos praticados neste projeto

- Manipulação de arquivos e diretórios com `pathlib`
- Automação de processos manuais do dia a dia
- Estruturação de funções e separação de responsabilidades
- Uso de dicionários para mapear extensões → categorias
- Validação de entradas do usuário
- Tratamento de erros e checagens de caminho
- Organização de código e boas práticas
- Fluxo lógico completo: entrada → processamento → saída

## Por que desenvolvi este projeto?

Criei este organizador de arquivos para treinar lógica de programação e manipulação de dados reais no sistema de arquivos.  
O objetivo principal foi transformar um processo manual e repetitivo em uma automação simples, mas útil, reforçando:

- raciocínio lógico,
- modularização,
- manipulação real do sistema operacional,
- e leitura/escrita de arquivos.

Esse projeto foi essencial para consolidar pontos importantes da minha formação como desenvolvedor Python back-end.


## Como o programa funciona

1. O usuário informa o **caminho da pasta de origem**.
2. O programa:
   - valida se o caminho existe e se é realmente uma pasta
   - lista todos os arquivos dessa pasta
   - pega a extensão de cada arquivo (`.suffix`)
   - descobre a categoria a partir da extensão
   - cria a pasta da categoria em `organizados/` (se não existir)
   - move o arquivo para a pasta correta

## Estrutura das funções principais

- `listar_arquivos(pasta)`: retorna uma lista de arquivos da pasta.
- `descobrir_categoria(ext)`: recebe uma extensão (ex: `.jpg`) e devolve a categoria (`"imagens"`, `"documentos"`, etc.).
- `mover_arquivo(arquivo, categoria)`: cria a pasta de destino (se precisar) e move o arquivo.
- `obter_pasta()`: lê o caminho digitado pelo usuário, valida e retorna um `Path` ou `None`.

##  Como executar

1. Clone o repositório ou baixe os arquivos.
2. Instale o Python 3, se ainda não tiver.
3. No terminal, dentro da pasta do projeto, execute:
