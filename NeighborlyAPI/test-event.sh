curl -v -X POST "https://anjanatopiclab1.eastus-1.eventgrid.azure.net/api/events" \
-H "aeg-sas-key: 1gfdG2JIO1c2tMZsFfHAKMDXZ54ru6fxXtgUzDBa9g9DbP9kncwcJQQJ99CFACYeBjFXJ3w3AAABAZEG9CwR" \
-H "Content-Type: application/json" \
-d '[
  {
    "id":"1",
    "eventType":"Neighborly.Test",
    "subject":"test",
    "eventTime":"2026-06-09T12:00:00Z",
    "data":{
      "message":"Hello Event Grid"
    },
    "dataVersion":"1.0"
  }
]'