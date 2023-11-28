from flask import g


def set_my_request_var(name: str, value: any):
    if 'my_req_var' not in g:
        g.my_req_var = {}

    g.my_req_var[name] = value
