import string_utils

class TestStringUtils:

  def test_reverse_string(self):
    assert string_utils.reverse_string("hello") == "olleh"

  def test_capitalize_string(self):
    assert string_utils.capitalize_string("hello") == "Hello"

  def test_is_capitalized(self):
    assert string_utils.is_capitalized("Hello") == True
    assert string_utils.is_capitalized("hello") == False

