#!usr/bin/python3
""" A script that 
- fetches a link and
- uses a urllib package"""
"""


if __name___ = '__main__':
    import urllib.request

    with
urllib.request.urlopen('https://intranet.hbtn.io/status') as resp:
    content = resp.read()
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".for.at(content))
    print("\t- utf8 content:{}".format(content.decode('utf-8')))
