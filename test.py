# from langchain_core.output_parsers import JsonOutputParser
# from langchain_core.prompts import PromptTemplate
# from pydantic import BaseModel, Field
# from langchain_openai import ChatOpenAI
# import prompts
# from dotenv import load_dotenv
# # import prompts
# import json

# load_dotenv()

# model = ChatOpenAI(temperature=0)

# class Joke(BaseModel):
#     questions: str = Field(description="search queries generated by llm.")




# task = "Current job situation"

# # Set up a parser + inject instructions into the prompt template.
# parser = JsonOutputParser(pydantic_object=Joke)

# # prompt = PromptTemplate(
# #     template= prompts.search_query_gen,
# #     input_variables=["task"],
# #     #partial_variables={"format_instructions": parser.get_format_instructions()},
# # )

# prompt = prompts.search_query_gen.replace('$task', task)
# # print(prompt)
# # chain = prompt | model #| parser

# content = model.invoke(prompt).content
# print(content)
# print(json.loads(content))


from tavily import TavilyClient

# Step 1. Instantiating your TavilyClient
tavily_client = TavilyClient(api_key= "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")

# Step 2. Executing a simple search query
response = tavily_client.get_search_context("Who is Leo Messi?")

# Step 3. That's it! You've done a Tavily Search!
print(response)
# print(response.keys())