import pytest
from collections import namedtuple

"""
class Values:
    def __init__(self):
        self.column_a = "sleep"
        self.column_b = 100
        self.column_c = True

    def test_func(self):
        return 404

Task = namedtuple("test_task", ["column_a", "column_b", "column_c"])
Task.__new__.__defaults__ = ("a", 0, False)
try_data = (Task("sleep", 100, True),
            Task("wake", 200, False),
            Task("breakfast", -100, ),
            Task("excercise", True),
            Task())

attr_list = ("column_a", "column_b", "column_c")

# このままだと全データでテストが実行されて失敗しまくる
@pytest.mark.parametrize("tasks", try_data)
def test_value(tasks):
    val = Values()
    for attr in attr_list:
        assert getattr(val, attr) == getattr(tasks, attr)
"""

def test_mock(mocker):
    import os
    assert os.path.join("\\a\\b", "c\\d\\e") == "\\a\\b\\c\\d\\e"
    with mocker.patch("os.path.join", return_value = "dummy"):
        assert os.path.join("\\a\\b", "\\c\\d\\e")


class TestCls:
    a = 200
    
    def b(self):
        return 500

def test_mock_object(mocker):
    assert TestCls.a == 200
    with mocker.patch.object(TestCls, "a"):
        TestCls.a = 300
        assert TestCls.a == 300
    TestCls.a == 400
    assert TestCls.a == 300
    mock = mocker.MagicMock(return_value=1000)
    with mocker.patch.object(TestCls, "b", mock):
        assert TestCls.b() == 1000
        