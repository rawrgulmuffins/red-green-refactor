from calc import INTEGER, Token


def test_token_can_be_instantiated_with_known_values():
    """
    Test that a :class:`Token` with known good initialization values can be
    instantiated.
    """
    token = Token(type=INTEGER, value=2)
    assert token.value == 2
    assert token.type == INTEGER


def test_token_can_be_converted_to_str():
    """
    Test that a :class:`Token` can be converted into a string, even when
    instantiated with a non-string value such as an integer.
    """
    token = Token(type=INTEGER, value=2)
    expected_result = "Token(type=INTEGER, value=2)"
    assert str(token) == expected_result
