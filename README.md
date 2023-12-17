# python-curl
This is a basic implementation of curl in Python. This has been developed using [httpbin](https://eu.httpbin.org/?utm_source=substack&utm_medium=email#/HTTP_Methods) for testing it supports the methods we want to test.

## Supported Methods

### GET
To perform a get request

```
$ python3 main.py --url https://eu.httpbin.org/get
> Connecting to  eu.httpbin.org
> Sending request GET HTTP/1.1
> Host:  eu.httpbin.org
> Accept: */*


{
  "args": {}, 
  "headers": {
    "Host": "eu.httpbin.org", 
    "X-Amzn-Trace-Id": "Root=1-657ecfb8-217fe3c973968c59380f407d"
  }, 
  "origin": "105.234.162.40", 
  "url": "http://eu.httpbin.org/get"
}
```
add `-v` for verbose output

```
$ python3 main.py --url https://eu.httpbin.org/get -v
> Connecting to  eu.httpbin.org
> Sending request GET HTTP/1.1
> Host:  eu.httpbin.org
> Accept: */*


HTTP/1.1 200 OK
Date: Sun, 17 Dec 2023 10:40:13 GMT
Content-Type: application/json
Content-Length: 205
Connection: keep-alive
Server: gunicorn/19.9.0
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true

{
  "args": {}, 
  "headers": {
    "Host": "eu.httpbin.org", 
    "X-Amzn-Trace-Id": "Root=1-657ed00d-02f536750b52a7922579b4e2"
  }, 
  "origin": "105.234.162.40", 
  "url": "http://eu.httpbin.org/get"
}
```

If you don't specify the method, it defaults to GET request
```
$ python3 main.py --url https://eu.httpbin.org/get -v -X GET
> Connecting to  eu.httpbin.org
> Sending request GET HTTP/1.1
> Host:  eu.httpbin.org
> Accept: */*


HTTP/1.1 200 OK
Date: Sun, 17 Dec 2023 10:40:58 GMT
Content-Type: application/json
Content-Length: 205
Connection: keep-alive
Server: gunicorn/19.9.0
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true

{
  "args": {}, 
  "headers": {
    "Host": "eu.httpbin.org", 
    "X-Amzn-Trace-Id": "Root=1-657ed03a-378b696d641e9dd93d1f3412"
  }, 
  "origin": "105.234.162.40", 
  "url": "http://eu.httpbin.org/get"
}
```

### DELETE
To perform a delete request

```
$ python3 main.py --url https://eu.httpbin.org/delete -v -X DELETE
> Connecting to  eu.httpbin.org
> Sending request DELETE HTTP/1.1
> Host:  eu.httpbin.org
> Accept: */*


HTTP/1.1 200 OK
Date: Sun, 17 Dec 2023 10:42:50 GMT
Content-Type: application/json
Content-Length: 271
Connection: keep-alive
Server: gunicorn/19.9.0
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true

{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Host": "eu.httpbin.org", 
    "X-Amzn-Trace-Id": "Root=1-657ed0aa-03e5ee1c6585f19119d47317"
  }, 
  "json": null, 
  "origin": "105.234.162.40", 
  "url": "http://eu.httpbin.org/delete"
}
```

### POST
To perform a post request

```
$ python3 main.py --url https://eu.httpbin.org/post -X POST -H "Content-Type: application/json" -d '{"key": "value"}'
> Connecting to  eu.httpbin.org
> Sending request POST HTTP/1.1
> Host:  eu.httpbin.org
> Accept: */*
args": {}, 
  "data": "{\"key\": \"value\"}", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "application/json", 
    "Content-Length": "16", 
    "Content-Type": "application/json", 
    "Host": "eu.httpbin.org", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0", 
    "X-Amzn-Trace-Id": "Root=1-657ed159-60da5db76ae3a0bc38013d9f"
  }, 
  "json": {
    "key": "value"
  }, 
  "origin": "105.234.162.40", 
  "url": "https://eu.httpbin.org/post"
}
```


