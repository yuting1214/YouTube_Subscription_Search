import json
from typing import Dict, Union, List
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser

class JsonToDict(BaseOutputParser):
    """Parse the output of an LLM call to a Python Dict."""

    def parse(self, text: str) -> Dict:
        """Parse the output of an LLM call."""
        try:
            output = json.loads(text)
        except:
            output = text
        return output

system_template_llm_judge = """
### System Prompt:
Act as an impartial judge and evaluate the relevance of a YouTube channel’s content based on a provided search prompt. Relevance is assessed by the holistic understanding and insights the relevant videos offer regarding the search prompt, focusing not on the quantity but on the quality and comprehensiveness of the relevant videos. You'll be given a `grading_function` which you'll call for each provided search prompt and a list of the channel’s videos to submit your reasoning and score for the relevance.

#### Relevance Measurement:
Relevance is evaluated by examining the depth and breadth of the content provided in the videos relevant to the search prompt within the channel. A channel is considered highly relevant if the pertinent videos collectively offer clarity, cover a broad spectrum of the topic, and provide depth, allowing for a thorough grasp of the concepts.

#### Relevance Grading Rubric:
- **Score 0: No Relevance**
  - **Definition:** The channel has no videos relevant to the search prompt.
  - **Example:**
    - **Search Prompt:** “Easy Recipes and Culinary Tips”
    - **List of Video Titles:** “Exploring Hidden Beaches in Bali”, “The Ultimate Guide to DSLR Photography”, “A Day in My Life: Tokyo Edition”, “The Mysteries of the Universe”, “High-Intensity Interval Training: Full Body Workout”

- **Score 1: Partial Relevance**
  - **Definition:** The channel has some relevant videos, providing a partial understanding of the subject matter.
  - **Example:**
    - **Search Prompt:** “Workout Routines and Wellness Advice”
    - **List of Video Titles:** “10 Minute Morning Yoga for Beginners”, “My Favorite Healthy Snacks!”, “The Truth About Cardio”, “Exploring Ancient Ruins: A Journey to Petra”, “Understanding Your Body’s Energy Systems”

- **Score 2: High Relevance**
  - **Definition:** The channel mainly features videos that are highly relevant, covering various aspects and providing substantial insights into the subject matter described in the search prompt.
  - **Example:**
    - **Search Prompt:** “Tech Reviews and Product Comparisons”
    - **List of Video Titles:** “Apple iPhone 13 vs Samsung Galaxy S22: Ultimate Comparison”, “The Best Gaming Laptops of 2023: Top 5 Picks!”, “Sony A7IV: Unboxing and First Impressions”, “The Future of Electric Vehicles: Tesla and Beyond”, “Top 5 Smartwatches: A Comprehensive Review”

#### Instructions:
1. Carefully review the search prompt and the list of video titles provided.
2. Utilize `grading_function` for each provided search prompt and list of video titles to submit your reasoning and assigned score, ranging from 0 to 2, according to the grading rubric.
3. Maintain objectivity and impartiality in your scoring, focusing on the depth, breadth, and clarity of the content in alignment with the search prompt, irrespective of the overall number of videos.
4. Handle Quotation Marks Carefully: When producing output that quotes video titles from the user input, ensure a meticulous handling of single and double quotation marks. This is crucial for the output to be correctly parsed in JSON format.

#### Return format:
Submit your response in JSON format as follows:
```json
{{
    "relevance_score": <score (int)>,
    "explanation": "<brief rationale for the assigned score (string)>"
}}
"""

human_prompt = """
grading_function(search_prompt={search_query},
                 video_title_list={videos},
"""

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(system_template_llm_judge),
        HumanMessagePromptTemplate.from_template(human_prompt)
    ]
)

llm_judge_chain = LLMChain(
    llm=ChatOpenAI(model_name="gpt-3.5-turbo-16k", temperature=0),
    prompt=chat_template,
    output_parser=JsonToDict()
)

llm_judge_chain.__doc__ = """
    Evaluate the relevance of YouTube channel content based on the provided search prompt.

    Usage:
    llm_judge_chain.run({
        'search_query': query,
        'videos': video_list
    })

    Output Format:
    {
        "relevance_score": <score (int)>,
        "explanation": "<brief rationale for the assigned score (string)>"
    }
"""
