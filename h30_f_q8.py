#!/usr/bin/env python3
# h30_f_q8.py : 基本情報技術者試験 平成30年度秋 午後問題 問8

from typing import List, Tuple

def compute(expression: str) -> int:
    """数式を計算する。

    Args:
        expression: 計算する数式（例: "2*(34-(5+67)/8)"）

    Returns:
        計算結果
    """
    operators, priorities, values = compute_analysis(expression)
    return compute_calculation(operators, priorities, values)

def compute_analysis(expression: str) -> Tuple[List[str], List[int], List[int]]:
    """数式を解析し、演算子、優先順位、値を抽出する。

    Args:
        expression: 解析する数式

    Returns:
        演算子のリスト、優先順位のリスト、値のリストのタプル
    """
    operators: List[str] = []
    priorities: List[int] = []
    values: List[int] = [0]
    nest: int = 0

    for char in expression:
        if '0' <= char <= '9':
            values[-1] = 10 * values[-1] + int(char)
        elif char in ('+', '-', '*', '/'):
            operators.append(char)
            priorities.append(nest + (1 if char in ('+', '-') else 2))
            values.append(0)
        elif char == '(':
            nest += 10
        elif char == ')':
            nest -= 10

    return operators, priorities, values

def compute_calculation(operators: List[str], priorities: List[int], values: List[int]) -> int:
    """演算子、優先順位、値に基づいて計算結果を算出する。

    Args:
        operators: 演算子のリスト
        priorities: 優先順位のリスト
        values: 値のリスト

    Returns:
        計算結果
    """
    while len(operators) > 0:
        ip = 0
        for i in range(1, len(operators)):
            if priorities[ip] < priorities[i]:
                ip = i

        char = operators[ip]

        if char == '+':
            values[ip] += values[ip + 1]
        elif char == '-':
            values[ip] -= values[ip + 1]
        elif char == '*':
            values[ip] *= values[ip + 1]
        elif char == '/':
            values[ip] = int(values[ip] / values[ip + 1]) # int型にキャスト（元の実装に準ずる）

        for i in range(ip + 1, len(operators)):
            values[i] = values[i + 1]
            operators[i - 1] = operators[i]
            priorities[i - 1] = priorities[i]

        operators.pop()
        priorities.pop()
        values.pop()

    return values[0]

# 実行
expression = "2*(34-(5+67)/8)"
answer = compute(expression)
print("Answer:", answer)