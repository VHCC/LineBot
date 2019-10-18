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


### How to run this project

1. reverse-proxy this app
2. python3 app.py
3. set the webhook url in Line Console.
4. set the right port in reverse-proxy, it's 1234


## Line-Api
Futher more detail please visit [Line-API](https://developers.line.biz/en/)
