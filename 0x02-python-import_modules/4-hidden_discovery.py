#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    a = "__"
    for i in (dir(hidden_4)):
        if a not in i:
            print(i)
