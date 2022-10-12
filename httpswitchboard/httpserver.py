from http.server import HTTPServer, SimpleHTTPRequestHandler


class Redirect(SimpleHTTPRequestHandler):

    remap = {}
    directory = ''

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super().__init__(*args, directory=self.directory, **kwargs)

    def redirect(self):
        self.send_response(302)
        self.send_header("Location", self.remap[self.path])
        self.end_headers()

    def do_GET(self):
        if self.path in self.remap:
            self.redirect()

        else:
            super().do_GET()


class RedirectServer(HTTPServer):
    def __init__(self, *args, directory, remap, **kwargs):
        Redirect.remap = remap
        Redirect.directory = directory
        super().__init__(
            *args,
            Redirect,
            **kwargs
        )
