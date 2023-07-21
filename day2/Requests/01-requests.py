import requests
import secrets


def main():
    res = requests.get(
        f"http://api.exchangeratesapi.io/v1/latest?access_key={secrets.API_KEY}")
    print(res)
    print(res.data)
    print(res.status_code)
    print(res.headers["Content-Type"])
    # 받은 res를 dictionary화해서
    # success는 뭐다
    # timestamp는 몇이다
    # base KRW 기준으로 달러는 얼마다


#
if __name__ == '__main__':
    main()
