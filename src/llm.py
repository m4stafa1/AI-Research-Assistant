import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


def get_llm():

    # ================= Gemini =================

    if GOOGLE_API_KEY:

        try:

            llm = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                google_api_key=GOOGLE_API_KEY,
                temperature=0.3,
                max_output_tokens=2048,
            )

            llm.invoke("Hello")

            print("=" * 50)
            print("Using Gemini")
            print("=" * 50)

            return llm

        except Exception as e:

            print("=" * 50)
            print("Gemini Failed")
            print(e)
            print("=" * 50)

    # ================= OpenRouter =================

    if OPENROUTER_API_KEY:

        try:

            llm = ChatOpenAI(
                model="deepseek/deepseek-chat-v3-0324",
                base_url="https://openrouter.ai/api/v1",
                api_key=OPENROUTER_API_KEY,
                temperature=0.3,
                max_tokens=2048,
            )

            llm.invoke("Hello")

            print("=" * 50)
            print("Using OpenRouter")
            print("=" * 50)

            return llm

        except Exception as e:

            print("=" * 50)
            print("OpenRouter Failed")
            print(e)
            print("=" * 50)

    raise RuntimeError(
        "No available LLM. Please check your API keys."
    )


llm = get_llm()