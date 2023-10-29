# YouTube_Subscription_Search

A system enables semantic search within your personal YouTube subscriptions to efficiently find your desired channels.

![Demonstration](https://github.com/yuting1214/YouTube_Subscription_Search/blob/main/material/demo.gif)

## :arrow_down: Installation

Virtual Environment (Optional)

### Install Dependencies:
```
pip install -U pip setuptools wheel
pip install .
```

### API Key

[See detailed instructions](https://github.com/yuting1214/YouTube_Subscription_Search/Google_API_key_setup.ipynb)
```
Make sure to place the file youtube_credential.json under the folder of API_key/
```

## :rocket: Quickstart
After clone, run

1. Create your personal Database
```
youtube_subscription createdb
```

2. Render front-end App
```
youtube_subscription runapp
```

3. Update Database when adding new subscription
```
youtube_subscription update_db
```

## 🎯 Purpose of the Project:

- 📺 **Channel Management**
  - Streamline and enhance the experience of managing subscribed YouTube channels.
  
- 🤖 **Advanced Modelling Techniques**
  - Leverage state-of-the-art Language Learning Models (LLMs), embedding techniques, and vector storage methods to improve system functionality.
  
- ⚖️ **Automated Judging Mechanism**
 - Introduce an LLM-based judge as an alternative to traditional human judgment processes. This method is designed to more accurately gauge relevance related to user intentions, leading to significant reductions in labor costs.
  
- 🔍 **Information Retrieval Enhancement**
  - Harness advanced IR techniques, including:
    - Specialized search algorithms tailored for rich content discovery.
    - Integration of LLMs to bolster the overall project development and refine user queries.
   
 - 🔍 **Tool Exploration and Integration**:
  - **LLM Exploration**: Dived deep into various Large Language Models for content completion using platforms like:
    - OpenAI, Cohere, Claude
  - **Embedding Tools**: For text embeddings, relied on both commercial and open-source solutions:
    - **Commercial Vendors**:
      - OpenAI, Cohere, Google Vertex AI
    - **Open-Source Solutions**:
      - SBERT (all-MiniLM-L6-v2)
  - **Integration**: Leveraged LangChain to seamlessly link and combine these tools, ensuring a smooth and integrated workflow.


- 🚀 **Future Development**:
  - Serve as an intermediate step toward developing an intelligent agent that automatically prioritizes high-quality videos to foster users' life-long learning.
  
---

## Experiment Workflow

For experiment, we collected data to evaluate the proposed searching methods ; for application, we adpot the optimal solutions from the experiment and your personal subsribed data.

[See more in]()

## Experiment results

### Comparison for Relevance

| Splitting Method | Embedding  Method                                                  | Avg_Rel @ 1 | Avg_Rel @ 3 |
|------------------|--------------------------------------------------------------------|-------------|-------------|
| 256              | all-mpnet-base-v2 (SBERT)                                         | 1.422       | 3.622       |
| 256              | all-MiniLM-L12-v2  (SBERT)                                        | 1.400       | 3.533       |
| 256              | text-embedding-ada-002 (OpenAI)                                   | 1.378       | 3.222       |
| 4500             | text-embedding-ada-002 (OpenAI)                                   | 1.356       | 3.422       |
| 256              | textembedding-gecko-multilingual@latest (Google Vertex AI)       | 1.289       | 3.400       |
| 256              | textembedding-gecko@001 (Google Vertex AI)                        | 1.267       | 3.333       |
| 3000             | textembedding-gecko@001 (Google Vertex AI)                        | 1.267       | 3.422       |
| 256              | embed-english-light-v2.0 (Cohere)                                 | 1.222       | 3.067       |
| 256              | embed-multilingual-v2.0 (Cohere)                                  | 1.156       | 3.200       |

* Rubric for relevance score ([See more details](https://github.com/yuting1214/YouTube_Subscription_Search/blob/main/llm_chain/llm_judge.py))
* Avg_Rel @ k = Average relevance scores on top k retrieved channels.


![Score Distribution for Searching methods](/material/experiment/score_dist.png)
|:--:| 
| Score Distribution for Searching methods |

![Average scores for different types of Queries](/material/experiment/avg_score_query.png)
|:--:| 
| Average scores for different types of Queries |

Query examples
```
# Genre: Vlogging
{
  "general_query": "daily vlogs of people's lives",
  "specific_query": "A day in the life of a travel vlogger exploring Bali",
  "detail_query":  "A daily vlog of a college student's study routine, including tips and tricks for effective studying"
}
```

### Comparison for Accuracy(Genre)

| Splitting Method | Embedding  Method                                                | Accuracy @ 1 |
|------------------|------------------------------------------------------------------|----------|
| 256              | embed-english-light-v2.0 (Cohere)                               | 0.844    |
| 256              | all-mpnet-base-v2 (SBERT)                                       | 0.822    |
| 256              | all-MiniLM-L12-v2  (SBERT)                                      | 0.800    |
| 256              | textembedding-gecko@001 (Google Vertex AI)                      | 0.778    |
| 3000             | textembedding-gecko@001 (Google Vertex AI)                      | 0.778    |
| 256              | text-embedding-ada-002 (OpenAI)                                 | 0.756    |
| 256              | textembedding-gecko-multilingual@latest (Google Vertex AI)     | 0.711     |
| 4500             | text-embedding-ada-002 (OpenAI)                                 | 0.689    |
| 256              | embed-multilingual-v2.0 (Cohere)                                | 0.667    |

* There exists a ground-truth genre for each channel in the experiment.

![Genre Accuracy for Searching methods](/material/experiment/acc_dist.png)
|:--:| 
| Genre Accuracy for Searching methods |

![Average Genre Accuracy for different types of Queries](/material/experiment/avg_acc_query.png)
|:--:| 
| Average Genre Accuracy for different types of Queries |

### Takeaways

1. Open-source embedding methods from [SBERT](https://www.sbert.net/) (all-mpnet-base-v2, all-MiniLM-L12-v2) outperforms the services provided by the commercial vendors in our experiment, therefore, we'll adopt all-MiniLM-L12-v2(more efficent) in our application.
2. The relevance score by LLM judge aligns better with user's searching intention compared to considering only genre accuracy.
3. Adopting the LLM judge to measure relevance could reduce manual labor, saving both time and budget.

# Bug:
The LLM sometimes still would return something as non-intended format, like non-JSON format 


## Acknowledgements
- Special thanks to [Hitesh Kumar Saini](https://github.com/alexmercerind) for [youtube-search-python](https://github.com/alexmercerind/youtube-search-python).

## Reference

### LLM Judge:

* [Best Practices for LLM Evaluation of RAG Applications](https://www.databricks.com/blog/LLM-auto-eval-best-practices-RAG?utm_source=bambu&utm_medium=social&utm_campaign=advocacy&blaid=5053105)

### YouTube Scraping API:

* [YouTube Data API v3 (Official)](https://developers.google.com/youtube/v3/docs)

### YouTube channels:

* [Usual way to find a channel in YouTube](https://support.google.com/youtube/answer/11997749?hl=en&co=GENIE.Platform%3DDesktop&oco=2)
* [How to search Influencers in YouTube](https://www.modash.io/blog/how-to-find-youtube-influencers)
* [10 Most Watched Categories of YouTube Videos](https://mugafi.com/blog/10-most-watched-categories-of-youtube-videos)
* [24 Most Popular Types of YouTube Videos in 2023](https://visme.co/blog/types-of-youtube-videos/)
* [What are the Most Popular Genres on YouTube in 2023?](https://pictory.ai/blog/what-are-the-most-popular-genres-on-youtube-in-2023?el=0035&htrafficsource=pictoryblog&hcategory=video)
* [Top 12 Most Popular Types Of YouTube Videos: List Of Popular Genres To Get The Most Views](https://www.ottawalife.com/article/top-12-most-popular-types-of-youtube-videos-list-of-popular-genres-to-get-the-most-views/)
* [12 Best Types of YouTube Content To Succeed at Growing a YouTube Channel](https://influencermarketinghub.com/types-of-youtube-content/#toc-4)
* [Youtube Commercial Tools](https://www.modash.io/influencer-lookalike-tool)

