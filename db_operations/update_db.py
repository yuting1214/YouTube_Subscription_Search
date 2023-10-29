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
from youtube.channel_operations import update_channel_info_json
from youtube.video_operations import Scrape_video_info


def run():
    # Authenticate YouTube API
    youtube = get_authenticated_service()
    if not youtube:
        raise Exception('Please follow the instruction to set up YouTube API')

    # Ensure data directory exists
    ensure_directory_exists('./data')

    # Check Diff of channel_info file and Update
    channel_info_path = './data/channel_info.json'
    channel_info = load_json_from_file(channel_info_path, [])
    latest_subscriptions = get_all_subscriptions(youtube)
    latest_subscriptions_key = {channel['snippet']['resourceId']['channelId'] for channel in latest_subscriptions}
    updated_keys = list(latest_subscriptions_key - set(channel_info.keys()))
    if not updated_keys:
        print('There is no new channels added!')
        return None
    update_channel_info_json(latest_subscriptions)
    latest_channel_info = load_json_from_file(channel_info_path, [])
    new_channel_info = {k: v for k, v in latest_channel_info.items() if k in updated_keys}
    print('Channel info is ready!')

    # Update channel_video_info file
    print('Start updating video info for new subscribed channels')
    if new_channel_info:
        Scrape_video_info(new_channel_info, num_video=100)
    print('Channel_video_info is ready!')

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

    # Update DB
    channel_video_path = './data/channel_video_info.json'
    channel_video = load_json_from_file(channel_video_path, {})
    new_channel_video = {k: v for k, v in channel_video.items() if k in updated_keys}

    docs = json_documentify(new_channel_video)
    # Doc preprocessing
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 256,
        chunk_overlap  = 10,
        length_function = len,
        is_separator_regex = False,
    )
    texts = text_splitter.split_documents(docs)

    # Update VectorDB
    db_path='./data/vector_db'
    vector_db = Chroma(persist_directory=db_path, embedding_function=embedding_function)
    vector_db.add_documents(texts)
    # Updaet log
    logger = Logger()
    message = f"Added channels: [{', '.join(updated_keys)}]"
    logger.add_log(message)
    print('Vector DB is finished update!')

if __name__ == "__main__":
    run()
