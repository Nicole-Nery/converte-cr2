import os
from PIL import Image

# Diretório onde estão os arquivos CR2 ---- Por favor, altere para o seu caminho de diretório!
caminho_diretorio = "Seu/Caminho/Diretorio" 
caminho_diretorio_saida = "Seu/Caminho/DiretorioDeSaida"

# Criando uma lista com os arquivos CR2 presentes no seu diretório
arquivos_cr2 = [arquivo for arquivo in os.listdir(caminho_diretorio) if arquivo.endswith('.CR2')]

# Convertendo arquivos .CR2 em .jpg e fazendo ajustes necessários para as minhas imagens
# Pode ser necessário que você faça outros ajustes ou que não necessite dos que eu fiz para minhas imagens
# Nesse caso, lembre-se de alterar o código
for arquivo in arquivos_cr2:
    caminho_arquivo_cr2 = os.path.join(caminho_diretorio, arquivo)
    nome_arquivo_jpg = os.path.splitext(arquivo)[0] + '.JPG'
    caminho_arquivo_jpg = os.path.join(caminho_diretorio_saida, nome_arquivo_jpg)

    # Fazendo ajustes necessários às minhas imagens, como espelhando e rotacionando em 180° (as imagens estavam de "cabeça para baixo")
    im = Image.open(caminho_arquivo_cr2).convert('RGB').transpose(method=Image.FLIP_LEFT_RIGHT).transpose(method=Image.ROTATE_180).save(caminho_arquivo_jpg)