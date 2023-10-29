YouTube_Subscription_Search/
│
├── db_operations/
│   ├── __init__.py
│   ├── create_db.py
│   └── update_db.py
│
├── youtube/
│   ├── __init__.py
│   ├── authentication.py
│   ├── channel_operations.py
│   ├── subscription_operations.py
│   └── video_operations.py
|
├── utilities/
│   ├── __init__.py
│   ├── filesystem.py
│   ├── json_operations.py
│   └── text_processing.py 
│
├── models/  # Pre-trained models
│   └── sentence_transformers/
| 
├── app/ # Front-end streamlit app  
│   └── front_end.py 
|
├── llm_prompt/
│   ├── prompt/
│   └── llm_chain/
|
├── main/
│   ├── __init__.py
|   └── main.py  # The main script to run the project
