# Dowell Permutation API Docs

## Endpoints
### Calculate Permutation
#### POST https://100050.pythonanywhere.com/api/calculateperm/
#### Request
```json
{
    "char": "A"
}
```

#### Response
```json
{
  "permutation": [["A"]]
}
```

### Save Permutation
#### POST https://100050.pythonanywhere.com/api/save/
#### Request
```json
{
  "char":"A"
}
```

#### Response
```json
{
  "saved": "A"
}
```


### Clear Session
#### GET https://100050.pythonanywhere.com/api/clear_session/

#### Response
```json
{
  "response": "Session Cleared"
}
```
