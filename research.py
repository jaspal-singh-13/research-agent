import os
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from dotenv import load_dotenv
import prompts
import json
from tqdm import tqdm

load_dotenv()



class research:
    def __init__(self, task, model="gpt-4o-mini") -> None:
        self.model = model
        self.task = task 
        self.message = [("system",prompts.system)]
        

    def model_initialization(self):
        self.llm = ChatOpenAI(
            model=self.model,
            temperature=0,
            max_tokens=500,
            timeout=None,
            max_retries=2,)
        
        self.tavily = TavilyClient(api_key=os.getenv("TAVILY_KEY"))


    def get_search_queries(self, task):
        search_query_prompt = prompts.search_query_gen.replace("$task", task)
        self.message.append(
            ("human", search_query_prompt)
        )
        response = self.llm.invoke(self.message).content
        self.message.append(
            ("assistant", response)
        )
        return json.loads(response)
    


    def internet_search(self, search_queries):
        search_results = []
        for search_query in tqdm(search_queries['search_queries'], desc='processing search queries...'):
            search_result = self.tavily.get_search_context(search_query)
            search_results.append(search_result)
        return search_results
    

    
    def get_final_response(self, task, search_results):
        
        response_gen_prompt = prompts.response_gen.format(task= task, information = search_results)
        # print(response_gen_prompt)
        self.message.append(
            ("human", response_gen_prompt)
        )
        response = self.llm.invoke(self.message).content
        
        return response



    def execute(self):
        self.model_initialization()
        search_queries = self.get_search_queries(self.task)
        search_results = self.internet_search(search_queries)
        # print(search_results)
        response = self.get_final_response(self.task, search_results)
        return response



research_obj = research(task = "current job market in india")
print(research_obj.execute())