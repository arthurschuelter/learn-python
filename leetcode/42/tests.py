import pytest
from solution import Solution

solution = Solution()

@pytest.mark.parametrize("height, expected", [
    # Test case 1 
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    # Test case 2
    ([4,2,0,3,2,5], 9),
])

def test_solution(height, expected):
    result = solution.trap(height)

    assert result == expected