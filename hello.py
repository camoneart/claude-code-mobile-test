#!/usr/bin/env python3
"""
テスト用のHello Worldプログラム
"""

def greet(name: str = "World") -> str:
    """
    挨拶メッセージを返す

    Args:
        name: 挨拶する相手の名前

    Returns:
        挨拶メッセージ
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
    print(greet("Claude"))
