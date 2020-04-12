s = "+(+(5)(2))(-(2)(3))"
l = ['+', ['+', 5, 2], ['-', 2, 3]]

def parse(s):
    global i, tree
    if s[i].isdigit():
        j = i + 1
        while s[j].isdigit():
            j += 1
        tree = int(s[i:j])
        i = j
    elif s[i] == '+':
        i += 2
        x = parse(s)
        i += 2
        y = parse(s)
        i += 1
        tree = ['+', x, y]
    elif s[i] == '-':
        i += 2
        x = parse(s)
        i += 2
        y = parse(s)
        i += 1
        tree = ['-', x, y]

    return tree

def myEval(tree):
    if type(tree) == int:
        ans = tree
    else:
        x = myEval(tree[1])
        y = myEval(tree[2])
        ans = x + y if tree[0] == '+' else x - y
    return ans

def prettyPrint(tree):
    if type(tree) == int:
        ans = str(tree)
    else:
        op = tree[0]
        x = prettyPrint(tree[1])
        y = prettyPrint(tree[2])
        ans = "({}{}{})".format(x, op, y)
    return ans

def checkParse(s):
    if 
    else:
        ans = False

    return ans

i = 0
r = parse(s)
print(r)
print(myEval(r))
print(prettyPrint(r))
