import pytest
from solution import Solution

solution = Solution()

@pytest.mark.parametrize("nums, expected", [
    # Test case 1 
    ([3,4,5,1,2], 1),
    # Test case 2
    ([4,5,6,7,0,1,2], 0),
    # Test case 2
    ([11,13,15,17], 11),
])

def test_solution(nums, expected):
    result = solution.findMin(nums)

    assert result == expected