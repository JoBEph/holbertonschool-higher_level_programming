#!/usr/bin/env python3
"""basic Python script to fetch posts from JSONPlacehold"""

import requests
import csv


def fetch_and_print_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print(f'status_code: {response.status_code}')

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    status_code = response.status_code
    posts = response.json()
    data = [
        {'id': post['id'], 'title': post['title'], 'body': post['body']}
        for post in posts
    ]
    with open('posts.csv', 'w', newline="", encoding="utf-8") as fcsv:
        writer = csv.DictWriter(fcsv, fieldnames=['id', 'title', 'body'])
        writer.writeheader()
        writer.writerows(data)

    print('posts have been saved to posts.csv')
