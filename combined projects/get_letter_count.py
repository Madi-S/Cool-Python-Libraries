import requests
from html2text import HTML2Text
from string import ascii_lowercase
from time import sleep

import argh
from tqdm import tqdm


@argh.arg('url', help='Specify the url')
@argh.arg('letter', help='Specify ASCII letter', choices=ascii_lowercase)
def get_letter_count(url, letter):
    '''Returns the number of occurrences  of given letter'''

    r = requests.get(url)
    if r.ok:
        occurrences = 0

        h = HTML2Text()
        h.ignore_links = True
        h.ignore_links

        pure_text = h.handle(r.text).strip()

        for l in tqdm(pure_text):
            if l == letter:
                occurrences += 1
                sleep(.05)

        return {letter: occurrences}

    return 'Given URL is invalid ' + r


if __name__ == '__main__':
    argh.dispatch_command(get_letter_count)
