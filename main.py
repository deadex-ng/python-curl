import argparse
from urllib.parse import urlparse
from tcp import Client

parser = argparse.ArgumentParser()

parser.add_argument("--url", type=str)
parser.add_argument("-X", type=str)
parser.add_argument("-d", type=str)
parser.add_argument("-H", type=str)
parser.add_argument("-v", action="store_true")
args = parser.parse_args()

if args.X is None:
    args.X = "GET"

parsed_url = urlparse(args.url)

print("> Connecting to ", parsed_url.netloc)
print("> Sending request {} HTTP/1.1".format(args.X))
print("> Host: ", parsed_url.netloc)
print("> Accept: */*")

client = Client(parsed_url.netloc, 443, args.v, args.X, args.H, args.d)
client.connect()
