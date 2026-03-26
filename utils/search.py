import re

def highlight(text, query, max_length=200):
    """
    Trims text to a snippet around the first match,
    then wraps matching words in <mark> tags.
    """
    if not text or not query:
        return text[:max_length] + "..." if text and len(text) > max_length else text

    # Find first match position for smart snippet
    lower_text = text.lower()
    lower_query = query.lower()
    pos = lower_text.find(lower_query)

    if pos != -1:
        start = max(0, pos - 60)
        end = min(len(text), pos + max_length)
        snippet = ("..." if start > 0 else "") + text[start:end] + ("..." if end < len(text) else "")
    else:
        snippet = text[:max_length] + ("..." if len(text) > max_length else "")

    # Highlight all matching words
    words = re.escape(query).replace(r"\ ", "|")
    pattern = re.compile(f"({words})", re.IGNORECASE)
    return pattern.sub(r'<mark>\1</mark>', snippet)