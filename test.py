# test.py
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]  # Ten en cuenta que corregí el typo aquí

