```
Started by upstream project "PIPELINE-FULL-CD" build number 5
originally caused by:
 Started by user nos
Obtained pipelines/PIPELINE-FULL-PRODUCTION/Jenkinsfile from git https://github.com/NosSLV/todo-list-aws.git
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in /var/lib/jenkins/workspace/PIPELINE-FULL-PRODUCTION
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Declarative: Checkout SCM)
[Pipeline] checkout
Selected Git installation does not exist. Using Default
The recommended git tool is: NONE
using credential github
Cloning the remote Git repository
Cloning repository https://github.com/NosSLV/todo-list-aws.git
 > git init /var/lib/jenkins/workspace/PIPELINE-FULL-PRODUCTION # timeout=10
Fetching upstream changes from https://github.com/NosSLV/todo-list-aws.git
 > git --version # timeout=10
 > git --version # 'git version 2.17.1'
using GIT_SSH to set credentials Acceso SSH a repositorio principal en Github
 > git fetch --tags --progress -- https://github.com/NosSLV/todo-list-aws.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git config remote.origin.url https://github.com/NosSLV/todo-list-aws.git # timeout=10
 > git config --add remote.origin.fetch +refs/heads/*:refs/remotes/origin/* # timeout=10
Avoid second fetch
 > git rev-parse refs/remotes/origin/master^{commit} # timeout=10
Checking out Revision bb4da090824841a1f778d924129fcab0aa6292a7 (refs/remotes/origin/master)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f bb4da090824841a1f778d924129fcab0aa6292a7 # timeout=10
Commit message: "staging pipeline logs added"
First time build. Skipping changelog.
[Pipeline] }
[Pipeline] // stage
[Pipeline] withEnv
[Pipeline] {
[Pipeline] stage
[Pipeline] { (SetUp)
[Pipeline] echo
Setup Virtualenv for testing
[Pipeline] sh
+ bash pipelines/PIPELINE-FULL-PRODUCTION/setup.sh
+ python3.7 -m venv todo-list-aws
+ source todo-list-aws/bin/activate
++ deactivate nondestructive
++ '[' -n '' ']'
++ '[' -n '' ']'
++ '[' -n /bin/bash -o -n '' ']'
++ hash -r
++ '[' -n '' ']'
++ unset VIRTUAL_ENV
++ '[' '!' nondestructive = nondestructive ']'
++ VIRTUAL_ENV=/var/lib/jenkins/workspace/PIPELINE-FULL-PRODUCTION/todo-list-aws
++ export VIRTUAL_ENV
++ _OLD_VIRTUAL_PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
++ PATH=/var/lib/jenkins/workspace/PIPELINE-FULL-PRODUCTION/todo-list-aws/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
++ export PATH
++ '[' -n '' ']'
++ '[' -z '' ']'
++ _OLD_VIRTUAL_PS1=
++ '[' 'x(todo-list-aws) ' '!=' x ']'
++ PS1='(todo-list-aws) '
++ export PS1
++ '[' -n /bin/bash -o -n '' ']'
++ hash -r
+ python -m pip install --upgrade pip
Collecting pip
  Using cached https://files.pythonhosted.org/packages/9b/e6/aa8149e048eda381f2a433599be9b1f5e5e3a189636cd6cf9614aa2ff5be/pip-22.1.1-py3-none-any.whl
Installing collected packages: pip
  Found existing installation: pip 9.0.1
    Uninstalling pip-9.0.1:
      Successfully uninstalled pip-9.0.1
Successfully installed pip-22.1.1
+ python -m pip install awscli
Collecting awscli
  Downloading awscli-1.24.7-py3-none-any.whl (3.9 MB)
     ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 3.9/3.9 MB 50.6 MB/s eta 0:00:00
Collecting PyYAML<5.5,>=3.10
  Downloading PyYAML-5.4.1-cp37-cp37m-manylinux1_x86_64.whl (636 kB)
     ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 636.6/636.6 kB 56.8 MB/s eta 0:00:00
Collecting botocore==1.26.7
  Using cached botocore-1.26.7-py3-none-any.whl (8.8 MB)
Collecting s3transfer<0.6.0,>=0.5.0
  Using cached s3transfer-0.5.2-py3-none-any.whl (79 kB)
Collecting rsa<4.8,>=3.1.2
  Downloading rsa-4.7.2-py3-none-any.whl (34 kB)
Collecting docutils<0.17,>=0.10
  Downloading docutils-0.16-py2.py3-none-any.whl (548 kB)
     ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 548.2/548.2 kB 59.4 MB/s eta 0:00:00
Collecting colorama<0.4.5,>=0.2.5
  Using cached colorama-0.4.4-py2.py3-none-any.whl (16 kB)
Collecting jmespath<2.0.0,>=0.7.1
  Using cached jmespath-1.0.0-py3-none-any.whl (23 kB)
Collecting urllib3<1.27,>=1.25.4
  Using cached urllib3-1.26.9-py2.py3-none-any.whl (138 kB)
Collecting python-dateutil<3.0.0,>=2.1
  Using cached python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
Collecting pyasn1>=0.1.3
  Downloading pyasn1-0.4.8-py2.py3-none-any.whl (77 kB)
     ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 77.1/77.1 kB 15.6 MB/s eta 0:00:00
Collecting six>=1.5
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: pyasn1, urllib3, six, rsa, PyYAML, jmespath, docutils, colorama, python-dateutil, botocore, s3transfer, awscli
Successfully installed PyYAML-5.4.1 awscli-1.24.7 botocore-1.26.7 colorama-0.4.4 docutils-0.16 jmespath-1.0.0 pyasn1-0.4.8 python-dateutil-2.8.2 rsa-4.7.2 s3transfer-0.5.2 six-1.16.0 urllib3-1.26.9
+ python -m pip install aws-sam-cli
Collecting aws-sam-cli
  Downloading aws_sam_cli-1.50.0-py3-none-any.whl (5.1 MB)
     ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 5.1/5.1 MB 48.6 MB/s eta 0:00:00
Collecting boto3==1.*,>=1.19.5
  Using cached boto3-1.23.7-py3-none-any.whl (132 kB)
Collecting requests==2.25.1
  Downloading requests-2.25.1-py2.py3-none-any.whl (61 kB)
     ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 61.2/61.2 kB 11.4 MB/s eta 0:00:00
Collecting MarkupSafe==2.0.1
  Downloading MarkupSafe-2.0.1-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (31 kB)
Collecting dateparser~=1.0
  Downloading dateparser-1.1.1-py2.py3-none-any.whl (288 kB)
     ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 288.9/288.9 kB 34.3 MB/s eta 0:00:00
Collecting aws-sam-translator==1.45.0
  Downloading aws_sam_translator-1.45.0-py3-none-any.whl (228 kB)
     ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 228.9/228.9 kB 40.9 MB/s eta 0:00:00
Collecting chevron~=0.12
  Downloading chevron-0.14.0-py3-none-any.whl (11 kB)
Collecting Flask~=1.1.2
  Downloading Flask-1.1.4-py2.py3-none-any.whl (94 kB)
     ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 94.6/94.6 kB 18.9 MB/s eta 0:00:00
Collecting tomlkit==0.7.2
  Downloading tomlkit-0.7.2-py2.py3-none-any.whl (32 kB)
Collecting typing-extensions==3.10.0.0
  Downloading typing_extensions-3.10.0.0-py3-none-any.whl (26 kB)
Collecting click~=7.1
  Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)
     ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 82.8/82.8 kB 16.0 MB/s eta 0:00:00
Collecting cookiecutter~=1.7.2
  Downloading cookiecutter-1.7.3-py2.py3-none-any.whl (34 kB)
Requirement already satisfied: PyYAML~=5.3 in ./todo-list-aws/lib/python3.7/site-packages (from aws-sam-cli) (5.4.1)
Collecting jmespath~=0.10.0
  Downloading jmespath-0.10.0-py2.py3-none-any.whl (24 kB)
Collecting watchdog==2.1.2
  Downloading watchdog-2.1.2-py3-none-manylinux2014_x86_64.whl (74 kB)
     ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 74.9/74.9 kB 14.9 MB/s eta 0:00:00
Collecting docker~=4.2.0
  Downloading docker-4.2.2-py2.py3-none-any.whl (144 kB)
     ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 144.1/144.1 kB 26.4 MB/s eta 0:00:00
Collecting aws-lambda-builders==1.16.0
  Downloading aws_lambda_builders-1.16.0-py3-none-any.whl (114 kB)
     ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 114.3/114.3 kB 19.0 MB/s eta 0:00:00
Collecting serverlessrepo==0.1.10
  Downloading serverlessrepo-0.1.10-py2.py3-none-any.whl (23 kB)
Collecting regex==2021.9.30
  Downloading regex-2021.9.30-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (747 kB)
     ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 747.4/747.4 kB 57.6 MB/s eta 0:00:00
Collecting tzlocal==3.0
  Downloading tzlocal-3.0-py3-none-any.whl (16 kB)
Requirement already satisfied: six~=1.11 in ./todo-list-aws/lib/python3.7/site-packages (from aws-lambda-builders==1.16.0->aws-sam-cli) (1.16.0)
Collecting wheel
  Downloading wheel-0.37.1-py2.py3-none-any.whl (35 kB)
Requirement already satisfied: setuptools in ./todo-list-aws/lib/python3.7/site-packages (from aws-lambda-builders==1.16.0->aws-sam-cli) (39.0.1)
Collecting jsonschema~=3.2
  Downloading jsonschema-3.2.0-py2.py3-none-any.whl (56 kB)
     ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 56.3/56.3 kB 12.4 MB/s eta 0:00:00
Requirement already satisfied: botocore<1.27.0,>=1.26.7 in ./todo-list-aws/lib/python3.7/site-packages (from boto3==1.*,>=1.19.5->aws-sam-cli) (1.26.7)
Requirement already satisfied: s3transfer<0.6.0,>=0.5.0 in ./todo-list-aws/lib/python3.7/site-packages (from boto3==1.*,>=1.19.5->aws-sam-cli) (0.5.2)
Collecting idna<3,>=2.5
  Downloading idna-2.10-py2.py3-none-any.whl (58 kB)
     ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 58.8/58.8 kB 13.2 MB/s eta 0:00:00
Requirement already satisfied: urllib3<1.27,>=1.21.1 in ./todo-list-aws/lib/python3.7/site-packages (from requests==2.25.1->aws-sam-cli) (1.26.9)
Collecting chardet<5,>=3.0.2
  Downloading chardet-4.0.0-py2.py3-none-any.whl (178 kB)
     ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 178.7/178.7 kB 34.7 MB/s eta 0:00:00
Collecting certifi>=2017.4.17
  Using cached certifi-2022.5.18.1-py3-none-any.whl (155 kB)
Collecting backports.zoneinfo
  Downloading backports.zoneinfo-0.2.1-cp37-cp37m-manylinux1_x86_64.whl (70 kB)
     ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 70.7/70.7 kB 12.7 MB/s eta 0:00:00
Collecting Jinja2<4.0.0,>=2.7
  Using cached Jinja2-3.1.2-py3-none-any.whl (133 kB)
Collecting python-slugify>=4.0.0
  Downloading python_slugify-6.1.2-py2.py3-none-any.whl (9.4 kB)
Collecting poyo>=0.5.0
  Downloading poyo-0.5.0-py2.py3-none-any.whl (10 kB)
Collecting binaryornot>=0.4.4
  Downloading binaryornot-0.4.4-py2.py3-none-any.whl (9.0 kB)
Collecting jinja2-time>=0.2.0
  Downloading jinja2_time-0.2.0-py2.py3-none-any.whl (6.4 kB)
Requirement already satisfied: python-dateutil in ./todo-list-aws/lib/python3.7/site-packages (from dateparser~=1.0->aws-sam-cli) (2.8.2)
Collecting pytz
  Using cached pytz-2022.1-py2.py3-none-any.whl (503 kB)
Collecting websocket-client>=0.32.0
  Downloading websocket_client-1.3.2-py3-none-any.whl (54 kB)
     ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 54.3/54.3 kB 10.1 MB/s eta 0:00:00
Collecting itsdangerous<2.0,>=0.24
  Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting Werkzeug<2.0,>=0.15
  Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
     ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 298.6/298.6 kB 37.9 MB/s eta 0:00:00
Collecting Jinja2<4.0.0,>=2.7
  Downloading Jinja2-2.11.3-py2.py3-none-any.whl (125 kB)
     ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 125.7/125.7 kB 22.9 MB/s eta 0:00:00
Collecting arrow
  Downloading arrow-1.2.2-py3-none-any.whl (64 kB)
     ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 64.0/64.0 kB 11.7 MB/s eta 0:00:00
Collecting pyrsistent>=0.14.0
  Downloading pyrsistent-0.18.1-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (117 kB)
     ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 117.1/117.1 kB 24.2 MB/s eta 0:00:00
Collecting importlib-metadata
  Downloading importlib_metadata-4.11.4-py3-none-any.whl (18 kB)
Collecting attrs>=17.4.0
  Using cached attrs-21.4.0-py2.py3-none-any.whl (60 kB)
Collecting text-unidecode>=1.3
  Downloading text_unidecode-1.3-py2.py3-none-any.whl (78 kB)
     ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 78.2/78.2 kB 15.2 MB/s eta 0:00:00
Collecting zipp>=0.5
  Using cached zipp-3.8.0-py3-none-any.whl (5.4 kB)
Installing collected packages: typing-extensions, text-unidecode, regex, pytz, chevron, zipp, wheel, Werkzeug, websocket-client, watchdog, tomlkit, python-slugify, pyrsistent, poyo, MarkupSafe, jmespath, itsdangerous, idna, click, chardet, certifi, backports.zoneinfo, attrs, tzlocal, requests, Jinja2, importlib-metadata, binaryornot, aws-lambda-builders, arrow, jsonschema, jinja2-time, Flask, docker, dateparser, cookiecutter, boto3, serverlessrepo, aws-sam-translator, aws-sam-cli
  Attempting uninstall: jmespath
    Found existing installation: jmespath 1.0.0
    Uninstalling jmespath-1.0.0:
      Successfully uninstalled jmespath-1.0.0
Successfully installed Flask-1.1.4 Jinja2-2.11.3 MarkupSafe-2.0.1 Werkzeug-1.0.1 arrow-1.2.2 attrs-21.4.0 aws-lambda-builders-1.16.0 aws-sam-cli-1.50.0 aws-sam-translator-1.45.0 backports.zoneinfo-0.2.1 binaryornot-0.4.4 boto3-1.23.7 certifi-2022.5.18.1 chardet-4.0.0 chevron-0.14.0 click-7.1.2 cookiecutter-1.7.3 dateparser-1.1.1 docker-4.2.2 idna-2.10 importlib-metadata-4.11.4 itsdangerous-1.1.0 jinja2-time-0.2.0 jmespath-0.10.0 jsonschema-3.2.0 poyo-0.5.0 pyrsistent-0.18.1 python-slugify-6.1.2 pytz-2022.1 regex-2021.9.30 requests-2.25.1 serverlessrepo-0.1.10 text-unidecode-1.3 tomlkit-0.7.2 typing-extensions-3.10.0.0 tzlocal-3.0 watchdog-2.1.2 websocket-client-1.3.2 wheel-0.37.1 zipp-3.8.0
+ python -m pip install pytest
Collecting pytest
  Using cached pytest-7.1.2-py3-none-any.whl (297 kB)
Collecting packaging
  Using cached packaging-21.3-py3-none-any.whl (40 kB)
Collecting iniconfig
  Using cached iniconfig-1.1.1-py2.py3-none-any.whl (5.0 kB)
Requirement already satisfied: attrs>=19.2.0 in ./todo-list-aws/lib/python3.7/site-packages (from pytest) (21.4.0)
Collecting pluggy<2.0,>=0.12
  Using cached pluggy-1.0.0-py2.py3-none-any.whl (13 kB)
Collecting py>=1.8.2
  Using cached py-1.11.0-py2.py3-none-any.whl (98 kB)
Requirement already satisfied: importlib-metadata>=0.12 in ./todo-list-aws/lib/python3.7/site-packages (from pytest) (4.11.4)
Collecting tomli>=1.0.0
  Using cached tomli-2.0.1-py3-none-any.whl (12 kB)
Requirement already satisfied: typing-extensions>=3.6.4 in ./todo-list-aws/lib/python3.7/site-packages (from importlib-metadata>=0.12->pytest) (3.10.0.0)
Requirement already satisfied: zipp>=0.5 in ./todo-list-aws/lib/python3.7/site-packages (from importlib-metadata>=0.12->pytest) (3.8.0)
Collecting pyparsing!=3.0.5,>=2.0.2
  Using cached pyparsing-3.0.9-py3-none-any.whl (98 kB)
Installing collected packages: iniconfig, tomli, pyparsing, py, pluggy, packaging, pytest
Successfully installed iniconfig-1.1.1 packaging-21.3 pluggy-1.0.0 py-1.11.0 pyparsing-3.0.9 pytest-7.1.2 tomli-2.0.1
+ pwd
/var/lib/jenkins/workspace/PIPELINE-FULL-PRODUCTION
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Build)
[Pipeline] echo
Package sam application:
[Pipeline] sh
+ bash pipelines/common-steps/build.sh
+ sam validate --region us-east-1
2022-05-25 14:11:56 Loading policies from IAM...
2022-05-25 14:11:57 Finished loading policies from IAM.
/var/lib/jenkins/workspace/PIPELINE-FULL-PRODUCTION/template.yaml is a valid SAM Template
+ sam build
[33mYour template contains a resource with logical ID "ServerlessRestApi", which is a reserved logical ID in AWS SAM. It could result in unexpected behaviors and is not recommended.[0m
Building codeuri: /var/lib/jenkins/workspace/PIPELINE-FULL-PRODUCTION/src runtime: python3.7 metadata: {} architecture: x86_64 functions: ['CreateTodoFunction', 'ListTodosFunction', 'GetTodoFunction', 'UpdateTodoFunction', 'DeleteTodoFunction']
Running PythonPipBuilder:ResolveDependencies
Running PythonPipBuilder:CopySource

Build Succeeded

Built Artifacts  : .aws-sam/build
Built Template   : .aws-sam/build/template.yaml

Commands you can use next
=========================
[*] Validate SAM template: sam validate
[*] Invoke Function: sam local invoke
[*] Test Function in the Cloud: sam sync --stack-name {stack-name} --watch
[*] Deploy: sam deploy --guided
        
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Deploy)
[Pipeline] echo
Initiating Deployment
[Pipeline] sh
+ bash pipelines/common-steps/deploy.sh
+ du -hs CHANGELOG.md README.md localEnvironment.json logs pipelines pytest.ini samconfig.toml src template.yaml test todo-list-aws
+ sort -h
4.0K	CHANGELOG.md
4.0K	localEnvironment.json
4.0K	pytest.ini
4.0K	samconfig.toml
8.0K	template.yaml
12K	README.md
28K	test
36K	src
60K	pipelines
100K	logs
172M	todo-list-aws
+ sam deploy template.yaml --config-env production --no-confirm-changeset --force-upload --no-fail-on-empty-changeset --no-progressbar

	Deploying with following values
	===============================
	Stack name                   : todo-list-aws-production
	Region                       : us-east-1
	Confirm changeset            : False
	Deployment s3 bucket         : aws-sam-cli-managed-production-samclisourcebucket-nosslvprod
	Capabilities                 : ["CAPABILITY_IAM"]
	Parameter overrides          : {"Stage": "production"}
	Signing Profiles             : {}

Initiating deployment
=====================

Waiting for changeset to be created..

CloudFormation stack changeset
-------------------------------------------------------------------------------------------------
Operation                LogicalResourceId        ResourceType             Replacement            
-------------------------------------------------------------------------------------------------
+ Add                    CreateTodoFunctionCrea   AWS::Lambda::Permissio   N/A                    
                         tePermissionProd         n                                               
+ Add                    CreateTodoFunction       AWS::Lambda::Function    N/A                    
+ Add                    DeleteTodoFunctionCrea   AWS::Lambda::Permissio   N/A                    
                         tePermissionProd         n                                               
+ Add                    DeleteTodoFunction       AWS::Lambda::Function    N/A                    
+ Add                    GetTodoFunctionCreateP   AWS::Lambda::Permissio   N/A                    
                         ermissionProd            n                                               
+ Add                    GetTodoFunction          AWS::Lambda::Function    N/A                    
+ Add                    ListTodosFunctionCreat   AWS::Lambda::Permissio   N/A                    
                         ePermissionProd          n                                               
+ Add                    ListTodosFunction        AWS::Lambda::Function    N/A                    
+ Add                    ServerlessRestApiDeplo   AWS::ApiGateway::Deplo   N/A                    
                         yment141b842de6          yment                                           
+ Add                    ServerlessRestApiProdS   AWS::ApiGateway::Stage   N/A                    
                         tage                                                                     
+ Add                    ServerlessRestApi        AWS::ApiGateway::RestA   N/A                    
                                                  pi                                              
+ Add                    TodosDynamoDbTable       AWS::DynamoDB::Table     N/A                    
+ Add                    UpdateTodoFunctionCrea   AWS::Lambda::Permissio   N/A                    
                         tePermissionProd         n                                               
+ Add                    UpdateTodoFunction       AWS::Lambda::Function    N/A                    
-------------------------------------------------------------------------------------------------

Changeset created successfully. arn:aws:cloudformation:us-east-1:840621790817:changeSet/samcli-deploy1653487922/4be2168d-8fab-40c6-8a48-00637de46e1f


2022-05-25 14:12:13 - Waiting for stack create/update to complete

CloudFormation events from changeset
-------------------------------------------------------------------------------------------------
ResourceStatus           ResourceType             LogicalResourceId        ResourceStatusReason   
-------------------------------------------------------------------------------------------------
CREATE_IN_PROGRESS       AWS::DynamoDB::Table     TodosDynamoDbTable       -                      
CREATE_IN_PROGRESS       AWS::DynamoDB::Table     TodosDynamoDbTable       Resource creation      
                                                                           Initiated              
CREATE_COMPLETE          AWS::DynamoDB::Table     TodosDynamoDbTable       -                      
CREATE_IN_PROGRESS       AWS::Lambda::Function    DeleteTodoFunction       -                      
CREATE_IN_PROGRESS       AWS::Lambda::Function    CreateTodoFunction       -                      
CREATE_IN_PROGRESS       AWS::Lambda::Function    GetTodoFunction          -                      
CREATE_IN_PROGRESS       AWS::Lambda::Function    UpdateTodoFunction       -                      
CREATE_IN_PROGRESS       AWS::Lambda::Function    ListTodosFunction        -                      
CREATE_IN_PROGRESS       AWS::Lambda::Function    CreateTodoFunction       Resource creation      
                                                                           Initiated              
CREATE_IN_PROGRESS       AWS::Lambda::Function    DeleteTodoFunction       Resource creation      
                                                                           Initiated              
CREATE_IN_PROGRESS       AWS::Lambda::Function    GetTodoFunction          Resource creation      
                                                                           Initiated              
CREATE_IN_PROGRESS       AWS::Lambda::Function    UpdateTodoFunction       Resource creation      
                                                                           Initiated              
CREATE_IN_PROGRESS       AWS::Lambda::Function    ListTodosFunction        Resource creation      
                                                                           Initiated              
CREATE_COMPLETE          AWS::Lambda::Function    DeleteTodoFunction       -                      
CREATE_COMPLETE          AWS::Lambda::Function    CreateTodoFunction       -                      
CREATE_COMPLETE          AWS::Lambda::Function    UpdateTodoFunction       -                      
CREATE_COMPLETE          AWS::Lambda::Function    ListTodosFunction        -                      
CREATE_COMPLETE          AWS::Lambda::Function    GetTodoFunction          -                      
CREATE_IN_PROGRESS       AWS::ApiGateway::RestA   ServerlessRestApi        -                      
                         pi                                                                       
CREATE_IN_PROGRESS       AWS::ApiGateway::RestA   ServerlessRestApi        Resource creation      
                         pi                                                Initiated              
CREATE_COMPLETE          AWS::ApiGateway::RestA   ServerlessRestApi        -                      
                         pi                                                                       
CREATE_IN_PROGRESS       AWS::Lambda::Permissio   CreateTodoFunctionCrea   -                      
                         n                        tePermissionProd                                
CREATE_IN_PROGRESS       AWS::ApiGateway::Deplo   ServerlessRestApiDeplo   -                      
                         yment                    yment141b842de6                                 
CREATE_IN_PROGRESS       AWS::Lambda::Permissio   DeleteTodoFunctionCrea   Resource creation      
                         n                        tePermissionProd         Initiated              
CREATE_IN_PROGRESS       AWS::Lambda::Permissio   UpdateTodoFunctionCrea   -                      
                         n                        tePermissionProd                                
CREATE_IN_PROGRESS       AWS::Lambda::Permissio   GetTodoFunctionCreateP   -                      
                         n                        ermissionProd                                   
CREATE_IN_PROGRESS       AWS::Lambda::Permissio   DeleteTodoFunctionCrea   -                      
                         n                        tePermissionProd                                
CREATE_IN_PROGRESS       AWS::Lambda::Permissio   ListTodosFunctionCreat   Resource creation      
                         n                        ePermissionProd          Initiated              
CREATE_IN_PROGRESS       AWS::Lambda::Permissio   UpdateTodoFunctionCrea   Resource creation      
                         n                        tePermissionProd         Initiated              
CREATE_IN_PROGRESS       AWS::Lambda::Permissio   CreateTodoFunctionCrea   Resource creation      
                         n                        tePermissionProd         Initiated              
CREATE_IN_PROGRESS       AWS::Lambda::Permissio   GetTodoFunctionCreateP   Resource creation      
                         n                        ermissionProd            Initiated              
CREATE_IN_PROGRESS       AWS::Lambda::Permissio   ListTodosFunctionCreat   -                      
                         n                        ePermissionProd                                 
CREATE_IN_PROGRESS       AWS::ApiGateway::Deplo   ServerlessRestApiDeplo   Resource creation      
                         yment                    yment141b842de6          Initiated              
CREATE_COMPLETE          AWS::ApiGateway::Deplo   ServerlessRestApiDeplo   -                      
                         yment                    yment141b842de6                                 
CREATE_IN_PROGRESS       AWS::ApiGateway::Stage   ServerlessRestApiProdS   -                      
                                                  tage                                            
CREATE_IN_PROGRESS       AWS::ApiGateway::Stage   ServerlessRestApiProdS   Resource creation      
                                                  tage                     Initiated              
CREATE_COMPLETE          AWS::ApiGateway::Stage   ServerlessRestApiProdS   -                      
                                                  tage                                            
CREATE_COMPLETE          AWS::Lambda::Permissio   CreateTodoFunctionCrea   -                      
                         n                        tePermissionProd                                
CREATE_COMPLETE          AWS::Lambda::Permissio   GetTodoFunctionCreateP   -                      
                         n                        ermissionProd                                   
CREATE_COMPLETE          AWS::Lambda::Permissio   DeleteTodoFunctionCrea   -                      
                         n                        tePermissionProd                                
CREATE_COMPLETE          AWS::Lambda::Permissio   ListTodosFunctionCreat   -                      
                         n                        ePermissionProd                                 
CREATE_COMPLETE          AWS::Lambda::Permissio   UpdateTodoFunctionCrea   -                      
                         n                        tePermissionProd                                
CREATE_COMPLETE          AWS::CloudFormation::S   todo-list-aws-           -                      
                         tack                     production                                      
-------------------------------------------------------------------------------------------------

CloudFormation outputs from deployed stack
-------------------------------------------------------------------------------------------------
Outputs                                                                                         
-------------------------------------------------------------------------------------------------
Key                 BaseUrlApi                                                                  
Description         Base URL of API                                                             
Value               https://iu0jx0uxja.execute-api.us-east-1.amazonaws.com/Prod                 

Key                 DeleteTodoApi                                                               
Description         API Gateway endpoint URL for ${opt:stage} stage for Delete TODO             
Value               https://iu0jx0uxja.execute-api.us-east-1.amazonaws.com/Prod/todos/{id}      

Key                 ListTodosApi                                                                
Description         API Gateway endpoint URL for ${opt:stage} stage for List TODO               
Value               https://iu0jx0uxja.execute-api.us-east-1.amazonaws.com/Prod/todos           

Key                 UpdateTodoApi                                                               
Description         API Gateway endpoint URL for ${opt:stage} stage for Update TODO             
Value               https://iu0jx0uxja.execute-api.us-east-1.amazonaws.com/Prod/todos/{id}      

Key                 GetTodoApi                                                                  
Description         API Gateway endpoint URL for ${opt:stage} stage for Get TODO                
Value               https://iu0jx0uxja.execute-api.us-east-1.amazonaws.com/Prod/todos/{id}      

Key                 CreateTodoApi                                                               
Description         API Gateway endpoint URL for ${opt:stage} stage for Create TODO             
Value               https://iu0jx0uxja.execute-api.us-east-1.amazonaws.com/Prod/todos/          
-------------------------------------------------------------------------------------------------

Successfully created/updated stack - todo-list-aws-production in us-east-1

[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Integration Test after deploy)
[Pipeline] script
[Pipeline] {
[Pipeline] sh
+ aws cloudformation describe-stacks --stack-name todo-list-aws-production --query Stacks[0].Outputs[?OutputKey==`BaseUrlApi`].OutputValue --region us-east-1 --output text
[Pipeline] echo
https://iu0jx0uxja.execute-api.us-east-1.amazonaws.com/Prod

[Pipeline] echo
Initiating Integration Tests
[Pipeline] sh
+ bash pipelines/common-steps/integration.sh https://iu0jx0uxja.execute-api.us-east-1.amazonaws.com/Prod
+ export BASE_URL=https://iu0jx0uxja.execute-api.us-east-1.amazonaws.com/Prod
+ BASE_URL=https://iu0jx0uxja.execute-api.us-east-1.amazonaws.com/Prod
+ pytest -s test/integration/todoApiTest.py
============================= test session starts ==============================
platform linux -- Python 3.7.5, pytest-7.1.2, pluggy-1.0.0
rootdir: /var/lib/jenkins/workspace/PIPELINE-FULL-PRODUCTION, configfile: pytest.ini
collected 5 items

test/integration/todoApiTest.py ---------------------------------------
Starting - integration test Add TODO
Response Add Todo: {"id": "dad1b6a2-dc34-11ec-9cdf-8250f360b779", "text": "Integration text example", "checked": false, "createdAt": "1653488010.8018427", "updatedAt": "1653488010.8018427"}
ID todo:dad1b6a2-dc34-11ec-9cdf-8250f360b779
End - integration test Add TODO
.---------------------------------------
Starting - integration test Delete TODO
Response Add todo: {"id": "dc58504e-dc34-11ec-9cdf-8250f360b779", "text": "Integration text example - Initial", "checked": false, "createdAt": "1653488013.4826374", "updatedAt": "1653488013.4826374"}
ID todo:dc58504e-dc34-11ec-9cdf-8250f360b779
Response Delete Todo:<Response [200]>
Response Get Todo https://iu0jx0uxja.execute-api.us-east-1.amazonaws.com/Prod/todos/dc58504e-dc34-11ec-9cdf-8250f360b779: <Response [404]>
End - integration test Delete TODO
.---------------------------------------
Starting - integration test Get TODO
Response Add Todo: {'statusCode': 200, 'body': '{"id": "de00bf80-dc34-11ec-9cdf-8250f360b779", "text": "Integration text example - GET", "checked": false, "createdAt": "1653488016.2642338", "updatedAt": "1653488016.2642338"}'}
ID todo:de00bf80-dc34-11ec-9cdf-8250f360b779
Response Get Todo: {'checked': False, 'createdAt': '1653488016.2642338', 'text': 'Integration text example - GET', 'id': 'de00bf80-dc34-11ec-9cdf-8250f360b779', 'updatedAt': '1653488016.2642338'}
End - integration test Get TODO
.---------------------------------------
Starting - integration test List TODO
Response Add Todo: {'statusCode': 200, 'body': '{"id": "deae321e-dc34-11ec-9cdf-8250f360b779", "text": "Integration text example", "checked": false, "createdAt": "1653488017.364428", "updatedAt": "1653488017.364428"}'}
ID todo:deae321e-dc34-11ec-9cdf-8250f360b779
Response List Todo:[{'checked': False, 'createdAt': '1653488017.364428', 'text': 'Integration text example', 'id': 'deae321e-dc34-11ec-9cdf-8250f360b779', 'updatedAt': '1653488017.364428'}]
End - integration test List TODO
.---------------------------------------
Starting - integration test Update TODO
Response Add todo: {"id": "e02c2ec0-dc34-11ec-9cdf-8250f360b779", "text": "Integration text example - Initial", "checked": false, "createdAt": "1653488019.904313", "updatedAt": "1653488019.904313"}
ID todo:e02c2ec0-dc34-11ec-9cdf-8250f360b779
Response Update todo: {'checked': 'true', 'createdAt': '1653488019.904313', 'text': 'Integration text example - Modified', 'id': 'e02c2ec0-dc34-11ec-9cdf-8250f360b779', 'updatedAt': 1653488022118}
Response Get Todo: {'checked': 'true', 'createdAt': '1653488019.904313', 'text': 'Integration text example - Modified', 'id': 'e02c2ec0-dc34-11ec-9cdf-8250f360b779', 'updatedAt': 1653488022118}
End - integration test Update TODO
.

============================== 5 passed in 14.18s ==============================
[Pipeline] }
[Pipeline] // script
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Declarative: Post Actions)
[Pipeline] echo
Clean env: delete dir
[Pipeline] cleanWs
[WS-CLEANUP] Deleting project workspace...
[WS-CLEANUP] Deferred wipeout is used...
[WS-CLEANUP] done
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS
```