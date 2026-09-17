from langchain_community.vectorstores import FAISS

from app.components.embeddings import get_embedding_model

from app.common.logger import get_logger
from app.common.custom_expection import CustomException


def load_vector_store():
    