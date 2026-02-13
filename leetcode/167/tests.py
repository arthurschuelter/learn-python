import pytest
from solution import Solution

solution = Solution()

@pytest.mark.parametrize("nums, target, expected", [
    # Test case 1 
    ([2,7,11,15], 9, [1,2]),
    # Test case 2
    ([2,3,4], 6, [1,3]),
])

def test_solution(nums, target, expected):
    result = solution.twoSum(nums, target)

    assert result == expected