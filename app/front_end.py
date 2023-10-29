import os
import torch
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
import streamlit as st
from utilities.json_operations import load_json_from_file
from utilities.text_processing import find_most_similar


# Config
about = """
    A system enables semantic search within your personal YouTube subscriptions to efficiently find your desired channels.
"""

st.set_page_config(
    page_title="YouTube_subscription_search",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/yuting1214/Youtube_Subscription_Search',
        'Report a bug': "https://github.com/yuting1214/Youtube_Subscription_Search/issues",
        'About': about
    }
)

# Layout 
container1 = st.container()
## Main page
container1.title("Search subscribed channels in YouTube")
container1.write("""
Simplify your search to swiftly access your favorite subscribed channels.
""")

container2 = st.container()
cols = container2.columns(2)
cols[0].subheader('Subscribed Channel:')
cols[1].subheader('Relevant Videos:')

## Sidebar
### Check Vector DB
db_path='./data/vector_db'
if not os.path.isdir(db_path):
    st.spinner('Create a VectorDB first...')
### Load Embedding model
model_name = "sentence-transformers/all-MiniLM-L6-v2"
model_kwargs = {'device': "cuda" if torch.cuda.is_available() else "cpu"}
encode_kwargs = {'normalize_embeddings': False}
embedding_function = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)
### Load Data
channel_info = load_json_from_file('./data/channel_info.json', [])
channel_video = load_json_from_file('./data/channel_video_info.json', [])
vector_db = Chroma(persist_directory=db_path, embedding_function=embedding_function)

## Sidebar
st.sidebar.header('User Input: 👇')
query = st.sidebar.text_area('Provide a search query.', '')
if st.sidebar.button('Submit'):
    with st.spinner('Processing...'):
        # Channel
        doc = vector_db.similarity_search(query, k=1)[0]
        channel_id = doc.metadata['channel_id']
        channel_link = channel_info[channel_id]['channel_link']
        channel_title = channel_info[channel_id]['channel_title']
        channel_description = channel_info[channel_id]['channel_description']
        image_url = channel_info[channel_id]['channel_thumbnail']
        markdown_string = f"[![Channel]({image_url})]({channel_link})\n\n**{channel_title}**"
        cols[0].markdown(markdown_string)
        ## Channel description
        cols[0].subheader('Description:')
        cols[0].markdown(channel_description)
        # Video
        video_title = find_most_similar(doc.page_content.split("',")[0], channel_video[channel_id]['video']['video_title'])
        video_index = channel_video[channel_id]['video']['video_title'].index(video_title)
        video_id = channel_video[channel_id]['video']['video_id'][video_index]
        video_link = 'https://www.youtube.com/watch?v=' + video_id
        cols[1].video(video_link)
else:
    cols[0].write('Wait for input.')

### Note
st.sidebar.markdown('''
* English language supported currently.
* Multilingual content search is under development.
                    ''')
st.sidebar.markdown('''[GitHub Repo](https://github.com/yuting1214/Youtube_Subscription_Search)''', unsafe_allow_html=True)