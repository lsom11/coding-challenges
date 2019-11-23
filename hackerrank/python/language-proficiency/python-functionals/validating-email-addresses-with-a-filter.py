import re


def fun(s):
    email_match = re.compile(r'^[a-z0-9_-]+@[a-z0-9]+\.[a-z]{1,3}$')
    return re.match(email_match, s)


def filter_mail(emails):
