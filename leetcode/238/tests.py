import pytest
from solution import Solution

solution = Solution()

@pytest.mark.parametrize("nums, expected", [
    # Test case 1 
    ([1,2,3,4], [24,12,8,6]),
    # Test case 2
    ([-1,1,0,-3,3], [0,0,9,0,0]),
])

def test_solution(nums, expected):
    result = solution.productExceptSelf(nums)

    assert sorted(result) == sorted(expected)