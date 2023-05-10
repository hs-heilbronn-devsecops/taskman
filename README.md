# Taskman

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/hhn-secops-projectgrp-vrock/taskman)

# Testing from the command line
## Create a new task

```
curl --request POST --url http://localhost:8000/tasks \
  --header 'Content-Type: application/json' \
  --data '{"name": "my name", "description": "my description"}'
```

