import sys
import pytest
sys.path.append('../')
from package.string import hello

def test_string():
    output = hello()
    assert output == "Hello World Testing it for another version"
    