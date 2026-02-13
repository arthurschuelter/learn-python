import pytest
from solution import Solution

solution = Solution()

@pytest.mark.parametrize("s, k, expected", [
    # Test case 1 
    ("XYYX", 2, 4),
    # Test case 2
    ("AAABABB", 1, 5),
])

def test_solution(s, k, expected):
    result = solution.characterReplacement(s, k)

    assert result == expected