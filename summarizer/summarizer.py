from langchain.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.prompts import PromptTemplate


class SimpleSummarizer:    
    model_id = "Falconsai/text_summarization" # default model for summarization
    prompt = "Generate a concise summary of {text}" # default prompt for sumamrization
    def __init__(self, custom_model_id: str="", custom_prompt: str = "") -> None:
        """
        custom_model_id: str - custom model for text summarization
        custom_prompt: str - custom prompt for summarization
        """
        self.load_model(custom_model_id) # loading model
        self.load_prompt_template(custom_prompt) # loading prompt

    def load_model(self, custom_model_id: str):
        """
        Method to load model(default or a custom one) for text summarization
        """
        model_id = self.model_id
        if custom_model_id: # if custom model specified change our model to it
            model_id = custom_model_id
        self.llm = HuggingFacePipeline.from_model_id(
            model_id=model_id,
            task="summarization"
        )
    
    def load_prompt_template(self, custom_prompt) -> PromptTemplate:
        """
        Method to load prompt template(or a custom one) for text summarization
        Always write it as in an example with specifying {text} parametr
        Example:
        "Generate a concise summary of {text}"
        """
        prompt_template = self.prompt
        if custom_prompt: # load a custom prompt if we have a given one
            prompt_template = custom_prompt
        self.prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
    
    def summarize(self, text_to_summarize:str) -> str:
        """
        The main method of class. Makes summarization by given prompt and model
        text_to_summarize: str - Text to sumamrization
        returns: str - summary of our text
        """
        prompt_text = self.prompt.format(text=text_to_summarize)
        response = self.llm.invoke(input=prompt_text)
        return response
