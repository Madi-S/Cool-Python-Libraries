# Cool python libraries

This repositroy demonstrates some of very useful python libraries

Inspired by this [video](https://www.youtube.com/watch?v=eILeIEE3C8c)

## 1) Argh

### Argh installation

As the [docs](https://argh.readthedocs.io/en/latest/) says:

Argh is a smart wrapper for argparse. Argparse is a very powerful tool; Argh just makes it easy to use.

```bash
pip install argh
```

### Argh usage
Code snippets for this module can be found in directory "argh".

For example, a calculator created using argh:
```python
import argh



def calc(expr):
    print(f'Evaluating expression {expr}')
    try:
        return eval(expr)
    except:
        return 'Given algebraic expression is invalid'


if __name__ == '__main__':
    argh.dispatch_command(calc)
```
```html
cd argh

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
```