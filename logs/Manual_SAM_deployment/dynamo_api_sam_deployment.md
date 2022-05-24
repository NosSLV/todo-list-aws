Command test logs after first deployment with SAM:

## Create

```shell
curl -X POST https://okkqqzxsqd.execute-api.us-east-1.amazonaws.com/Prod/todos/ --data '{ "text": "Learn Serverless" }'

# log:
{"statusCode": 200, "body": "{\"id\": \"08aa19e0-db43-11ec-8c19-5a4c0e05e8a7\", \"text\": \"Learn Serverless\", \"checked\": false, \"createdAt\": \"1653384149.510069\", \"updatedAt\": \"1653384149.510069\"}"}
```

## List

```shell
curl https://okkqqzxsqd.execute-api.us-east-1.amazonaws.com/Prod/todos/

# log:
[{"checked": false, "createdAt": "1653384149.510069", "text": "Learn Serverless", "id": "08aa19e0-db43-11ec-8c19-5a4c0e05e8a7", "updatedAt": "1653384149.510069"}]
```

## Get

```shell
curl https://okkqqzxsqd.execute-api.us-east-1.amazonaws.com/Prod/todos/08aa19e0-db43-11ec-8c19-5a4c0e05e8a7

# log:
{"checked": false, "createdAt": "1653384149.510069", "text": "Learn Serverless", "id": "08aa19e0-db43-11ec-8c19-5a4c0e05e8a7", "updatedAt": "1653384149.510069"}
```

## Update

```shell

curl -X PUT https://okkqqzxsqd.execute-api.us-east-1.amazonaws.com/Prod/todos/08aa19e0-db43-11ec-8c19-5a4c0e05e8a7 --data '{ "text": "Learn Serverless", "checked": true }'

# log:
{"checked": true, "createdAt": "1653384149.510069", "text": "Learn Serverless", "id": "08aa19e0-db43-11ec-8c19-5a4c0e05e8a7", "updatedAt": 1653384289418}
```

## Delete

```shell
curl -X DELETE https://okkqqzxsqd.execute-api.us-east-1.amazonaws.com/Prod/todos/08aa19e0-db43-11ec-8c19-5a4c0e05e8a7

## log:
# Nothing is showed, but if we go to our DynamoDB service in AWS Console we can see that the item has been deleted from the table "default-TodosDynamoDbTable".
```