from langgraph.graph import StateGraph , START , END
from typing import TypedDict , Annotated
from langchain_core.messages import HumanMessage , SystemMessage , BaseMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages

load_dotenv()
llm = ChatGroq(
    model="llama-3.1-8b-instant", 
    temperature=0.7
)

class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage] , add_messages]

def chat_node(state:ChatState):
    #take user query from state
    messages = state['messages']
    
    #send to llm
    response = llm.invoke(messages)
    
    return {'messages':[response]}
    
import sqlite3
connection  = sqlite3.connect(database='chatbot.db',check_same_thread=False) 
       
checkpointer  = SqliteSaver(conn=connection)


graph = StateGraph(ChatState)

graph.add_node('chat_node',chat_node)

graph.add_edge(START , 'chat_node')
graph.add_edge('chat_node',END)

chatbot = graph.compile(checkpointer=checkpointer) 

def retrieve_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None):
       all_threads.add(checkpoint.config['configurable']['thread_id'])

    return list(all_threads)    



