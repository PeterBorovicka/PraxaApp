from langchain_community.chat_models import ChatOpenAI
from typing import Optional, Any
import os


DEFAULT_MODEL = "openai/gpt-4o-mini"


class ChatModel(ChatOpenAI):
    """
    Creates a chat model from openrouter.ai using the OpenAI API
    """
    def __init__(
            self,
            model_name: str,
            openai_api_key: Optional[str] = None,
            openai_api_base: str="https://openrouter.ai/api/v1",
            **kwargs: Any):
        openai_api_key = openai_api_key or os.getenv('OPENROUTER_API_KEY')
        super().__init__(
            openai_api_base=openai_api_base,
            openai_api_key=openai_api_key,
            model_name=model_name,
            **kwargs
        )


def get_model(model_name: Optional[str] = None) -> ChatModel:
    """
    Gets a reference to a model
    
    :param model_name: Name of the model. Defaults to OPENROUTER_MODEL or a paid model with better availability.
    :type model_name: str | None
    :return: the model
    :rtype: ChatModel
    """
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
    if not openrouter_api_key:
        raise RuntimeError(
            "OPENROUTER_API_KEY is not set. Export it in your shell before starting the app."
        )

    selected_model = model_name or os.getenv("OPENROUTER_MODEL") or DEFAULT_MODEL

    return ChatModel(
        model_name=selected_model,
        openai_api_key=openrouter_api_key,
        max_tokens=512,
        temperature=0
    )


if __name__ == "__main__":
# when run as a script, run some tests to demonstrate capabilities
#    model = get_model()
#    from langchain_core.messages import HumanMessage
#    from langchain.prompts import ChatPromptTemplate

#    prompt_template = ChatPromptTemplate([
#        ("human", "You are a helpful assistant."),
#        ("human", "What is {playwright}'s most recent play?")
#    ])

#    response = model.invoke(
#        [HumanMessage("You are a helpful assistant."),
#         HumanMessage("What are some plays by Tawfiq al-Hakim?")])
#    print(response.content)
#    print("----------")
#    response = model.invoke(
#        [HumanMessage("You are a helpful assistant."),
#         HumanMessage("What is Ryan Calais Camerons's most recent play?")])
#    print(response.content)
#    print("----------")
#    response = model.invoke(
#        [HumanMessage("You are a helpful assistant."),
#         HumanMessage("What Broadway shows have more than 10,000 performances?")])
#    print(response.content)

#    print(prompt_template.invoke({"playwright": "Ryan Calais Cameron"}))
#    response = model.invoke(prompt_template.invoke({"playwright": "Ryan Calais Cameron"}))
#    print(response.content)

#    chain = prompt_template | model
#    response = chain.invoke({"playwright": "Ryan Calais Cameron"})
#    print(response.content)

    pass
