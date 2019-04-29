from pprint import pprint
from json_requests import JsonRequests


def main():
    requests = JsonRequests(auth=('testuser', 'TESTPASS'), params={ 'qsname': 'qsvalue' })
    result = requests.get('https://httpbin.org/get')
    pprint(result)


if __name__ == '__main__':
    main()
