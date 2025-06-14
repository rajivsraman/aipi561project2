def clean_input(text: str) -> str:
    return text.strip().replace('\n', ' ')

def tag_keywords(text: str) -> str:
    keywords = ["AI", "data", "model"]
    for word in keywords:
        text = text.replace(word, f"[{word}]")
    return text