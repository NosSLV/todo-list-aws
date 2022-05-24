## Log SAM Build

```Bash
voclabs:~/todo-list-aws (feature) $ sam build

# log

        SAM CLI now collects telemetry to better understand customer needs.

        You can OPT OUT and disable telemetry collection by setting the
        environment variable SAM_CLI_TELEMETRY=0 in your shell.
        Thanks for your help!

        Learn More: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-telemetry.html

Building codeuri: /home/ubuntu/todo-list-aws/src runtime: python3.7 metadata: {} architecture: x86_64 functions: ['CreateTodoFunction', 'ListTodosFunction', 'GetTodoFunction', 'UpdateTodoFunction', 'DeleteTodoFunction']
Running PythonPipBuilder:ResolveDependencies
Running PythonPipBuilder:CopySource

Build Succeeded

Built Artifacts  : .aws-sam/build
Built Template   : .aws-sam/build/template.yaml

Commands you can use next
=========================
[*] Invoke Function: sam local invoke
[*] Deploy: sam deploy --guided
    

SAM CLI update available (1.50.0); (1.33.0 installed)
To download: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html
```

## Log SAM deploy

```Bash
voclabs:~/todo-list-aws (feature) $ sam deploy --guided

# Log:

Configuring SAM deploy
======================

        Looking for config file [samconfig.toml] :  Found
        Reading default arguments  :  Success

        Setting default arguments for 'sam deploy'
        =========================================
        Stack Name [todo-list-aws]: 
        AWS Region [us-east-1]: 
        Parameter Stage [default]: 
        #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
        Confirm changes before deploy [y/N]: y
        #SAM needs permission to be able to create roles to connect to the resources in your template
        Allow SAM CLI IAM role creation [Y/n]: y
        CreateTodoFunction may not have authorization defined, Is this okay? [y/N]: y
        ListTodosFunction may not have authorization defined, Is this okay? [y/N]: y
        GetTodoFunction may not have authorization defined, Is this okay? [y/N]: y
        UpdateTodoFunction may not have authorization defined, Is this okay? [y/N]: y
        DeleteTodoFunction may not have authorization defined, Is this okay? [y/N]: y
        Save arguments to configuration file [Y/n]: Y
        SAM configuration file [samconfig.toml]: 
        SAM configuration environment [default]: 

        Looking for resources needed for deployment:
        Creating the required resources...
        Successfully created!
         Managed S3 bucket: aws-sam-cli-managed-default-samclisourcebucket-oa1orr9izdgy
         A different default S3 bucket can be set in samconfig.toml

        Saved arguments to config file
        Running 'sam deploy' for future deployments will use the parameters saved above.
        The above parameters can be changed by modifying samconfig.toml
        Learn more about samconfig.toml syntax at 
        https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-config.html

Uploading to todo-list-aws/87f479ab562f5257ae240e7adc755c6c  461312 / 461312  (100.00%)
File with same data already exists at todo-list-aws/87f479ab562f5257ae240e7adc755c6c, skipping upload
File with same data already exists at todo-list-aws/87f479ab562f5257ae240e7adc755c6c, skipping upload
File with same data already exists at todo-list-aws/87f479ab562f5257ae240e7adc755c6c, skipping upload
File with same data already exists at todo-list-aws/87f479ab562f5257ae240e7adc755c6c, skipping upload

        Deploying with following values
        ===============================
        Stack name                   : todo-list-aws
        Region                       : us-east-1
        Confirm changeset            : True
        Deployment s3 bucket         : aws-sam-cli-managed-default-samclisourcebucket-oa1orr9izdgy
        Capabilities                 : ["CAPABILITY_IAM"]
        Parameter overrides          : {"Stage": "default"}
        Signing Profiles             : {}

Initiating deployment
=====================
Uploading to todo-list-aws/a542b0bc2444103a3223088aa22c9a6e.template  4310 / 4310  (100.00%)

Waiting for changeset to be created..

CloudFormation stack changeset
-----------------------------------------------------------------------------------------------------------------------------
Operation                       LogicalResourceId               ResourceType                    Replacement                   
-----------------------------------------------------------------------------------------------------------------------------
+ Add                           CreateTodoFunctionCreatePermi   AWS::Lambda::Permission         N/A                           
                                ssionProd                                                                                     
+ Add                           CreateTodoFunction              AWS::Lambda::Function           N/A                           
+ Add                           DeleteTodoFunctionCreatePermi   AWS::Lambda::Permission         N/A                           
                                ssionProd                                                                                     
+ Add                           DeleteTodoFunction              AWS::Lambda::Function           N/A                           
+ Add                           GetTodoFunctionCreatePermissi   AWS::Lambda::Permission         N/A                           
                                onProd                                                                                        
+ Add                           GetTodoFunction                 AWS::Lambda::Function           N/A                           
+ Add                           ListTodosFunctionCreatePermis   AWS::Lambda::Permission         N/A                           
                                sionProd                                                                                      
+ Add                           ListTodosFunction               AWS::Lambda::Function           N/A                           
+ Add                           ServerlessRestApiDeployment14   AWS::ApiGateway::Deployment     N/A                           
                                1b842de6                                                                                      
+ Add                           ServerlessRestApiProdStage      AWS::ApiGateway::Stage          N/A                           
+ Add                           ServerlessRestApi               AWS::ApiGateway::RestApi        N/A                           
+ Add                           TodosDynamoDbTable              AWS::DynamoDB::Table            N/A                           
+ Add                           UpdateTodoFunctionCreatePermi   AWS::Lambda::Permission         N/A                           
                                ssionProd                                                                                     
+ Add                           UpdateTodoFunction              AWS::Lambda::Function           N/A                           
-----------------------------------------------------------------------------------------------------------------------------

Changeset created successfully. arn:aws:cloudformation:us-east-1:840621790817:changeSet/samcli-deploy1653381945/2abc1fb7-42bb-4bc2-bf76-d3ed52d7c257


Previewing CloudFormation changeset before deployment
======================================================
Deploy this changeset? [y/N]: y

2022-05-24 08:53:34 - Waiting for stack create/update to complete

CloudFormation events from changeset
-----------------------------------------------------------------------------------------------------------------------------
ResourceStatus                  ResourceType                    LogicalResourceId               ResourceStatusReason          
-----------------------------------------------------------------------------------------------------------------------------
CREATE_IN_PROGRESS              AWS::DynamoDB::Table            TodosDynamoDbTable              -                             
CREATE_IN_PROGRESS              AWS::DynamoDB::Table            TodosDynamoDbTable              Resource creation Initiated   
CREATE_COMPLETE                 AWS::DynamoDB::Table            TodosDynamoDbTable              -                             
CREATE_IN_PROGRESS              AWS::Lambda::Function           DeleteTodoFunction              -                             
CREATE_IN_PROGRESS              AWS::Lambda::Function           GetTodoFunction                 -                             
CREATE_IN_PROGRESS              AWS::Lambda::Function           CreateTodoFunction              -                             
CREATE_IN_PROGRESS              AWS::Lambda::Function           ListTodosFunction               -                             
CREATE_IN_PROGRESS              AWS::Lambda::Function           UpdateTodoFunction              -                             
CREATE_IN_PROGRESS              AWS::Lambda::Function           GetTodoFunction                 Resource creation Initiated   
CREATE_IN_PROGRESS              AWS::Lambda::Function           DeleteTodoFunction              Resource creation Initiated   
CREATE_IN_PROGRESS              AWS::Lambda::Function           ListTodosFunction               Resource creation Initiated   
CREATE_IN_PROGRESS              AWS::Lambda::Function           CreateTodoFunction              Resource creation Initiated   
CREATE_IN_PROGRESS              AWS::Lambda::Function           UpdateTodoFunction              Resource creation Initiated   
CREATE_COMPLETE                 AWS::Lambda::Function           DeleteTodoFunction              -                             
CREATE_COMPLETE                 AWS::Lambda::Function           GetTodoFunction                 -                             
CREATE_COMPLETE                 AWS::Lambda::Function           CreateTodoFunction              -                             
CREATE_COMPLETE                 AWS::Lambda::Function           ListTodosFunction               -                             
CREATE_COMPLETE                 AWS::Lambda::Function           UpdateTodoFunction              -                             
CREATE_IN_PROGRESS              AWS::ApiGateway::RestApi        ServerlessRestApi               -                             
CREATE_IN_PROGRESS              AWS::ApiGateway::RestApi        ServerlessRestApi               Resource creation Initiated   
CREATE_COMPLETE                 AWS::ApiGateway::RestApi        ServerlessRestApi               -                             
CREATE_IN_PROGRESS              AWS::Lambda::Permission         GetTodoFunctionCreatePermissi   -                             
                                                                onProd                                                        
CREATE_IN_PROGRESS              AWS::Lambda::Permission         GetTodoFunctionCreatePermissi   Resource creation Initiated   
                                                                onProd                                                        
CREATE_IN_PROGRESS              AWS::Lambda::Permission         UpdateTodoFunctionCreatePermi   -                             
                                                                ssionProd                                                     
CREATE_IN_PROGRESS              AWS::ApiGateway::Deployment     ServerlessRestApiDeployment14   -                             
                                                                1b842de6                                                      
CREATE_IN_PROGRESS              AWS::Lambda::Permission         DeleteTodoFunctionCreatePermi   -                             
                                                                ssionProd                                                     
CREATE_IN_PROGRESS              AWS::Lambda::Permission         CreateTodoFunctionCreatePermi   -                             
                                                                ssionProd                                                     
CREATE_IN_PROGRESS              AWS::Lambda::Permission         UpdateTodoFunctionCreatePermi   Resource creation Initiated   
                                                                ssionProd                                                     
CREATE_IN_PROGRESS              AWS::Lambda::Permission         DeleteTodoFunctionCreatePermi   Resource creation Initiated   
                                                                ssionProd                                                     
CREATE_IN_PROGRESS              AWS::Lambda::Permission         CreateTodoFunctionCreatePermi   Resource creation Initiated   
                                                                ssionProd                                                     
CREATE_IN_PROGRESS              AWS::Lambda::Permission         ListTodosFunctionCreatePermis   -                             
                                                                sionProd                                                      
CREATE_IN_PROGRESS              AWS::Lambda::Permission         ListTodosFunctionCreatePermis   Resource creation Initiated   
                                                                sionProd                                                      
CREATE_IN_PROGRESS              AWS::ApiGateway::Deployment     ServerlessRestApiDeployment14   Resource creation Initiated   
                                                                1b842de6                                                      
CREATE_COMPLETE                 AWS::ApiGateway::Deployment     ServerlessRestApiDeployment14   -                             
                                                                1b842de6                                                      
CREATE_IN_PROGRESS              AWS::ApiGateway::Stage          ServerlessRestApiProdStage      -                             
CREATE_IN_PROGRESS              AWS::ApiGateway::Stage          ServerlessRestApiProdStage      Resource creation Initiated   
CREATE_COMPLETE                 AWS::ApiGateway::Stage          ServerlessRestApiProdStage      -                             
CREATE_COMPLETE                 AWS::Lambda::Permission         GetTodoFunctionCreatePermissi   -                             
                                                                onProd                                                        
CREATE_COMPLETE                 AWS::Lambda::Permission         UpdateTodoFunctionCreatePermi   -                             
                                                                ssionProd                                                     
CREATE_COMPLETE                 AWS::Lambda::Permission         DeleteTodoFunctionCreatePermi   -                             
                                                                ssionProd                                                     
CREATE_COMPLETE                 AWS::Lambda::Permission         CreateTodoFunctionCreatePermi   -                             
                                                                ssionProd                                                     
CREATE_COMPLETE                 AWS::Lambda::Permission         ListTodosFunctionCreatePermis   -                             
                                                                sionProd                                                      
CREATE_COMPLETE                 AWS::CloudFormation::Stack      todo-list-aws                   -                             
-----------------------------------------------------------------------------------------------------------------------------

CloudFormation outputs from deployed stack
--------------------------------------------------------------------------------------------------------------------------------
Outputs                                                                                                                        
--------------------------------------------------------------------------------------------------------------------------------
Key                 BaseUrlApi                                                                                                 
Description         Base URL of API                                                                                            
Value               https://okkqqzxsqd.execute-api.us-east-1.amazonaws.com/Prod                                                

Key                 DeleteTodoApi                                                                                              
Description         API Gateway endpoint URL for ${opt:stage} stage for Delete TODO                                            
Value               https://okkqqzxsqd.execute-api.us-east-1.amazonaws.com/Prod/todos/{id}                                     

Key                 ListTodosApi                                                                                               
Description         API Gateway endpoint URL for ${opt:stage} stage for List TODO                                              
Value               https://okkqqzxsqd.execute-api.us-east-1.amazonaws.com/Prod/todos                                          

Key                 UpdateTodoApi                                                                                              
Description         API Gateway endpoint URL for ${opt:stage} stage for Update TODO                                            
Value               https://okkqqzxsqd.execute-api.us-east-1.amazonaws.com/Prod/todos/{id}                                     

Key                 GetTodoApi                                                                                                 
Description         API Gateway endpoint URL for ${opt:stage} stage for Get TODO                                               
Value               https://okkqqzxsqd.execute-api.us-east-1.amazonaws.com/Prod/todos/{id}                                     

Key                 CreateTodoApi                                                                                              
Description         API Gateway endpoint URL for ${opt:stage} stage for Create TODO                                            
Value               https://okkqqzxsqd.execute-api.us-east-1.amazonaws.com/Prod/todos/                                         
--------------------------------------------------------------------------------------------------------------------------------

Successfully created/updated stack - todo-list-aws in us-east-1

```