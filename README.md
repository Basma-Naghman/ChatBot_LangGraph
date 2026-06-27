# 🤖 ChatBot with LangGraph

A conversational chatbot built with **LangGraph** and **Groq's LLaMA 3.1**, featuring persistent memory across messages and a clean **Streamlit** chat interface.

---

## ✨ Features

- **Stateful Conversations** — uses LangGraph's `MemorySaver` to retain the full message history within a session thread
- **LLaMA 3.1 via Groq** — powered by `llama-3.1-8b-instant` for fast, high-quality responses
- **Graph-based Architecture** — conversation logic is modeled as a `StateGraph` with typed state
- **Streamlit UI** — minimal, intuitive chat interface with role-based message display

---

## 🗂️ Project Structure

```
ChatBot_LangGraph/
├── langraph_backend.py   # LangGraph state graph, LLM setup, checkpointer
├── streamlit_app.py      # Streamlit frontend and chat UI
├── .env                  # API keys (not committed)
└── requirements.txt      # Python dependencies
```

---

## ⚙️ How It Works

### Backend (`langraph_backend.py`)

The backend defines a `StateGraph` with a single `chat_node`:

1. **State** — `ChatState` holds a list of `BaseMessage` objects, accumulated via `add_messages`
2. **LLM** — `ChatGroq` wraps `llama-3.1-8b-instant` with `temperature=0.7`
3. **Graph** — `START → chat_node → END`
4. **Memory** — `MemorySaver` checkpointer persists conversation state per `thread_id`

### Frontend (`streamlit_app.py`)

- Renders previous messages from `st.session_state`
- Sends new user input to the compiled LangGraph chatbot
- Uses a fixed `thread_id` (`thread_1`) so memory is consistent within a session
- Appends both user and assistant messages to the display history

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Basma-Naghman/ChatBot_LangGraph.git
cd ChatBot_LangGraph
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install langgraph langchain-groq langchain-core streamlit python-dotenv
```

### 3. Set up environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your free API key at [console.groq.com](https://console.groq.com).

### 4. Run the app

```bash
streamlit run streamlit_app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🧠 Tech Stack

| Tool | Purpose |
|---|---|
| [LangGraph](https://github.com/langchain-ai/langgraph) | Stateful graph-based conversation orchestration |
| [LangChain Groq](https://python.langchain.com/docs/integrations/chat/groq/) | LLM provider integration |
| [Groq — LLaMA 3.1 8B](https://groq.com) | Underlying language model |
| [Streamlit](https://streamlit.io) | Chat user interface |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

## 📋 Requirements

- Python 3.9+
- A [Groq API key](https://console.groq.com)

---

## 📌 Notes

- The `thread_id` is currently hardcoded as `thread_1`. To support multiple independent conversations, generate a unique `thread_id` per user session.
- `MemorySaver` stores state in memory only — it resets when the app restarts. For persistent storage across restarts, swap it with a database-backed checkpointer.
