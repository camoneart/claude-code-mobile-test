#!/usr/bin/env python3
"""
hello.pyのテストコード
"""

import unittest
from hello import greet, farewell


class TestGreetings(unittest.TestCase):
    """挨拶関数のテストクラス"""

    def test_greet_default(self):
        """デフォルトの挨拶メッセージをテスト"""
        self.assertEqual(greet(), "Hello, World!")

    def test_greet_with_name(self):
        """名前を指定した挨拶メッセージをテスト"""
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_farewell_default(self):
        """デフォルトの別れのメッセージをテスト"""
        self.assertEqual(farewell(), "Goodbye, World! See you soon!")

    def test_farewell_with_name(self):
        """名前を指定した別れのメッセージをテスト"""
        self.assertEqual(farewell("Bob"), "Goodbye, Bob! See you soon!")


if __name__ == "__main__":
    unittest.main()
