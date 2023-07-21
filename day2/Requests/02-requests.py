import requests
import secrets


def main():
    payload = {
        "access_key": secrets.API_KEY,
    }
    res = requests.get(
        f"http://api.exchangeratesapi.io/v1/latest", params=payload)

    if not res.status_code == 200:
        print("Error occured!")
        return

    res_dict = res.json()
    success = res_dict['success']
    timestamp = res_dict['timestamp']
    base = res_dict['base']
    KRW = res_dict['rates']['KRW']
    USD = res_dict['rates']['USD']

    print(f'성공코드: {success}')
    print(f'timestamp: {timestamp}')
    print(f'base: {base}')
    print(f'KRW: {KRW}')
    print(f'USD: {USD}')



if __name__ == '__main__':
    main()
