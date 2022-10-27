def memorize_func(f):
    memo = dict()

    def func(*args):
        print(f'Run with args={args}, memo={memo}')
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]

    return func