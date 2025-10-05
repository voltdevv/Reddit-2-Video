import ollama
from ollama import ChatResponse


def filter(text) -> str:
    """
    This filters the paramenter, text, to replace profanity and 
    to unabbreivate abbreviations. Just uses a local AI with
    ollama and returns the new post text. 
    """
    response: ChatResponse = ollama.chat(
        model="llama3",
        messages=[
            {
                'role': 'user',
                'content': (
                    "Please process the following text with the following rules:\n\n"
                    "1. Profanity Filter: Replace all profane or offensive words with appropriate, family-friendly alternatives that maintain the tone or intent of the original message.\n"
                    "2. Abbreviation Expansion:\n"
                    "   - Expand all age/gender abbreviations (e.g., \"19m\" → \"19 male\", \"25f\" → \"25 female\").\n"
                    "   - Expand all acronyms (e.g., \"AITA\" → \"am I the a-hole\"). Use \"a-hole\" as a censored but recognizable form.\n"
                    "3. Formatting:\n"
                    "   - Remove unnecessary spaces and line breaks.\n"
                    "   - Return the result as a single clean block of text.\n"
                    "   - Also, remove anything that isn't part of the story or from the user. i.e reddit mod text. \n"
                    "4. Output Only: Return only the transformed text. Do not include explanations or extra formatting. ONLY RETURN THE TEXT.\n\n"
                    f"Input Text: {text}"
                )
            }
        ]
    )

    return response.message.content.strip()
