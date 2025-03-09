from typing import Any

import pytest

from src.decorators import log


@log()
def good_function(x: int, y: int) -> int:
    return x + y


@log()
def bad_function(x: int, y: int) -> float:
    return x / y


def test_good_log(capsys: Any) -> None:
    good_function(5, 7)
    see_logs = capsys.readouterr()
    assert "good_function is ok" in see_logs.out


def test_bad_log(capsys: Any) -> None:
    with pytest.raises(ZeroDivisionError):
        bad_function(1, 0)
    see_logs = capsys.readouterr()
    assert "bad_function error: division by zero" in see_logs.out
    assert "input: (1, 0), {}" in see_logs.out


def test_logs_in_file(tmp_path: Any) -> None:
    logs_file = tmp_path / "test_log.txt"
    func = log(filename=str(logs_file))(good_function)
    func(4, 3)


def test_bad_logs_in_file(tmp_path: Any) -> None:
    log_file = tmp_path / "test_error_log.txt"
    func = log(filename=str(log_file))(bad_function)
    with pytest.raises(ZeroDivisionError):
        func(1, 0)
    with open(log_file) as f:
        log_contents = f.read()
    assert "bad_function error: division by zero" in log_contents
    assert "input: (1, 0), {}" in log_contents
