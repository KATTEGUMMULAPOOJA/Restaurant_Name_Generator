from key import API_KEY
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain 
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain



os.environ['OPENAI_API_KEY']=API_KEY

llm=OpenAI(temperature=0.6)



def generate_restaurant_name_and_items(cuisine):
    # restaurant Name
    prompt_template_name=PromptTemplate(
    input_variables=['cuisine'],
    template="I want to open a restaurant for Indian food. Suggest a fancy name for this."
)

    name_chain=LLMChain(llm=llm,prompt=prompt_template_name,output_key="resturant_name")

# Menu Items
    prompt_template_items=PromptTemplate(
        input_variables=['resturant_name'],
        template="Suggest some menu items for {resturant_name}. Return it as comma separated list."

    )

    food_items_chain=LLMChain(llm=llm,prompt=prompt_template_items,output_key="menu_items")

    chain=SequentialChain(
        chains=[name_chain,food_items_chain],
        input_variables=['cuisine'],
        output_variables=['resuturant_name','menu_items']
    )
    response=chain({'cuisine':'Arabic'})

    return response
if __name__ =="__main__":
    print(generate_restaurant_name_and_items("Indian"))

