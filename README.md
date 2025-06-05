# dmr-adk

[Use the Google (Python) Agent Development Kit with Docker Model Runner](https://k33g.hashnode.dev/use-the-google-python-agent-development-kit-with-docker-model-runner)


## Python environment

Start Devcontainer, then create a virtual environment:

```bash
python -m venv tmp
source tmp/bin/activate
pip install -r requirements.txt
```

## Donatello

Run the example:

```bash
cd agents
adk web
```

```bash
cd agents
adk run donatello
```

```bash
cd agents
adk api_server
```

```bash
curl -X POST http://localhost:8000/apps/donatello/users/bob/sessions/bob_session_42 \
  -H "Content-Type: application/json" \
  -d '{"state": {}}' | jq '.'
```

```bash
curl -X POST http://localhost:8000/run \
-H "Content-Type: application/json" \
-d '{
    "appName": "donatello",
    "userId": "bob",
    "sessionId": "bob_session_42",
    "newMessage": {
        "role": "user",
        "parts": [{
            "text": "What is the best pizza in the world?"
        }]
    }
}' | jq '.'
```


```bash
curl -X POST http://localhost:8000/run_sse \
-H "Content-Type: application/json" \
-d '{
    "appName": "donatello",
    "userId": "bob",
    "sessionId": "bob_session_42",
    "newMessage": {
        "role": "user",
        "parts": [{
            "text": "What is the best pizza in the world?"
        }]
    },"streaming": true
}'
```
