def summarize_response(text: str) -> str:
    return text.split('.')[0] + '.' if '.' in text else text