from main import brackets_cutter_regex


def test_simple():
    assert brackets_cutter_regex('esdfd((2esdf)(esdf') == 'esdfd((2esdf)'


def test_simple_2():
    assert brackets_cutter_regex('(esdfd((2esdf)(esdf') == '(esdfd((2esdf)'


def test_simple_3():
    assert brackets_cutter_regex('(esdfd((2esdf)(esdf)') == '(esdfd((2esdf)(esdf)'


def test_simple_4():
    assert brackets_cutter_regex('(asdas)') == '(asdas)'


def test_simple_5():
    assert brackets_cutter_regex('))(())') == '))(())'


def test_without_brackets():
    assert brackets_cutter_regex('asdas') == 'asdas'


def test_with_one_opened_bracket():
    assert brackets_cutter_regex('(asdas') == ''


def test_with_one_closed_bracket():
    assert brackets_cutter_regex('asdas)') == 'asdas)'


def test_with_one_closed_bracket_only():
    assert brackets_cutter_regex(')') == ')'


def test_with_one_closed_bracket_and_one_letter_only():
    assert brackets_cutter_regex('z)') == 'z)'


def test_with_one_opened_bracket_only():
    assert brackets_cutter_regex('(') == ''


def test_with_one_opened_bracket_and_one_letter_only():
    assert brackets_cutter_regex('(z') == ''


def test_empty_string():
    assert brackets_cutter_regex('') == ''
