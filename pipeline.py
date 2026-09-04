"""
pipeline.py - A tiny "text processing pipeline" that we will unit test.

Each function does ONE simple job. This is intentional: small, single-purpose
functions are much easier to write unit tests for.
"""


def clean_text(text: str) -> str:
    """Strip leading/trailing whitespace and collapse internal spaces."""
    return " ".join(text.split())


def to_upper(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()


def word_count(text: str) -> int:
    """Count the number of words in the text."""
    return len(text.split())


def is_palindrome(text: str) -> bool:
    """Check if text is a palindrome, ignoring case, spaces, and punctuation."""
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def divide(a: float, b: float) -> float:
    """Divide a by b. Raises ValueError if b is 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def run_pipeline(text: str) -> dict:
    """Run text through clean -> upper, and report word count."""
    cleaned = clean_text(text)
    return {
        "cleaned": cleaned,
        "upper": to_upper(cleaned),
        "word_count": word_count(cleaned),
    }
