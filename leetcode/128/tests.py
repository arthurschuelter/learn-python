import pytest
from solution import Solution

solution = Solution()

@pytest.mark.parametrize("nums, expected", [
    # Test case 1 
    ([0,3,7,2,5,8,4,6,0,1], 9),
    # Test case 2
    ([1,0,1,2], 3),
])

def test_solution(nums, expected):
    result = solution.longestConsecutive(nums)

    assert result == expected