import argh
import requests
from bs4 import BeautifulSoup


@argh.arg('url', help='URL to website, please provide full URL')
@argh.arg('-t', '--tag', choices=['p', 'h1', 'div', 'span'], default='p', help='Choose a tag to count, by default "p"')
@argh.arg('--verbose', '-v', help='Show more data')
def get_tag_count_from_url(url, tag=None, verbose=False):
    '''This is help text: this function will retrieve the number of given tag occurences'''
    r = requests.get(url)
    if verbose:
        print(f'Response: {r}')

    if r.ok:
        soup = BeautifulSoup(r.text, 'lxml')
        if verbose:
            print('Soup created')
        return len(soup.find_all(tag))

    else:
        return f'URL {url} is invalid'

if __name__ == '__main__':
    argh.dispatch_command(get_tag_count_from_url)


'''
python advanced.py --help
    usage: advanced.py [-h] [-t {p,h1,div,span}] [--verbose] url

    This is help text: this function will retrieve the number of given tag occurences

    positional arguments:
    url                   URL to website, please provide full URL

    optional arguments:
    -h, --help            show this help message and exit
    -t {p,h1,div,span}, --tag {p,h1,div,span}
                            Choose a tag to count, by default "p" (default: 'p')
    --verbose, -v         Show more data (default: False)


python advanced.py https://argh.readthedocs.io/en/latest/ -t div
    55


python advanced.py https://argh.readthedocs.io/en/latest/ -t h1 --verbose
    Response: <Response [200]>
    Soup created
    2


python advanced.py https://argh.readthedocs.io/en/latest/ -t blabla --verbose
    usage: advanced.py [-h] [-t {p,h1,div,span}] [--verbose] url
    advanced.py: error: argument -t/--tag: invalid choice: 'blabla' (choose from 'p', 'h1', 'div', 'span')
'''