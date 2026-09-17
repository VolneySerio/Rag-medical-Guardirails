from langchain_huggingface import HuggingFaceEmbeddings

from app.common.logger import get_logger
from app.common.custom_expection import CustomException

logger = get_logger(__name__)


# Arranjar embedding model
    #Tentar 
        # loggar a inicialização
        # instancia o modelo. (Selecionar modelo)
        # Logga o loading do modelo
        # retorna o modelo

    #exception handler

def get_embedding_model():
    return 