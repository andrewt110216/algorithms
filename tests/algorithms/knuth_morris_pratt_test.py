from algorithms.knuth_morris_pratt import knuth_morris_pratt, test_cases


def test_knuth_morris_pratt():
    for text, pattern, expected in test_cases:
        assert knuth_morris_pratt(text, pattern) == expected
