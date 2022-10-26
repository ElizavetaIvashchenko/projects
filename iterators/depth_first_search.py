import pytest
from collections import Iterable

def dfs(it):
    for i, x in enumerate(it):
        while i < len(it) and isinstance(it[i], (list, tuple)):
            it[i:i+1] = it[i]
    return it

def test1():
    assert list(dfs([])) == []
    assert list(dfs([1])) == [1]
    assert list(dfs([1, 2])) == [1, 2]
    assert list(dfs([1, [2, 3, [], [4, 6, [7, 8]]], [10], 11])) == \
                [1, 2, 3, 4, 6, 7, 8, 10, 11]
if __name__ == '__main__':
    # При таком способе вызова каждый assert вместо просто да/нет будет
    # выдавать более детальную информацию, если что-то пошло не так.
    pytest.main([__file__])