system = """You are an helpful assistant"""

search_query_gen = """
You have been given a task you need to create multiple search queries for the search engine on the task. The queries needs to be such that more and more information should be aquired for the task. 
### TASK:
$task

### RESPONSE FORMAT:
{"search_queries" : ["<query 1>",...]}

Note: 
1. Do not give more than 10 search queries.
2. If you do not have anything to respond then repond with {}.
"""


response_gen = """
Based on the below information curated from the internet give response to the task. CURRATED INFORMATION also contains the source of the information.
### TASK:
{task}

### CURRATED INFORMATION:
{information}

Note: 
1. Give output in a string format.
2. Annotate the final response sentence with its source.
"""