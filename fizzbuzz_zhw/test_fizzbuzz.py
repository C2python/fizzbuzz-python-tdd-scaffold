#!/usr/bin/python3.7

# -*- coding:utf-8 -*-

# Author: zhangwen1
# Email: zhangwen1@unionpay.com
import pytest
from fizzbuzz import *


def test_fizzbuzz():
    assert(fizzbuzz(10)) == "Fizz"
    assert(fizzbuzz(15)) == "FizzBuzz"
    assert(fizzbuzz(3)) == "Buzz"
    assert(fizzbuzz(2)) is None
