from langchain_huggingface import HuggingFaceEmbeddings

from app.common.logger import get_logger
from app.common.custom_expection import CustomException

logger = get_logger(__name__)


# Arranjar embedding model
    #Tentar 
        # loggar a inicialização 
        # instancia o modelo. (Selecionar modelo) - "sentence-transformers/all-MiniLM-L6-v2"
        # Logga o loading do modelo
        # retorna o modelo

    #exception handler

def get_embedding_model():
    try:
        
        logger.info("Buscando embeddings do modelo no Hugging Face")

        model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

        logger.info("Modelo carregado com sucesso")

        return model

    except Exception as e:
        error_msg = CustomException("Error ocorreu enquanto carregava o embedding do modelo : ", e)
        logger.error(str(error_msg))

        raise error_msg

    #return 