from http.server import HTTPServer, SimpleHTTPRequestHandler


def RedirectFactory(remap):
    class Redirect(SimpleHTTPRequestHandler):
        def __init__(
            self,
            *args,
            directory='/home/pdmurray/Desktop/workspace/custom-ipywidget-example/dist',
            **kwargs
        ):
            self.remap = {} if remap is None else remap
            super().__init__(*args, directory=directory, **kwargs)

        def do_GET(self):
            if self.path in self.remap:
                self.send_response(302)
                self.send_header("Location", self.remap[self.path])
                self.end_headers()

            # if self.path == "/dist/myproject@%5E0.1.0/dist/index.js":
            #     self.send_response(302)
            #     self.send_header("Location", '/index.js')
            #     self.end_headers()
            else:
                super().do_GET()

    return Redirect


port = 8000
httpd = HTTPServer(
    ("", port),
    RedirectFactory(
        {
            "/dist/myproject@%5E0.1.0/dist/index.js": "/index.js",
            "//myproject@%5E0.1.0/dist/index.js": "/index.js",
            "//myproject@%5E0.1.0/dist/index.js": "/index.js",
            "//myproject@%5E0.1.0/dist/index.js.map": "index.js.map",
        }
    )
)
print(f"Serving on port {port}.")
httpd.serve_forever()
