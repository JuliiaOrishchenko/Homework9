def count_lines(name):
    file_lines = open(name).readlines()
    return f"lines: {len(file_lines)}"


def count_chars(name):
    file_chars = open(name).read()
    return f"chars: {len(file_chars)}"


def test(name):
    return count_lines(name), count_chars(name)





