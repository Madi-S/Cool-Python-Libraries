import argh

'''
Since only one funciton is dispatched, there is no need to specify the function name 
'''


def calc(expr):
    print(f'Evaluating expression {expr}')
    try:
        return eval(expr)
    except:
        return 'Given algebraic expression is invalid'


if __name__ == '__main__':
    argh.dispatch_command(calc)

'''
python calc.py -h
    usage: calc.py [-h] expr

    positional arguments:
    expr        -

    optional arguments:
    -h, --help  show this help message and exit


python calc.py 5+5
    Evaluating expression 5+5
    10


python calc.py 2+2*2
    Evaluating expression 2+2*2
    6
'''