import CSP_6_02_reading_files as HW

def test_longestLine():
    assert HW.longestLine('hello.txt') == 'I am a file to be read for this assignment\n'
    assert HW.longestLine('binary.txt') == '0110101010101\n'

def test_toBinary():
    assert HW.toBinary('binary.txt') == ['01101010', '10101010', '10101010', '10101110', '00101101', '01100101', '1101']

