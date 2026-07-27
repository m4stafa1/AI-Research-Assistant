import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


def get_llm():
    """
    Try Gemini first.
    If it fails, automatically use OpenRouter.
    """

    # -------- Gemini --------
    try:

        llm = ChatGoogleGenerativeAI(
            model="gemini-flash-latest",
            google_api_key=GOOGLE_API_KEY,
            temperature=0.2,
        )

        # اختبار سريع
        
        print("Using Gemini")

        return llm

    except Exception as e:

        print(" Gemini Failed")
        print(e)

    # -------- OpenRouter --------

    try:

        llm = ChatOpenAI(
            model="deepseek/deepseek-chat-v3-0324",
            base_url="https://openrouter.ai/api/v1",
            api_key=OPENROUTER_API_KEY,
            temperature=0.2,
        )

        

        print("Using OpenRouter")

        return llm

    except Exception as e:

        print(" OpenRouter Failed")
        print(e)

        raise RuntimeError(
            "No available LLM. Gemini and OpenRouter both failed."
        )


llm = get_llm()