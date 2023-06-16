# Taskman

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/hs-heilbronn-devsecops-gold/taskman)

# Testing from the command line

## Create a new task

```
curl --request POST --url http://localhost:8000/tasks \
  --header 'Content-Type: application/json' \
  --data '{"name": "my name", "description": "my description"}'
```

