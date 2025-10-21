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


def farewell(name: str = "World") -> str:
    """
    別れの挨拶メッセージを返す

    Args:
        name: 別れを告げる相手の名前

    Returns:
        別れの挨拶メッセージ
    """
    return f"Goodbye, {name}! See you soon!"


def main():
    """メイン関数"""
    print(greet())
    print(greet("Claude"))
    print()
    print(farewell())
    print(farewell("Claude"))


if __name__ == "__main__":
    main()
