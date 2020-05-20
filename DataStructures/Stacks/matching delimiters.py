def is_matched(expression):
    lefty = '{[('
    righty = '}])'
    stack = list()
    for i in expression:
        if i in lefty:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            if righty.index(i) != lefty.index(stack.pop()):
                return False
    return len(stack) == 0


print(is_matched("()(()){([()])}"))
print(is_matched(")(()){([()])}"))
print(is_matched("((()(()){([()])}))"))
