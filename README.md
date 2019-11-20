# Flask Echo

Sample echo-bot using [Flask](http://flask.pocoo.org/)

## Getting started

```
$ export LINE_CHANNEL_SECRET=YOUR_LINE_CHANNEL_SECRET
$ export LINE_CHANNEL_ACCESS_TOKEN=YOUR_LINE_CHANNEL_ACCESS_TOKEN

$ pip install -r requirements.txt
```

Run WebhookParser sample

```
$ python app.py
```

Run WebhookHandler sample

```
$ python app_with_handler.py
```


## How to run this project

- reverse-proxy this app
- python3 app.py
- set the webhook url in Line Console.
- set the right port in reverse-proxy, default is 1234.


## Line-Api
Futher more detail please visit [Line-API](https://developers.line.biz/en/)
