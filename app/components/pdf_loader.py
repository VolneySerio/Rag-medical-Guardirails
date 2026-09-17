import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.common.logger import get_logger
from app.common.custom_expection import CustomException

from app.config.config import DATA_PATH, CHUNK_SIZE, CHUNK_OVERLAP


logger = get_logger(__name__)

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


def load_pdf_files():
    try:
        if not os.path.exists(DATA_PATH):
            raise CustomException("Caminho para arquivos não encontrado.")

        logger.info("Caminho validado.")

        loader = DirectoryLoader(DATA_PATH, glob="*.pdf" ,loader_cls=PyPDFLoader)

        documents = loader.load(documents)

        if not documents:
            logger.warning("Falha ao carregar documento.")
        else:
            logger.info(f"{len(documents)} carregados.")

        return documents

    except Exception as e:
        error_menssage = CustomException("Error :", {})
        logger.error(str(error_menssage))
        return []



def create_text_chunks(documents):
    try: 
        if not documents:
            logger.warning("Documentos não encontrados.")

        logger.info("Documentos encontrados.")

        text_spliter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE , )

        text_chunks = text_spliter.split_documents(documents=documents)

        logger.info(f"{len(text_chunks)}Chunks gerados")

        return text_chunks
        
    except Exception as e:
        error_menssage = CustomException("Error :", {})
        logger.error(str(error_menssage))
        return []
