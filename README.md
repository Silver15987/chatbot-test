Example repo using Chatterbot and FastAPI to make an api chatbot

You can run this application in docker using the commands:
```bash
docker build -t chatbot_api
docker run -p 8887:80 chatbot_api
```
You can then go to <localhost:8887/docs> to get to the swagger UI for testing


we can run the docker app at any wanted port, here we will use port 8887 for ui testing.
