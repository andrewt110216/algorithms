from algorithms.boyer_moore import boyer_moore, test_cases


def test_boyer_moore():
    for text, pattern, expected in test_cases:
        assert boyer_moore(text, pattern) == expected
