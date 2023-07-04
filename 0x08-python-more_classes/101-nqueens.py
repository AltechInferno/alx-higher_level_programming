#!/usr/bin/python3
import sys

"""
contains an algorithm that resolves the N-Queen puzzle
using backtracking
"""


def isSafe(m_queen, n_queen):
    """ determines if the queens can or can't kill each other
    Args:
        m_queen: array that has queens positions
        nqueen: queen number
    Returns:
        True: when queens can't kill each other
        False: when some of the queens can kill
    """
    for i in range(n_queen):
        if m_queen[i] == m_queen[n_queen]:
            return False
        if abs(m_queen[i] - m_queen[n_queen]) == abs(i - n_queen):
            return False

    return True


def print_result(m_queen, n_queen):
    """ displays the list with the Queens positions
    Args:
        m_queen: array that has queens positions
        n_queen: queen number
    """
    res = []
    for i in range(n_queen):
        res.append([i, m_queen[i]])
    print(res)


def Queen(m_queen, n_queen):
    """ executes the Backtracking algorithm
    Args:
        m_queen: array has the queens positions
        n_queen: queen number
    """
    if n_queen is len(m_queen):
        print_result(m_queen, n_queen)
        return
    m_queen[n_queen] = -1

    while m_queen[n_queen] < len(m_queen) - 1:
        m_queen[n_queen] += 1
        if isSafe(m_queen, n_queen) is True:

            if n_queen is not len(m_queen):
                Queen(m_queen, n_queen + 1)


def solveNQueen(size):
    """ runs Backtracking algorithm
    Args:
        size: size of chessboard
    """
    m_queen = [-1 for i in range(size)]

    Queen(m_queen, 0)


if __name__ == '__main__':

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solveNQueen(size)

