# EVM Benchmarks project
# Copyright 2021 The EVM Benchmarks Authors.
# SPDX-License-Identifier: Apache-2.0

from evmbench import *


def test_dry_decode():
    assert dry_decode("") == ""
    assert dry_decode("00") == "00"

    assert dry_decode("(0*ca)") == ""
    assert dry_decode("(1*ca)") == "ca"
    assert dry_decode("(5*ca)") == "cacacacaca"

    assert dry_decode("01(0*3a)02") == "0102"
    assert dry_decode("01(1*3a)02") == "013a02"
    assert dry_decode("01(2*3a)02") == "013a3a02"

    assert dry_decode("01(2*333)02(2*4444)03") == "01333333024444444403"
    assert dry_decode("01(4*333)02(4*4)03") == "0133333333333302444403"

    assert dry_decode("(0*)") == ""
    assert dry_decode("(9*)") == ""

    # invalid syntax
    assert dry_decode("...(ZZ*??)") == "...(ZZ*??)"
    assert dry_decode("(") == "("
    assert dry_decode("*") == "*"
    assert dry_decode(")") == ")"
    assert dry_decode("()") == "()"
    assert dry_decode("(*)") == "(*)"
    assert dry_decode("(*y)") == "(*y)"
    assert dry_decode("(invalid)(2*_valid)") == "(invalid)_valid_valid"
    assert dry_decode(".(X*a).(3*_ok).") == ".(X*a)._ok_ok_ok."


if __name__ == '__main__':
    test_dry_decode()
