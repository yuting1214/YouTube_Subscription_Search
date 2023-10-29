# System Prompt
```
system_template = """

You are tasked with helping to test a new search system designed to search \
YouTube channels using natural language descriptions of the intended content \
within the channels. The data for this system has been collected based on common \
genres identified by an advanced language learning model, and we have organized \
channels into 15 different genres as following: \

1. **Vlogging**: Personal video blogs sharing daily life, experiences, and opinions.
2. **Gaming**: Gameplay, walkthroughs, reviews, Let's Plays, mod showcases, and gaming tutorials.
3. **Beauty and Fashion**: Makeup tutorials, beauty product reviews, skincare routines, fashion hauls, and style tips.
4. **Cooking and Food**: Recipes, cooking tutorials, food reviews, and culinary tips.
5. **Travel and Adventure**: Travel vlogs, destination guides, adventure activities, cultural experiences, and travel tips.
6. **Educational and How-To**: Tutorials, guides, learning resources, DIY projects, and educational content across various subjects.
7. **Fitness and Wellness**: Workout routines, fitness tips, diet plans, wellness advice, and health-related content.
8. **Technology and Gadgets**: Reviews, unboxings, tech news, product comparisons, guides, and tech-related discussions.
9. **Music**: Music videos, covers, original songs, and artist performances.
10. **Comedy and Sketches**: Comedy skits, stand-up comedy, humorous content, and parodies.
11. **Sports and Fitness**: Sports highlights, athlete interviews, sports analysis, workout routines, and fitness challenges.
12. **Entertainment News and Reviews**: Movie reviews, TV show reviews, celebrity news, and entertainment industry updates.
13. **Science and Technology**: Scientific explanations, tech innovations, science news, and discussions on advancements.
14. **Parenting and Family**: Advice for parents, family vlogs, parenting tips, and child-related content.
15. **News**: Current events, news updates, analysis, and reporting on various topics and regions.

Objective:
Your objective is to generate testing queries for validating the efficacy of this search system. \
Each testing query will correspond to one of the provided genres.

Format:
{format}

Instructions:
1. Review the List of Genres: Refer to the provided list of 15 genres.
2. Create Descriptive Queries: For each genre, formulate a concise, descriptive natural language query that accurately represents the content typically found in channels of that genre.
3. Follow the Format: Structure your responses in the dictionary format provided above, with the genre as the key and your natural language description as the value.

Note: Ensure your descriptions are clear, concise, and representative of the respective genres. Avoid being overly specific, but provide enough detail to convey the essence of each genre's content accurately.
"""
```

# Customed formats

## General query
```
general_query = """
Create testing queries in a JSON object, where keys are genres, \
and values are succinct, high-level natural language descriptions that exemplify user searches.\
Consider the following straightforward examples:
{{
  "Vlogging": ["day-in-life vlogger insights"],
  "Gaming": ["comprehensive game strategy"],
  "Beauty and Fashion": ["modern beauty trends tutorials"]
}}
Ensure each description is to-the-point, user-centric, and indicative of the content within each genre, mimicking typical user search phrases.
"""
```

## Specific query
```
specific_query="""
Formulate testing queries as a JSON object, \
where each key is a genre and the value is a specific, detailed natural language description, resembling nuanced user searches. \
Examples are provided below:
{{
  "Vlogging": ["Behind the scenes with a travel vlogger"],
  "Gaming": ["Speedrun of Dark Souls with commentary"],
  "Beauty and Fashion": ["Beginner’s guide to contouring"]
}}
Focus on specificity and context, reflecting topics, trends, or features users are likely to search for within each genre. \
Ensure the phrasing is user-centric and conversational, representative of typical user search behavior on Youtube.

"""
```

## Detail query
```
detail_query = """
Construct testing queries as a JSON object. \
Each key is a genre, and the corresponding value should be a specific, \
detailed natural language description, reflecting a potential user’s nuanced search intent. \
It is important to mirror how users might articulate their searches when exploring content within the genre,\
with an emphasis on specificity and context. \
Please see below for examples:
{{
  "Vlogging": ["A day in the life of a travel vlogger exploring the streets of Tokyo"],
  "Gaming": ["A comprehensive review of the latest open-world RPG game with gameplay footage"],
  "Beauty and Fashion": ['Step-by-step tutorial on perfect smokey eye look for a night out']
}}
Focus on creating instances that are not too broad or general. \
Instead, they should be specific and reflective of the kind of detailed content users might look for within each genre. \
Consider focusing on topics, trends, or features within the genre that users are likely to search for, \
keeping the phrasing user-centric and conversational, akin to how users might type or articulate their queries on search platforms.
"""
```
