Command test logs after local deployment:

## Create

```shell
curl -X POST http://127.0.0.1:8081/todos --data '{ "text": "Learn Serverless" }'

## Log
{"statusCode": 200, "body": "{\"id\": \"fb5fcfb6-dab9-11ec-8b2e-0242ac110002\", \"text\": \"Learn Serverless\", \"checked\": false, \"createdAt\": \"1653325286.2754197\", \"updatedAt\": \"1653325286.2754197\"}"}
```

## List
```shell
curl http://127.0.0.1:8081/todos

## Log
[{"checked": false, "createdAt": "1653325286.2754197", "id": "fb5fcfb6-dab9-11ec-8b2e-0242ac110002", "text": "Learn Serverless", "updatedAt": "1653325286.2754197"}]
```

## Get
```shell
curl http://127.0.0.1:8081/todos/fb5fcfb6-dab9-11ec-8b2e-0242ac110002

## Log
{"checked": false, "createdAt": "1653325286.2754197", "id": "fb5fcfb6-dab9-11ec-8b2e-0242ac110002", "text": "Learn Serverless", "updatedAt": "1653325286.2754197"}
```

## Update
```shell
curl -X PUT http://127.0.0.1:8081/todos/fb5fcfb6-dab9-11ec-8b2e-0242ac110002 --data '{ "text": "Learn Serverless", "checked": true }'

## Log
{"createdAt": "1653325286.2754197", "checked": true, "id": "fb5fcfb6-dab9-11ec-8b2e-0242ac110002", "text": "Learn Serverless", "updatedAt": 1653325454186}
```

## Delete
```shell
curl -X DELETE http://127.0.0.1:8081/todos/fb5fcfb6-dab9-11ec-8b2e-0242ac110002

## Log
# Nothing showed but in the API log we can see:
2022-05-23 19:04:50 127.0.0.1 - - [23/May/2022 19:04:50] "DELETE /todos/fb5fcfb6-dab9-11ec-8b2e-0242ac110002 HTTP/1.1" 200 -
```

