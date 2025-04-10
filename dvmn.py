from dotenv import load_dotenv
from urllib.parse import urlparse
import argparse
import requests
import os


def shorten_link(token, url):
    payload = {
        "access_token": token,
        "url": url,
        "v": "5.199"
    }
    response = requests.post("https://api.vk.ru/method/utils.getShortLink", params=payload)
    response.raise_for_status()
    short_link = response.json()

    if "error" in short_link:
        raise ValueError(f"Ошибка VK API: {short_link['error']['error_msg']}")

    return short_link['response']['short_url']


def count_clicks(token, link):
    payload = {
        "access_token": token,
        "key": link,
        "interval": "forever",
        "v": "5.199"
    }
    response = requests.post("https://api.vk.ru/method/utils.getLinkStats", params=payload)
    response.raise_for_status()
    click_stats_response = response.json()

    if "error" in click_stats_response:
        raise ValueError(f"Ошибка API: {click_stats_response['error']['error_msg']}")

    click_stats = click_stats_response['response']['stats']
    if not click_stats:
        raise ValueError("Ошибка: статистика по ссылке отсутствует")

    return click_stats[0]['views']


def is_shorten_link(url, token):
    payload = {
        "access_token": token,
        "url": url,
        "v": "5.199"
    }
    response = requests.post("https://api.vk.ru/method/utils.checkLink", params=payload)
    response.raise_for_status()
    link_check = response.json()
    if "error" in link_check:
        raise ValueError(f"Ошибка VK API: {link_check['error']['error_msg']}")

    return url == link_check["response"]["link"]

def main():
    parser = argparse.ArgumentParser(description="Обработка ссылок через VK API: сокращение или подсчет кликов.")
    parser.add_argument('url', help="Ссылка для обработки (длинная или короткая)")
    args = parser.parse_args()

    load_dotenv()

    vk_access_token = os.environ["VK_IMPLICIT_FLOW_TOKEN"]

    original_url = args.url

    try:
        if is_shorten_link(original_url, vk_access_token):
            shortened_url = shorten_link(vk_access_token, original_url)
            print(f"Сокращенная ссылка: {shortened_url}")
        else:
            short_link_key = urlparse(original_url).path.lstrip("/")
            click_count = count_clicks(vk_access_token, short_link_key)
            print(f"Ссылка короткая. Количество переходов: {click_count}")

    except ValueError as e:
        print(f"Произошла ошибка: {e}")
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}")


if __name__ == '__main__':
    main()
