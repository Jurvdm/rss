import urllib.parse as urlparse

def application(environ, start_response):
    status = '200 OK'
    response_header = [('Content-type', 'text/html')]
    start_response(status, response_header)

    html = ''
    html += '<html>\n'
    html += '  <body>\n'
    html += '    <title>Test WSGI page for fys</title>\n'
    html += '    <div style="width: 100%; font-size: 20px; font-weight: bold; text-align: center;">\n'
    html += '      Welcome to the mod_wsgi test page\n'
    html += '    </div>\n'

    html += 'You are logged in.\n'

    html += '    <h2>Some interesting environment variables:</h2>\n'
    html += '    <div style="width: 100%; font-family: Courier; font-size: 14px; font-weight: bold; text-align: left;">\n'

    html += '   <h2>Request parameters</h2>\n'
    html += '   <div style="width: 100%; font-family: Courier; font-size: 14px; font-weight: bold; text-align: left;">\n'
    # check HTTP request method and get parameters from requestmethod = environ.get('REQUEST_METHOD', '')
    method = environ.get('REQUEST_METHOD', '')

    params = {}
    if method == 'GET':
        params = urlparse.parse_qs(environ['QUERY_STRING'])
    elif method == 'POST':
        input = environ['wsgi.input'].read().decode()
        params = urlparse.parse_qs(input)

    html += 'Userid: ' + params.get('userid', [''])[0] + '<br>\n'
    html += 'Password: ' + params.get('password', [''])[0] + '<br>\n'

    html += ' </div>\n'

    environmentVars = ['REQUEST_METHOD', 'REQUEST_URI', 'QUERY_STRING', 'SCRIPT_NAME', 'HTTP_REFERER']
    for envVar in environmentVars:
        envVarValue = environ.get(envVar, '')
        html += envVar + ' = ' + envVarValue + '<br>\n'

    html += '    </div>\n'
    html += '  </body>\n'
    html += '</html>\n'

    return [bytes(html, 'utf-8')]

if __name__ == '__main__':
    page = application({}, print)
    print(page[0].decode())

