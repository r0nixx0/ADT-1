import ast
import importlib
import inspect
import textwrap

import pytest

import assignment


@pytest.fixture
def s():
    return importlib.reload(assignment)


def calls_in(function):
    tree = ast.parse(textwrap.dedent(inspect.getsource(function)))
    names = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                names.append(node.func.id)
            if isinstance(node.func, ast.Attribute):
                names.append("." + node.func.attr)
    return names


def check_no_list_methods(function):
    for name in calls_in(function):
        if name in [".append", ".pop", ".insert", ".remove", ".extend", ".clear"]:
            pytest.fail(
                function.__name__ + "() uses " + name + "(). "
                "Change TopOfStack and use Stack[TopOfStack] instead."
            )


def test1_initial_stack(s):
    assert s.Stack == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert s.TopOfStack == -1


def test1_is_empty(s):
    assert s.IsEmpty() == True
    s.TopOfStack = 0
    assert s.IsEmpty() == False
    s.TopOfStack = 5
    assert s.IsEmpty() == False
    s.TopOfStack = -1
    assert s.IsEmpty() == True


def test1_is_full(s):
    assert s.IsFull() == False
    s.TopOfStack = 4
    assert s.IsFull() == False
    s.TopOfStack = 9
    assert s.IsFull() == True


def test2_push(s):
    assert s.Push(15) == True
    assert s.TopOfStack == 0
    assert s.Stack[0] == 15
    assert s.Push(27) == True
    assert s.TopOfStack == 1
    assert s.Stack[1] == 27
    assert s.Stack[0] == 15


def test2_push_when_full(s):
    for x in range(10):
        assert s.Push(x) == True
    assert s.Push(99) == False
    assert s.TopOfStack == 9
    assert s.Stack == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test2_uses_top_of_stack(s):
    check_no_list_methods(s.Push)
    for x in range(12):
        s.Push(x)
    assert len(s.Stack) == 10
    assert s.TopOfStack == 9


def test3_pop(s):
    s.Stack[0] = 10
    s.Stack[1] = 20
    s.Stack[2] = 30
    s.TopOfStack = 2
    assert s.Pop() == 30
    assert s.TopOfStack == 1
    assert s.Pop() == 20
    assert s.TopOfStack == 0
    assert s.Pop() == 10
    assert s.TopOfStack == -1


def test3_pop_when_empty(s):
    assert s.Pop() == -1
    assert s.TopOfStack == -1
    s.Stack[0] = 7
    s.TopOfStack = 0
    s.Pop()
    assert s.Pop() == -1
    assert s.TopOfStack == -1


def test3_uses_top_of_stack(s):
    check_no_list_methods(s.Pop)
    s.Stack[0] = 4
    s.Stack[1] = 6
    s.TopOfStack = 1
    assert s.Pop() == 6
    assert s.Pop() == 4
    assert s.Pop() == -1
    assert len(s.Stack) == 10


def test4_peek(s):
    assert s.Peek() == -1
    s.Stack[0] = 8
    s.Stack[1] = 3
    s.TopOfStack = 1
    assert s.Peek() == 3
    assert s.Peek() == 3
    assert s.TopOfStack == 1
    s.TopOfStack = 0
    assert s.Peek() == 8


def test4_size(s):
    assert s.Size() == 0
    s.TopOfStack = 0
    assert s.Size() == 1
    s.TopOfStack = 4
    assert s.Size() == 5
    s.TopOfStack = 9
    assert s.Size() == 10


@pytest.mark.parametrize("word, expected", [
    ["HELLO", "OLLEH"],
    ["abc", "cba"],
    ["Python", "nohtyP"],
    ["Mongolia", "ailognoM"],
    ["racecar", "racecar"],
    ["a", "a"],
    ["", ""],
])
def test5_reverse_word(s, word, expected):
    assert s.ReverseWord(word) == expected


def test5_starts_with_empty_stack(s):
    s.Push("x")
    s.Push("y")
    assert s.ReverseWord("cat") == "tac"
    assert s.TopOfStack == -1


def test5_uses_the_stack(s):
    names = calls_in(s.ReverseWord)
    assert "Push" in names, "ReverseWord() must call Push()."
    assert "Pop" in names, "ReverseWord() must call Pop()."
    for banned in ["reversed", ".reverse"]:
        if banned in names:
            pytest.fail("ReverseWord() uses " + banned + "(). Use the stack instead.")
    tree = ast.parse(textwrap.dedent(inspect.getsource(s.ReverseWord)))
    for node in ast.walk(tree):
        if isinstance(node, ast.Slice) and node.step is not None:
            pytest.fail("ReverseWord() uses [::-1]. Use the stack instead.")
    assert s.ReverseWord("dog") == "god"
