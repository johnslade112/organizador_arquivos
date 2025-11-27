
# importando "Path" do pathlib
# ela descobre os caminhos, junta caminhos, verifar se é arquivo/pasta, mover arquivos, criar pasta 
from pathlib import Path

# importando extenções
from extensoes import TIPOS_ARQUIVOS

# import shutil: biblioteca que move arquivos com segurança
import shutil

# pasta onde tem os arquivos bagunçagos, é aqui que vamos pegar os aquivos
PASTA_TESTE  = Path(__file__).parent / "teste"

# é onde vamos criar as pasta orginazadas, Pasta Raiz
PASTA_DESTINO = Path(__file__).parent / "organizados"



# função para listar os arquivos 
# descobrir o que existe
# esse função deve retornar uma lista 
            #.iterdir()- te dá tudo lá dentro 
            #.is_file - se é uma arquivo
def listar_arquivos(pasta: Path):
    arquivo = []
    for item in pasta.iterdir(): # pra cada item na pasta, pega um por um ?
        if (item.is_file()):
            arquivo.append(item)
    # retornando os arquivos listados na pasta teste
    return arquivo

# a função de descobrir a categoria
        # 1- Padronizar a extensão lower()
        # 2- Procurar a extensão em cada lista de TIPOS_ARQUIVOS
        # 3- retornar a categoria certa. se não achar, retorna "outros"
def descobrir_categoria(ext):
    ext_P = ext.lower() # String da extensão, como imagem.PDF. transforma em ".pdf"
    for categoria, lista_ext in TIPOS_ARQUIVOS.items(): # TIPOS_ARQUIVOS: é o que foi importado la encima, importação global 
        if (ext_P in lista_ext):# verifica se a extensão esta na lista 
            return categoria # retornando a categoria
    return "outros" # retornand "outros"


# função para mover arquivo
# recebe arquivo + categoria
  #1 - crio a variavel destino, que é o caminho da lista. 
  #2 - vejo se ele existe, caso não, ele cria a pasta de "organizados"
  #3 - monto o caminho final do arquivo, para dentro da categoria
  #4 - movo o arquivo
def mover_arquivo(arquivo, categoria):
    # variavel de destino
    destino = PASTA_DESTINO / categoria
    # criar a pasta se não existir 
    destino.mkdir(parents=True, exist_ok= True)
    # novo caminho.
    # monta o caminho final do arquivo
    #  pegando só no nome do arquivo
    novo_caminho = destino / arquivo.name
    # move o arquivo 
    arquivo.rename(novo_caminho)
    




# função que pede o usuario a pasta ou o caminho 
def obter_pasta() -> Path | None: #"Path | None:" = se a pasta existir retorna path ou None
    caminho_str = input("Caminho da pasta: ").strip()

    try:
        pasta = Path(caminho_str)
        # se não existir a pasta
        if not pasta.exists():
            print("Pasta não existe, confere o caminho")
            return None
        # se não for pasta 
        if not pasta.is_dir():
            print('Isso não é uma pasta, é um arquivo')
            return None
        # retornando a pasta 
        return pasta
    except Exception as erro:
        print("Erro ao tentar abrir a pasta")
        return None


# código principal 
if __name__ == "__main__":
    pasta_origem = obter_pasta()

    if pasta_origem is None:
        print("Encerrando o programa, erro ao encontrar a pasta  ")
    else:
        arquivos = listar_arquivos(pasta_origem) # usando a função para lista os arquivos
    
        for arquivo in arquivos:
            ext = arquivo.suffix # pega somente a extensão ".pdf"
            categoria = descobrir_categoria(ext)
            mover_arquivo(arquivo, categoria)
            print(f'Movido: {arquivo.name} -> {categoria}' )