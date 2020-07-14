
def remove_consecutive_three(S: str) -> str:
    """
    Remove duplicated characters with no 3 consecutive identical
    characters.
    """
    ans = []
    for i in S:
        if len(ans) > 1 and ans[-1] == ans[-2] == i:
            continue
        ans.append(i)
    return ''.join(ans)


if __name__ == "__main__":
    test = [
        "eedaaad",
        "xxxtxxxx",
        "uuuuxaaaaxuuu"
    ]

    for i in test:
        print(remove_consecutive_three(i))
