import urllib.parse as urlparse
import logging

def application(environ, start_response):
    logging.error("HELP IK ZIT ONDER WATER!")
    status = '200 OK'
    response_header = [('Content-type', 'text/html')]
    start_response(status, response_header)

    # check HTTP request method and get parameters from requestmethod = environ.get('REQUEST_METHOD', '')
    method = environ.get('REQUEST_METHOD', '')

    params = {}
    if method == 'GET':
        params = urlparse.parse_qs(environ['QUERY_STRING'])
    elif method == 'POST':
        input = environ['wsgi.input'].read().decode()
        params = urlparse.parse_qs(input)

    Userid = params.get('Gebruikersnaam', [''])[0]
    Password = params.get('Wachtwoord', [''])[0]
    
# Maak dit relatief en niet absoluut
    if Userid == 'Jur' and Password == '123':
        fp = open('var/www/fys/calc.html', 'r')
        html = fp.read()
    else:
        fp = open('var/www/fys/websitefout.html', 'r')
        html = fp.read()

    return [bytes(html, 'utf-8')]

if __name__ == '__main__':
    page = application({}, print)
    print(page[0].decode())

