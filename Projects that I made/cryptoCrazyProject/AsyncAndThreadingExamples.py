import threading
import requests
import time
import asyncio
import aiohttp


def get_data_sync(urls):
    st = time.time()
    json_array = []
    for url in urls:
        json_array.append(requests.get(url).json())
    et = time.time()
    elapsed_time = et - st
    print("Execution time: ", elapsed_time, " seconds")
    return json_array


class ThreadingDownloader(threading.Thread):  # Kalıtım uyguladık
    json_array = []

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):  # Kendisi thread kütüphanesinin içinde olan bir fonksiyondur.
        response = requests.get(self.url)
        self.json_array.append(response.json())
        print(self.json_array)
        return response.json()


def get_data_threading(urls):
    st = time.time()
    threads = []
    for url in urls:
        t = ThreadingDownloader(url)
        t.start()  # Kendisi thread kütüphanesinin içinde olan bir komuttur.
        threads.append(t)

    for t in threads:
        t.join()  # join dediğimizde iş tamamen bitiyor. Kendisi thread kütüphanesinin içinde olan bir komuttur.
        print(t)

    et = time.time()
    elapsed_time = et - st
    print("Execution time: ", elapsed_time, " seconds")


async def get_data_async_but_as_wrapper(urls):
    # Bu kod, asenkron bir işlevi gerçekleştirmek için Python'un
    # asyncio ve aiohttp kütüphanelerini kullanan bir örnek içeriyor.
    # Bu örnekte, aynı anda birden fazla URL'ye HTTP istekleri yapılıyor
    # ve her isteğin yanıtı alınıp JSON içeriği okunuyor.
    st = time.time()
    json_array = []

    async with aiohttp.ClientSession() as session:  # async with bağlamı, bir nesnenin belirli bir zaman aralığında açık kalmasını sağlar ve işlem sona erdiğinde otomatik olarak kapatır. Bu durumda, HTTP istemcisi otomatik olarak kapatılacak şekilde ayarlanıyor.
        for url in urls:
            async with session.get(url) as resp:  # bu 3 satır her yerde aynıdır. Kopyala yapıştır.
                json_array.append(await resp.json())

    et = time.time()
    elapsed_time = et - st
    print("Execution time: ", elapsed_time, " seconds")
    return json_array


async def get_data(session, url, json_array):
    async with session.get(url) as resp:
        json_array.append(await resp.json())


async def get_data_async_concurrently(urls):
    st = time.time()
    json_array = []

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(get_data(session, url, json_array)))
        await asyncio.gather(*tasks)

    et = time.time()
    elapsed_time = et - st
    print("Execution time: ", elapsed_time, " seconds")
    return json_array


urls = ["https://postman-echo.com/delay/3"] * 5
# get_data_sync(urls)  # 40 sn
# get_data_threading(urls)  # 7 sn
# asyncio.run(get_data_async_but_as_wrapper(urls))  # 22 sn
asyncio.run(get_data_async_concurrently(urls))  # 5 sn anlamamıza gerek olmayan gather ve
# future özelliklerini kullandığımız için en verimlisi bu oldu
