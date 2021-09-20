def test_widget_functions_as_expected():
    assert True


def test_widget_fails():
    assert False


def example_assert_verification():
    A = 1
    B = 2
    sum = A+B
    print(type(sum))
    if sum == 3:
        assert True
    else: assert False
