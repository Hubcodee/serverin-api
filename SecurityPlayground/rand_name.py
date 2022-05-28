import requests
import random
port_used = set()


def words_fetch():
    url = "https://svnweb.freebsd.org/csrg/share/dict/propernames?revision=61767&view=co"

    names = requests.get(url).text

    words = names.split()

    name = random.choice(words)
    return name


def random_port():
    port = random.randint(30000, 32767)
    if(port in port_used):
        port = random.randint(30000, 32767)
    port_used.add(port)
    return port
