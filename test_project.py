from project import add_products, get_ints, list_products, remove_products
from persist import Persist

p = Persist(".persisted/.test/.test.csv")

# Clean .test.csv before tests
p.open_to("w")

def test_add_products():
    global p
    assert add_products(["abcd", "efgh", "ijkl", "mnop"], p) == ["abcd", "efgh", "ijkl", "mnop"]
    assert add_products(["qrs", "tuv", "wxyz"], p) == ["abcd", "efgh", "ijkl", "mnop", "qrs", "tuv", "wxyz"]


def test_remove_products():
    global p
    assert remove_products([1, 5, 6, 4], ["abcd", "efgh", "ijkl", "mnop", "qrs", "tuv", "wxyz"], p) == ["efgh", "ijkl", "wxyz"]
    assert remove_products([3], ["efgh", "ijkl", "wxyz"], p) == ["efgh", "ijkl"]
    assert remove_products([1, 2], ["efgh", "ijkl"], p) == []


def test_list_products():
    global p
    assert list_products(p) == []


def test_get_ints():
    assert get_ints("only text") == []
    assert get_ints("1 3 4 5") == [1, 3, 4 ,5]
    assert get_ints("a1 33kj 5, 3") == [5, 3]
    assert get_ints("3, 4, 5, (33)") == [3, 4, 5, 33]
    