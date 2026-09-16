import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.common.logger import get_logger
from app.common.custom_expection import CustomException

from app.config.config import DATA_PATH, CHUNK_SITE, CHUNK_OVERLAP


 #load pdf files
    ##tentar
    #fazer checagem
        #subir exce com texto
    #informar se deu certo
    #carregar os dados 
    #instanciar os documentos
    #checar documentos (Condicional talvez?)
    #retornar documentos
    #tratar a exception 
    #devolver mensagem de error
    #colocar no log a mensagem 

 # Criar os chunks RECEBE DOCUMENTOS
    ## tentar 
        #verificar se existe
        #loggar as informacies
        #instaciar o split
        #criar os chuncks usando o split
        #logar acao
        #retuornar chunkcs