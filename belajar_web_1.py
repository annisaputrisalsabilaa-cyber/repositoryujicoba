#membuat website
#belajar_web_1.py

import wsgiref.simple_server

def application(environ, start_response):
    #response
    response = b"hallo world"

    #status respon
    status = "200 ok"

    #header respon
    headers = [("Content-Type", "text/html")]

    #pengaturan status dan header
    start_response(status, headers)

    return [response]

    if __name__ =="__main__":

        w_s = wsgiref.simple_server.make_server(
            host = "localhost",
            port = 8021,
            app = application
        )

        w_s.handle.request()
