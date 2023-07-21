import requests


def main():
    response = requests.get(
        'https://outback.60736ldvbpamu.ap-northeast-2.cs.amazonlightsail.com/participation/statistics')
    print(response)
    print(response.headers['Content-Type'])
    print('Content:', response.text)


if __name__ == '__main__':
    main()
