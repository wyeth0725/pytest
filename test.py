import pytest
from collections import namedtuple


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