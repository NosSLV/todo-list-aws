**Crear red de docker**

```shell
docker network create sam
# Log
e37dda76d46e038b2945ff13f4d627cc16d12c506c0759012550439ae299ebe7
e37dda76d46e   sam             bridge    local
```

**Levantar contenedor de docker**

```shell
docker run -p 8000:8000 --network sam --name dynamodb --network-alias dynamodb -d amazon/dynamodb-local
# Log
0babf8a174080f6f2bd5a7ee4f4d752da5c8cbc6e00b2a1fe935f8dc2483c332
CONTAINER ID   0babf8a17408   
IMAGE    amazon/dynamodb-local                         
COMMAND "java -jar DynamoDBL…"
CREATED About a minute ago  
STATUS Up About a minute                  
PORTS 0.0.0.0:8000->8000/tcp                                    
NAMES dynamodb

```

**Crear tabla en dynamodb local**

```shell
aws dynamodb create-table --table-name local-TodosDynamoDbTable --attribute-definitions AttributeName=id,AttributeType=S --key-schema AttributeName=id,KeyType=HASH --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 --endpoint-url http://localhost:8000
# Log
{
    "TableDescription": {
        "AttributeDefinitions": [
            {
                "AttributeName": "id",
                "AttributeType": "S"
            }
        ],
        "TableName": "local-TodosDynamoDbTable",
        "KeySchema": [
            {
                "AttributeName": "id",
                "KeyType": "HASH"
            }
        ],
        "TableStatus": "ACTIVE",
        "CreationDateTime": 1653306996.986,
        "ProvisionedThroughput": {
            "LastIncreaseDateTime": 0.0,
            "LastDecreaseDateTime": 0.0,
            "NumberOfDecreasesToday": 0,
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        },
        "TableSizeBytes": 0,
        "ItemCount": 0,
        "TableArn": "arn:aws:dynamodb:ddblocal:000000000000:table/local-TodosDynamoDbTable"
    }
}

```

```shell
aws dynamodb list-tables --endpoint-url http://localhost:8000
# Log
{
    "TableNames": [
        "local-TodosDynamoDbTable"
    ]
}
```

**Empaquetar proyecto con SAM**

```shell
sam build --use-container

# Log
Starting Build inside a container
Your template contains a resource with logical ID "ServerlessRestApi", which is a reserved logical ID in AWS SAM. It could result in unexpected behaviors and is not recommended.
Building codeuri: …\Caso_Practico_1\Archivos\repositorio_cp1\src runtime: python3.7 metadata: {} architecture: x86_64 functions: ['CreateTodoFunction', 'ListTodosFunction', 'GetTodoFunction', 'UpdateTodoFunction', 'DeleteTodoFunction']

Fetching public.ecr.aws/sam/build-python3.7:latest-x86_64 Docker container image................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................
Mounting …\Caso_Practico_1\Archivos\repositorio_cp1\src as /tmp/samcli/source:ro,delegated inside runtime container

Build Succeeded

Built Artifacts  : .aws-sam\build
Built Template   : .aws-sam\build\template.yaml

Commands you can use next
=========================
[*] Validate SAM template: sam validate
[*] Invoke Function: sam local invoke
[*] Test Function in the Cloud: sam sync --stack-name {stack-name} --watch
[*] Deploy: sam deploy --guided

Running PythonPipBuilder:ResolveDependencies
Running PythonPipBuilder:CopySource
```

**Levantar la API localmente**

```shell
sam local start-api --port 8081 --env-vars localEnvironment.json --docker-network sam

# Log
Mounting CreateTodoFunction at http://127.0.0.1:8081/todos [POST]
Mounting UpdateTodoFunction at http://127.0.0.1:8081/todos/{id} [PUT]
Mounting DeleteTodoFunction at http://127.0.0.1:8081/todos/{id} [DELETE]
Mounting ListTodosFunction at http://127.0.0.1:8081/todos [GET]
Mounting GetTodoFunction at http://127.0.0.1:8081/todos/{id} [GET]
You can now browse to the above endpoints to invoke your functions. You do not need to restart/reload SAM CLI while working on your functions, changes will be reflected instantly/automatically. You only need to restart SAM CLI if you update your AWS SAM template
2022-05-23 15:29:14  * Running on http://127.0.0.1:8081/ (Press CTRL+C to quit)
Test rápido
Invoking list.list (python3.7)
Image was not found.
Removing rapid images for repo public.ecr.aws/sam/emulation-python3.7
Building image.................................................................................................................................................................................................................................................................................................................................................
Skip pulling image and use local one: public.ecr.aws/sam/emulation-python3.7:rapid-1.50.0-x86_64.

Mounting …\Caso_Practico_1\Archivos\repositorio_cp1\.aws-sam\build\ListTodosFunction as /var/task:ro,delegated inside runtime container
START RequestId: 4c4f94f5-6c7f-44d0-9b91-bf9f677fb10b Version: $LATEST
URL dynamoDB:http://dynamodb:8000
END RequestId: 4c4f94f5-6c7f-44d0-9b91-bf9f677fb10b
REPORT RequestId: 4c4f94f5-6c7f-44d0-9b91-bf9f677fb10b  Init Duration: 0.27 ms  Duration: 984.73 ms     Billed Duration: 985 ms   Memory Size: 128 MB     Max Memory Used: 128 MB
No Content-Type given. Defaulting to 'application/json'.
2022-05-23 15:29:56 127.0.0.1 - - [23/May/2022 15:29:56] "GET /todos HTTP/1.1" 200 -

```

