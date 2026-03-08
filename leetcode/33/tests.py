import pytest
from solution import Solution

solution = Solution()

@pytest.mark.parametrize("nums, target, expected", [
    ([4,5,6,7,0,1,2], 0, 4),
    ([4,5,6,7,0,1,2], 3, -1),
    ([8,1,2,3,4,5,6,7], 6, 6),
    ([5,1,2,3,4], 1, 1),
])

def test_solution(nums, target, expected):
    result = solution.search(nums, target)

    assert result == expected