# 🎥 YouTube & Website Content Summarizer (LangChain + Groq + Streamlit)

This project is an **AI-powered content summarizer** that extracts text
from: - 📺 **YouTube videos** - 🌐 **Web pages / articles**

and generates a **concise summary using Groq LLMs via LangChain**.

The application is built with **Streamlit**, making it easy to use
through a simple web interface.

------------------------------------------------------------------------

# 🚀 Features

-   Summarize **YouTube videos automatically**
-   Summarize **any website article**
-   Uses **LangChain summarization chains**
-   Powered by **Groq LLM (Llama 3.1)**
-   Handles **long transcripts with chunking**
-   Works with **auto-generated captions**
-   Clean **Streamlit UI**
-   Secure **API key input from sidebar**

------------------------------------------------------------------------

# 🧠 How It Works

1.  User enters:

    -   Groq API key
    -   YouTube or Website URL

2.  The system:

    -   Extracts transcript (YouTube) or text (website)
    -   Splits long content into chunks
    -   Sends chunks to Groq LLM

3.  LangChain performs **map-reduce summarization**

4.  Final **300‑word summary** is generated and displayed.

------------------------------------------------------------------------

# 🏗 Project Architecture

    User Input (Streamlit UI)
            │
            ▼
     URL Validation
            │
            ▼
    Content Loader
     ├─ YouTube Transcript API
     └─ Website Loader (UnstructuredURLLoader)
            │
            ▼
    Text Splitter (LangChain)
            │
            ▼
    Groq LLM (Llama‑3.1‑8B)
            │
            ▼
    LangChain Map‑Reduce Summarization
            │
            ▼
    Summary Output

------------------------------------------------------------------------

# 📂 Project Structure

    YT-Video-Summarization/
    │
    ├── app.py
    ├── requirements.txt
    ├── README.md
    └── .gitignore

------------------------------------------------------------------------

# ⚙️ Installation

### 1️⃣ Clone the Repository

    git clone https://github.com/Fardeennnnnnnnnnkhan/YT-VIdeo-Summarization.git
    cd YT-VIdeo-Summarization

### 2️⃣ Create Virtual Environment

    python -m venv venv

Activate environment

**Windows**

    venv\Scripts\activate

**Mac / Linux**

    source venv/bin/activate

------------------------------------------------------------------------

# 📦 Install Dependencies

    pip install -r requirements.txt

------------------------------------------------------------------------

# 🔑 Get Groq API Key

1.  Visit

```{=html}
<!-- -->
```
    https://console.groq.com/keys

2.  Generate an API key

3.  Paste it into the **Streamlit sidebar** when running the app

------------------------------------------------------------------------

# ▶️ Run the Application

    streamlit run app.py

Streamlit will start a local server:

    http://localhost:8501

------------------------------------------------------------------------

# 🧪 Example Usage

### YouTube Example

    https://www.youtube.com/watch?v=o126p1QN_RI

### Website Example

    https://blog.langchain.dev

------------------------------------------------------------------------

# 📚 Technologies Used

  Technology               Purpose
  ------------------------ -----------------------------
  Python                   Backend language
  Streamlit                Web UI
  LangChain                LLM orchestration
  Groq API                 Fast inference
  Llama 3.1                Language model
  youtube-transcript-api   Extract YouTube transcripts
  Unstructured Loader      Web content extraction

------------------------------------------------------------------------

# 🛠 Key LangChain Components

-   `PromptTemplate`
-   `load_summarize_chain`
-   `RecursiveCharacterTextSplitter`
-   `Document`
-   `ChatGroq`

------------------------------------------------------------------------

# ⚠️ Limitations

-   Videos **without captions cannot be summarized**
-   Very long transcripts may take longer to process
-   Requires an active **Groq API key**

------------------------------------------------------------------------

# 🔮 Future Improvements

-   Support **PDF summarization**
-   Add **multi‑language translation**
-   Add **chapter-wise summaries**
-   Improve UI with **video preview**
-   Export summaries as **PDF or Markdown**

------------------------------------------------------------------------

# 👨‍💻 Author

**Fardeen Khan**

GitHub: https://github.com/Fardeennnnnnnnnnkhan

------------------------------------------------------------------------

# ⭐ Support

If you find this project useful:

⭐ Star the repository\
🍴 Fork the project\
🚀 Build your own AI tools

------------------------------------------------------------------------

# 📜 License

This project is open-source and available under the **MIT License**.
