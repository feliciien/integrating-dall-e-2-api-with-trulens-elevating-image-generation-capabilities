import os
import requests
import streamlit as st
import weaviate
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatVertexAI
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import ConversationSummaryMemory
from langchain.prompts import ChatPromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Weaviate
from trulens_eval import Feedback, Huggingface, Tru, TruChain
from weaviate.embedded import EmbeddedOptions