from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from django.conf import settings

# Initialize Hugging Face model (e.g., GPT-2)
def initialize_huggingface_client():
    return HuggingFaceHub(repo_id="gpt2", huggingfacehub_api_token=settings.HUGGINGFACE_API_KEY)

# Create a code analysis chain using Hugging Face model
def create_code_analysis_chain():
    prompt_template = """
    Analyze the following Django code for quality, score it out of 10, 
    and suggest improvements:

    Code:
    {code}

    Provide:
    - Code quality score (out of 10)
    - Suggestions for improvement
    - Identified problematic code patterns
    """

    prompt = PromptTemplate(template=prompt_template, input_variables=["code"])
    llm = initialize_huggingface_client()
    chain = LLMChain(llm=llm, prompt=prompt)

    return chain
