import validators
import streamlit as st

from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.schema import Document

from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import UnstructuredURLLoader


# Streamlit App
st.set_page_config(
    page_title="LangChain : Summarization of Text from YouTube or Website",
    page_icon="🎥",
    layout="wide"
)

st.title("LangChain : Summarization of Text From YouTube or Any Website")
st.subheader("Summarize URL")


# Sidebar API key input
with st.sidebar:
    groq_api_key = st.text_input(
        "Enter your Groq API Key",
        value="",
        type="password"
    )


# URL input
url = st.text_input(
    "Enter the URL of the YouTube Video or Website to be Summarized",
    label_visibility="collapsed"
)


if st.button("Summarize The Content"):

    # Validate inputs
    if not groq_api_key.strip() or not url.strip():
        st.error("Please provide the required information to get started.")
        st.stop()

    if not validators.url(url):
        st.error("Please enter a valid URL.")
        st.stop()

    try:
        with st.spinner("Summarizing the content..."):

            # Initialize LLM
            llm = ChatGroq(
                groq_api_key=groq_api_key,
                model_name="llama-3.1-8b-instant",
                streaming=True
            )

            # --------------------------
            # YOUTUBE URL HANDLING
            # --------------------------
            if "youtube.com" in url or "youtu.be" in url:

                # Extract video ID
                if "youtube.com" in url:
                    query = urlparse(url)
                    video_id = parse_qs(query.query)["v"][0]
                else:
                    video_id = url.split("/")[-1]

                transcript_list = YouTubeTranscriptApi().list(video_id)

                try:
                    transcript = transcript_list.find_transcript(['en'])
                except:
                        transcript = list(transcript_list)[0]   # fallback to first available
                        transcript_data = transcript.fetch()

                # Convert to text
                text = " ".join([item.text for item in transcript_data])

                docs = [Document(page_content=text)]

            # --------------------------
            # WEBSITE URL HANDLING
            # --------------------------
            else:

                loader = UnstructuredURLLoader(
                    urls=[url],
                    ssl_verify=False,
                    headers={"User-Agent": "Mozilla/5.0"}
                )

                docs = loader.load()

                if not docs:
                    st.error("Could not fetch content from this website.")
                    st.stop()

            if len(docs) == 0:
                st.error("No content available to summarize.")
                st.stop()

            # Prompt
            prompt_template = """
Provide a concise summary of the following content in about 300 words.

Content:
{text}
"""

            prompt = PromptTemplate(
                template=prompt_template,
                input_variables=["text"]
            )

            # Summarization chain
            chain = load_summarize_chain(
                llm,
                chain_type="map_reduce",
                map_prompt=prompt,
                combine_prompt=prompt
            )

            summary = chain.run(docs)

            st.success("Content Summarized Successfully!")
            st.write(summary)

    except Exception as e:
        st.error(f"An error occurred while loading the content: {e}")