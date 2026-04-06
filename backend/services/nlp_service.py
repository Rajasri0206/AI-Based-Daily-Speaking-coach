import language_tool_python

# Initialize tool once
tool = language_tool_python.LanguageTool('en-US')

def correct_grammar(text: str) -> str:
    """
    Corrects grammar using LanguageTool
    """
    try:
        matches = tool.check(text)
        corrected_text = language_tool_python.utils.correct(text, matches)
        return corrected_text.strip()
    except Exception as e:
        raise Exception(f"NLP Error: {str(e)}")