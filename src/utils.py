from src.llm import get_gemini, get_openrouter


def safe_invoke(prompt):

    try:

        llm = get_gemini()

        return llm.invoke(prompt)

    except Exception as gemini_error:

        print("=" * 50)
        print("Gemini Failed")
        print(gemini_error)
        print("Switching to OpenRouter...")
        print("=" * 50)

        try:

            llm = get_openrouter()

            return llm.invoke(prompt)

        except Exception as openrouter_error:

            raise RuntimeError(
                f"""
Gemini Error:
{gemini_error}

OpenRouter Error:
{openrouter_error}
"""
            )