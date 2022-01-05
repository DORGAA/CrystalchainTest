import requests


def getTopicCount(topic):
    response = requests.get(f'https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page={topic}')
    txt = response.json().get('parse', {}).get('text', {}).get('*', {})
    if not txt:
        return 'Topic Not Found'

    return txt.count(topic)


if __name__ == '__main__':
    print(getTopicCount('pizza'))
