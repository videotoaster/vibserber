import argparse

parser = argparse.ArgumentParser(description="This script runs an http server on the specified port and host.")

parser.add_argument('port',
                    metavar='port',
                    type=int,
                    help='Port to run server on.'
                    )
parser.add_argument('host',
                    metavar='host',
                    type=str,
                    help='Host to run server on.'
                    )
parser.add_argument('debug',
                    metavar='debug',
                    type=bool,
                    help='Enable debug output.'
                    )

from pakthttp.server.server import HttpServer

args = parser.parse_args()

server = HttpServer(args.host, args.port)
print(f"[-] Starting Pakt HTTP server on host {args.host} and port {args.port}")
try:
    print(server.serve_forever())
except KeyboardInterrupt:
    print("\n[!] Received interrupt.")