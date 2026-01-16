from convert import convert

def test_convert():
    expected_output = " fahrenticies 77.0"
    assert convert(25) == expected_output
