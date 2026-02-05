def tree(label, branchs=[]):
    for branch in branchs:
        assert is_tree(branch), 'branch must be tree'
    return [label] + list(branchs)

def label(tree):
    return tree[0]

def branchs(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branchs(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branchs(tree)

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left) + label(right), [left, right])
    
def count_leaves(t):
    if is_leaf(t):
        return 1
    # sum = 0
    # for branch in branchs(t):
    #     sum += count_leaves(branch)
    # return sum
    branch_counts = [count_leaves(b) for b in branchs(t)]
    return sum(branch_counts)

def leaves(t):
    """
    return a list contain labels of leave node in t
    """
    if is_leaf(t):
        return [label(t)]
    else:
        return sum(leaves(b) for b in branchs(t))

def increment_leaves(t):
    if is_leaf(t):
        return tree(label(t)+1)
    bs = [increment_leaves(b) for b in branchs(t)]
    return tree(label(t), bs)

def increment(t):
    return tree(label(t)+1, [increment(b) for b in branchs(t)])

def print_tree(t, indent=0):
    print(' ' * indent + str(label(t)))
    for b in branchs(t):
        print_tree(b, indent+1)

def count_path(t, total):
    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum([count_path(b, total-label(t)) for b in branchs(t)])

