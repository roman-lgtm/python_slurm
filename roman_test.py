import pytest
from io import StringIO
from contextlib import redirect_stdout

from homework import matrix


@pytest.mark.parametrize(
    'rows, numbers',
    [
        (3, 4),
        (1, 1),
        (5, 2)
    ]
)
def test_matrix_positive(rows, numbers):
    """Проверяем правильную работу функции"""
    with StringIO() as buf, redirect_stdout(buf):
        matrix(rows, numbers)
        output = buf.getvalue().strip()
        expected_output = '\\n'.join([' '.join(map(str, range(i * numbers + 1, (i+1)*numbers + 1))) for i in range(rows)])
        assert output == expected_output


@pytest.mark.parametrize(
    'rows, numbers, error_message',
    [
        (-1, 3, "Количество строк должно быть положительным целым числом"),
        (3, -1, "Количество чисел в строке должно быть положительным целым числом"),
        ("a", 3, "Количество строк должно быть положительным целым числом"),
        (3, "b", "Количество чисел в строке должно быть положительным целым числом")
    ]
)
def test_matrix_errors(rows, numbers, error_message):
    """Тестируем обработку ошибок"""
    with pytest.raises(ValueError) as excinfo:
        matrix(rows, numbers)
    assert str(excinfo.value) == error_message
