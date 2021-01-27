import sys
import time
import os

stop = 0

while stop == 0:

    try:
        if sys.argv[1] == '-i':
            try:
                os.system('pip install -r requirements.txt')
            except:
                os.system('pip3 install -r requirements.txt')
            break

        if sys.argv[1] == '-help':
            print('\nHow To Use:\npython(3) sp.py -[arg]\n\nARGS:\n-help = help page\n-i = install script librarys\n-test = test script and librarys\n')
            break

        if sys.argv[1] == '-test':
            line_1 = "importing librirys..."

            for x in line_1:
                print(x, end='')
                sys.stdout.flush()
                time.sleep(0.1)

            from lxml import html
            from bs4 import BeautifulSoup
            import requests

            print('done')
            line_2 = "downloading html..."

            for x in line_2:
                print(x, end='')
                sys.stdout.flush()
                time.sleep(0.1)

            url = 'https://github.com/mixgx/SocialParse/blob/main/test.md'
            r = requests.get(url)
            htmlf = r.content.decode()

            print('done')

            line_2 = "finding article with test text..."

            for x in line_2:
                print(x, end='')
                sys.stdout.flush()
                time.sleep(0.1)

            soup = BeautifulSoup(htmlf, features="lxml")
            test = soup.find('article', {'class': 'markdown-body entry-content container-lg'}).text
            test.split()
            test = (test[0] + test[1] + test[2] + test[3])
            print('done')
            if test == 'test':
                print('Everything works fine[✔]')
            else:
                print('Something went wrong[✘]')
                print('Test is not equal to test but equal to "'+test+'"')
            break
    except:
        pass

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    from lxml import html
    from bs4 import BeautifulSoup

    print('\033[33m      _/_/_/                      _/            _/  _/_/_/  \033[31m |https://github.com/mixgx/SocialParse|   ')
    print('\033[33m   _/          _/_/      _/_/_/        _/_/_/  _/  _/    _/    _/_/_/  _/  _/_/    _/_/_/    _/_/    ')
    print('    _/_/    _/    _/  _/        _/  _/    _/  _/  _/_/_/    _/    _/  _/_/      _/_/      _/_/_/_/   ')
    print('       _/  _/    _/  _/        _/  _/    _/  _/  _/        _/    _/  _/            _/_/  _/          ')
    print('_/_/_/      _/_/      _/_/_/  _/    _/_/_/  _/  _/          _/_/_/  _/        _/_/_/      _/_/_/     \033[32m')

    import requests
    url = 'https://github.com/mixgx/SocialParse/blob/main/README.md'
    r = requests.get(url)
    htmlf = r.content.decode()

    soup = BeautifulSoup(htmlf, features="lxml")
    print(soup.find('article', {'class': 'markdown-body entry-content container-lg'}).text)

    break