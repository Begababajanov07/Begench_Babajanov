from webbrowser import get


def get_ranges(*args):

    n = ''
    for i in args:
        if len (i) == 1:
            n = n + str(min(i)) + ','
        else:
            n = n + str(min(i)) + '-' + str(max(i)) + ','
    print('"' + n[:len(n) - 1] + '"')

get_ranges ([1,2,3,4], [7,8], [10])