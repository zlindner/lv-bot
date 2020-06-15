import requests
from time import time, sleep


def check_availability(sku):
    '''Checks the availability of the given SKU'''

    url = 'https://secure.louisvuitton.com/ajaxsecure/getStockLevel.jsp?storeLang=eng-ca&pageType=product&skuIdList=' + sku
    headers = {
        'user-agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'
    }

    try:
        r = requests.get(url, timeout=10, headers=headers)
        r.raise_for_status()
    except Exception as err:
        raise SystemExit(err)

    json = r.json()
    return json[sku]['inStock']

def purchase(sku):
    print('Purchasing %s' %)


if __name__ == '__main__':
    print('### lv-bot v1.0.0 ###\n\n')

    # get sku from user
    print('Enter a SKU: ')
    sku = input().lower()

    # todo get product info
    # selected product: product name
    # is this correct? (y/n)

    print('Automatically purchase if in stock (Y/N): ')
    auto_buy = input().lower()

    if auto_buy != 'y' and auto_buy != 'n':
        print('Invalid option')
        exit()

    # start loop that executes every 60s
    start = time()

    while True:
        # check if the thing is in stock
        in_stock = check_availability(sku)

        print('Avaiability: ', end='', flush=False)

        if in_stock:
            print(f'\033[92In Stock\033[0m')

            if auto_buy:
                
        else:
            print(f'\033[91mOut of Stock\033[0m')

        # sleep for 60 seconds, then run again
        sleep(60.0 - ((time() - start) % 60.0))
