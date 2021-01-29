class Route:
    def __init__(self, path: str, allowed_methods: list = ["get"], response_code: int = 200):
        self.path = path
        self.allowed_methods = allowed_methods
        self.response_code = response_code

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # with open("pakthttp/server/test.html", "r") as html:
        #     self.wfile.write(html.read().encode())
