# YouTube_Subscription_Search [![](https://img.shields.io/github/license/yuting1214/YouTube_Subscription_Search)](https://github.com/yuting1214/YouTube_Subscription_Search/blob/main/LICENSE)


A system enables semantic search within your personal YouTube subscriptions to efficiently find your desired channels.

![Demonstration](https://github.com/yuting1214/YouTube_Subscription_Search/blob/main/material/demo.gif)

## :arrow_down: Installation

### Clone Repo:
```
git clone https://github.com/yuting1214/YouTube_Subscription_Search.git
```

Virtual Environment (Optional)

### Install Dependencies:
```
pip setuptools wheel
pip install .
```

### API Key

[See detailed instructions](https://github.com/yuting1214/YouTube_Subscription_Search/blob/main/Google_API_key_setup.ipynb)
```
Make sure to place the file youtube_credential.json under the folder of API_key/
```

## :rocket: Quickstart

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
youtube_subscription updatedb
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
   
 - 🔧 **Tool Exploration and Integration**:
   - **LLM Exploration**: Dived deep into various Large Language Models for content completion using platforms like:
     - [OpenAI](https://openai.com/), [Cohere](https://cohere.com/), [Claude](https://claude.ai/)
   - **Embedding Tools**: For text embeddings, relied on both commercial and open-source solutions:
     - **Commercial Vendors**:
       - [OpenAI](https://openai.com/), [Cohere](https://cohere.com/), [Google Vertex AI](https://cloud.google.com/vertex-ai?hl=en)
     - **Open-Source Solutions**:
       - [SBERT](https://www.sbert.net/) (all-MiniLM-L6-v2)
   - **Integration**: Leveraged [LangChain](https://www.langchain.com/) to seamlessly link and combine these tools, ensuring a smooth and integrated workflow.

- 🌱 **Future Development**:
  - Word toward developing an intelligent agent that automatically prioritizes high-quality channels and videos to foster users' life-long learning.
  
---

## Experiment Workflow

Data was collected to assess the proposed search methods. Optimal solutions from these experiments are adopted for the application using personal subscription data.

[See more details.](https://app.heptabase.com/w/47c96d92a26951c8bd074c791fcc59dea53e7fac6b2dbac3a440cab6c389af44)

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

* Rubric for relevance score ([See more details](https://github.com/yuting1214/YouTube_Subscription_Search/blob/main/llm_prompt/llm_chain/llm_judge.py))
* Avg_Rel @ k = Average relevance scores on top k retrieved channels.

Grading examples
```
{
  "query": "A step-by-step makeup tutorial for achieving a natural, everyday look using drugstore products",
  "query_type": "detail_query",
  "channel": "Tati",
  "genre": "Beauty and Fashion",
  "Relevance_Score": 2,
  "Score_explanation: "The channel has a high relevance score because the majority of the video titles are directly related to the search prompt.
                       The videos cover various aspects of makeup, including drugstore products, tutorials, product reviews, comparisons, and recommendations.
                       This provides a comprehensive understanding of achieving a natural, everyday look using drugstore products."
}
```

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

### Key Insights:

1. Open-source embedding methods from [SBERT](https://www.sbert.net/), especially **all-MiniLM-L12-v2**, outperform commercial vendors in our tests. As a result, we've integrated the efficient all-MiniLM-L12-v2 method into our application.
2. The LLM judge not only provides a relevance score that aligns more closely with a user's search intent than simply using genre accuracy but also offers a means to minimize manual tasks, ultimately saving both time and resources.
3. User queries categorized under "general_query" align closely with everyday user usage scenarios. Our proposed models perform exceptionally well for this type of query, suggesting that our experimental results can be seamlessly applied to daily usage.

## Known Issues and Future Resolutions

1. The LLM sometimes still would return something as non-intended format, like non-JSON format 


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


