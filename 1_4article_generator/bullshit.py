# -*- coding: UTF-8 -*-
import random
import json

data = json.load(open("data.json", encoding="utf-8"))


def generator(title, length=5000):
    """
    :param title: 文章标题
    :param length: 生成正文的长度
    :return: 返回正文内容
    """
    body = ""
    while len(body) < length:
        num = random.randint(0, 1000)
        if num < 100:
            body += "\r\n"
        elif num < 400:
            body += random.choice(data["famous"]) \
                .replace('a', random.choice(data["before"])) \
                .replace('b', random.choice(data['after']))
        else:
            body += random.choice(data["bosh"])
        body = body.replace("x", title)

    return body


if __name__ == '__main__':
    content = generator("梁杰")
    print(content)
