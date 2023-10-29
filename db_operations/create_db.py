import os
import torch
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from utilities.filesystem import ensure_directory_exists
from utilities.json_operations import load_json_from_file, json_documentify
from utilities.logger import Logger
from youtube.authentication import get_authenticated_service
from youtube.subscription_operations import get_all_subscriptions
from youtube.channel_operations import create_channel_info_json
from youtube.video_operations import Scrape_video_info

def run():
    # Authenticate YouTube API
    youtube = get_authenticated_service()
    if not youtube:
        raise Exception('Please follow the instruction to set up YouTube API')

    # Ensure data directory exists
    ensure_directory_exists('./data')

    # Check channel_info file
    channel_info_path = './data/channel_info.json'
    channel_info = load_json_from_file(channel_info_path, [])
    if not channel_info:
        subscriptions = get_all_subscriptions(youtube)
        create_channel_info_json(subscriptions)
        channel_info = load_json_from_file(channel_info_path, [])
    print('Channel info is ready!')

    # Check channel_video_info file
    channel_video_path = './data/channel_video_info.json'
    if not os.path.isfile(channel_video_path):
        print('Start collecting video info for each subscribed channel')
        Scrape_video_info(channel_info, num_video=100)
    print('Channel_video_info is ready! /n')

    # Load Embedding model
    model_path = './models/sentence_transformers'
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    model_kwargs = {'device': "cuda" if torch.cuda.is_available() else "cpu"}
    encode_kwargs = {'normalize_embeddings': False}
    embedding_function = HuggingFaceEmbeddings(
        cache_folder = model_path,
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )

    # Check DB
    db_path='./data/vector_db'
    if not os.path.isdir(db_path):
        channel_video = load_json_from_file(channel_video_path, {})
        if not channel_video:
            raise Exception('Error loading channel video data.')

        docs = json_documentify(channel_video)

        # Doc preprocessing
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 256,
            chunk_overlap  = 10,
            length_function = len,
            is_separator_regex = False,
        )
        texts = text_splitter.split_documents(docs)

        # Create vector db
        print('Start creating the VectorDB!')
        vector_db = Chroma.from_documents(
            documents=texts,
            embedding=embedding_function,
            persist_directory=db_path
        )
    else:
        vector_db = Chroma(persist_directory=db_path, embedding_function=embedding_function)
        # Additional DB validation or integrity checks if necessary
    # Update log
    logger = Logger()
    logger.add_log("Create a VectorDB")
    print('Vector DB is ready to use!')

if __name__ == "__main__":
    run()
