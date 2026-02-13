import pytest
from solution import Solution

solution = Solution()

@pytest.mark.parametrize("height, expected", [
    # Test case 1 
    ([1,8,6,2,5,4,8,3,7], 49),
    # Test case 2
    ([1,1], 1),
])

def test_solution(height, expected):
    result = solution.maxArea(height)

    assert result == expected