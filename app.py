from langchain import prompts
from langchain import chains
from langchain_openai import ChatOpenAI
import streamlit as st
import os

os.environ['OPENAI_API_KEY']=st.secrets['OPENAI_API_KEY']

tweet_template="Give me {number} of tweets on {topic} topic "

gpt_4o_mini=ChatOpenAI(model_name="gpt-4o-mini")

prompt_template=prompts.PromptTemplate(input_variables=["number","topic"],template=tweet_template)
tweet_chain=prompt_template | gpt_4o_mini
# response=tweet_chain.invoke({"number":2,"topic":"transformer architecture"})
# print(response)

st.header("Tweet Generator")
st.subheader( " Generate Tweets based on number request")
topic = st.text_input("topic")
number= st.number_input("Number of Tweets",min_value=1,max_value=10,value=1,step=1)
if st.button("Generate"):
    tweets=tweet_chain.invoke({"number":number,"topic":topic})
    st.write(tweets.content)






