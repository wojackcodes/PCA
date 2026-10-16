from langchain.chat_models import init_chat_model
from langchain.messages import AnyMessage
from typing_extensions import TypedDict, Annotated
from langchain.messages import SystemMessage
from langchain.tools import tool
from langchain.messages import ToolMessage
import operator

@tool
def greet():
    return "Hello, world!"

tools=[greet]

class MessageState(TypedDict):
    messages:Annotated[list[AnyMessage],operator.add]
    llm_calls:int
model=init_chat_model(model_name="gemini-3.6-flash", temperature=0.0)


model_with_tools=model.bind_tools(tools=tools)
def llm_call(state:dict):
    return {
        "messages":[model_with_tools.invoke([SystemMessage(content="You are a helpful assistant that can call tools to answer questions."),]+state["messages"])],
        "llm_calls":state.get('llm_calls',0)+1
    }