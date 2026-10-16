from langchain.chat_models import init_chat_model
from langchain.messages import AnyMessage
from typing_extensions import TypedDict, Annotated
from langchain.messages import SystemMessage
from langchain.tools import tool
import operator

class MessageState(TypedDict):
    messages:Annotated[list[AnyMessage],operator.add]
model=init_chat_model(model_name="gemini-3.6-flash", temperature=0.0)


def llm_call(state:dict):
    return {
        "messages":[model]
    }