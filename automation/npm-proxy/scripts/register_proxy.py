import os
import sys
from utils import authenticate, create_proxy, log

def main():
    domain = os.getenv("PROXY_DOMAIN")
    forward_port = int(os.getenv("PROXY_PORT"))
    cert_domain = os.getenv("CERT_DOMAIN", domain)
    forward_host = os.getenv("FORWARD_HOST", "127.0.0.1")

    if not domain or not forward_port:
        print("Missing required env vars: PROXY_DOMAIN, PROXY_PORT")
        sys.exit(1)

    token = authenticate()
    create_proxy(token, domain, forward_host, forward_port, cert_domain)

if __name__ == "__main__":
    main()
