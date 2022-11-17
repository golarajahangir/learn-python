import requests


ifttt_webhook_url = "https://maker.ifttt.com/trigger/test_event/json/with/key/mlIgTmJsJvG8cb0actBCFcZznfTDpa1FVzg9hLFQXW0"
requests.post(ifttt_webhook_url)