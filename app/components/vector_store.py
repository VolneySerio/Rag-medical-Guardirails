from langchain_community.vectorstores import FAISS

from app.components.embeddings import get_embedding_model

from app.common.logger import get_logger
from app.common.custom_expection import CustomException

from app.config.config import DB_FAISS_PATH


def load_vector_store():
    #tentar
        #puxar o embedding model

        #Se existir o path do db
            #retornar o Fais.load_local(path, o modelo e autorizar umas paradas doidas de perigo)
        #Se não
            #Loggar informação
    #excep
    # Mensagem de error
    return

def save_vector_store(text_chunkss):
    #tentar
        #checar se existe o text_chunks
        #Subir o error
    #loggar se der certo
    # modelo embedding
    #banco de dados FAIIS.from documents
    #loggar informação salva no banco
    #retornar DB
    #excep 
        #mensagem de error
    return 