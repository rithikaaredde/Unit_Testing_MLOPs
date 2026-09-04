"""
test_pipeline.py - Unit tests for pipeline.py, written with pytest.

Run with:
    pytest test_pipeline.py -v

WHAT IS UNIT TESTING?
----------------------
A "unit" is the smallest testable piece of code - usually a single function.
A unit test checks that ONE function behaves correctly for a given input,
in isolation from the rest of the program.

Good unit tests are:
  - Small and focused (test one behavior at a time)
  - Independent (order shouldn't matter, no shared state between tests)
  - Repeatable (same result every time you run them)
  - Fast (no network calls, no waiting)

HOW PYTEST WORKS
-----------------
- pytest auto-discovers any file named test_*.py or *_test.py
- Inside, it runs any function named test_*
- Each test uses a plain `assert` statement. If the assertion is True,
  the test passes. If False, pytest fails it and shows you exactly
  what was expected vs what happened.
- The `-v` flag just means "verbose" - it prints each test name and result.
"""

import pytest
from pipeline import clean_text, to_upper, word_count, is_palindrome, divide, run_pipeline


# ---------------------------------------------------------------------------
# 1. BASIC TESTS - one assertion, one behavior
# ---------------------------------------------------------------------------

def test_clean_text_strips_whitespace():
    assert clean_text("  hello world  ") == "hello world"


def test_clean_text_collapses_multiple_spaces():
    assert clean_text("hello    world") == "hello world"


def test_to_upper_converts_correctly():
    assert to_upper("hello") == "HELLO"


def test_word_count_basic():
    assert word_count("the quick brown fox") == 4


def test_word_count_empty_string_is_zero():
    assert word_count("") == 0


# ---------------------------------------------------------------------------
# 2. EDGE CASES - don't just test the "happy path"
#    Always ask: what about empty input? weird input? boundary values?
# ---------------------------------------------------------------------------

def test_is_palindrome_true_for_simple_word():
    assert is_palindrome("racecar") is True


def test_is_palindrome_ignores_case_and_spaces():
    # "A man a plan a canal Panama" is a classic palindrome phrase
    assert is_palindrome("A man a plan a canal Panama") is True


def test_is_palindrome_false_for_normal_text():
    assert is_palindrome("hello world") is False


def test_is_palindrome_empty_string_is_true():
    # An empty string reversed is still empty - technically a palindrome
    assert is_palindrome("") is True


# ---------------------------------------------------------------------------
# 3. TESTING EXCEPTIONS
#    Use pytest.raises() to confirm your code fails the way it SHOULD fail.
# ---------------------------------------------------------------------------

def test_divide_normal_case():
    assert divide(10, 2) == 5


def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_divide_by_zero_error_message():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)


# ---------------------------------------------------------------------------
# 4. TESTING FUNCTIONS THAT RETURN COMPLEX DATA (dicts, lists, objects)
# ---------------------------------------------------------------------------

def test_run_pipeline_returns_expected_keys():
    result = run_pipeline("  hello   world  ")
    assert set(result.keys()) == {"cleaned", "upper", "word_count"}


def test_run_pipeline_values_are_correct():
    result = run_pipeline("  hello   world  ")
    assert result["cleaned"] == "hello world"
    assert result["upper"] == "HELLO WORLD"
    assert result["word_count"] == 2


# ---------------------------------------------------------------------------
# 5. PARAMETRIZED TESTS
#    Instead of copy-pasting a test for every input, let pytest loop for you.
#    Each tuple below runs as its own separate test case in the -v output.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("text, expected_count", [
    ("one", 1),
    ("one two", 2),
    ("one two three", 3),
    ("   spaced   out   words   ", 3),
    ("", 0),
])
def test_word_count_parametrized(text, expected_count):
    assert word_count(text) == expected_count


@pytest.mark.parametrize("text, expected", [
    ("racecar", True),
    ("hello", False),
    ("Was it a car or a cat I saw", True),
    ("Python", False),
])
def test_is_palindrome_parametrized(text, expected):
    assert is_palindrome(text) == expected


# ---------------------------------------------------------------------------
# 6. FIXTURES
#    A fixture provides reusable setup data/objects to multiple tests.
#    pytest automatically passes it in when a test function asks for it
#    by name (see the `sample_text` argument below).
# ---------------------------------------------------------------------------

@pytest.fixture
def sample_text():
    """Reusable sample input for tests that need it."""
    return "  The Quick Brown Fox  "


def test_clean_text_with_fixture(sample_text):
    assert clean_text(sample_text) == "The Quick Brown Fox"


def test_word_count_with_fixture(sample_text):
    assert word_count(sample_text) == 4
