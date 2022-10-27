import pytest

def test_add():
    # test basic functionality
    assert project.add(1,1) == 2
    # try a border case
    assert project.add(-1,-1) == -2
