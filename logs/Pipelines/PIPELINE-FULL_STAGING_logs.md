Started by user nos
Obtained pipelines/PIPELINE-FULL-STAGING/Jenkinsfile from git https://github.com/NosSLV/todo-list-aws.git
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in /var/lib/jenkins/workspace/PIPELINE-FULL_STAGING
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Declarative: Checkout SCM)
[Pipeline] checkout
Selected Git installation does not exist. Using Default
The recommended git tool is: NONE
using credential github
Cloning the remote Git repository
Cloning repository https://github.com/NosSLV/todo-list-aws.git
 > git init /var/lib/jenkins/workspace/PIPELINE-FULL_STAGING # timeout=10
Fetching upstream changes from https://github.com/NosSLV/todo-list-aws.git
 > git --version # timeout=10
 > git --version # 'git version 2.17.1'
using GIT_SSH to set credentials Acceso SSH a repositorio principal en Github
 > git fetch --tags --progress -- https://github.com/NosSLV/todo-list-aws.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git config remote.origin.url https://github.com/NosSLV/todo-list-aws.git # timeout=10
 > git config --add remote.origin.fetch +refs/heads/*:refs/remotes/origin/* # timeout=10
Avoid second fetch
 > git rev-parse refs/remotes/origin/develop^{commit} # timeout=10
Checking out Revision 73717fafc2fabb4f6e810c5aabd9f70b17b7af01 (refs/remotes/origin/develop)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 73717fafc2fabb4f6e810c5aabd9f70b17b7af01 # timeout=10
Commit message: "Indentation Fix"
 > git rev-list --no-walk 73717fafc2fabb4f6e810c5aabd9f70b17b7af01 # timeout=10
[Pipeline] }
[Pipeline] // stage
[Pipeline] withEnv
[Pipeline] {
[Pipeline] stage
[Pipeline] { (SetUp)
[Pipeline] echo
Setup Virtualenv for testing
[Pipeline] sh
+ bash pipelines/PIPELINE-FULL-STAGING/setup.sh
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
++ VIRTUAL_ENV=/var/lib/jenkins/workspace/PIPELINE-FULL_STAGING/todo-list-aws
++ export VIRTUAL_ENV
++ _OLD_VIRTUAL_PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
++ PATH=/var/lib/jenkins/workspace/PIPELINE-FULL_STAGING/todo-list-aws/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
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
+ python -m pip install radon
Collecting radon
  Using cached radon-5.1.0-py2.py3-none-any.whl (52 kB)
Collecting future
  Using cached future-0.18.2.tar.gz (829 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting colorama>=0.4.1
  Using cached colorama-0.4.4-py2.py3-none-any.whl (16 kB)
Collecting mando<0.7,>=0.6
  Using cached mando-0.6.4-py2.py3-none-any.whl (29 kB)
Collecting six
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Using legacy 'setup.py install' for future, since package 'wheel' is not installed.
Installing collected packages: six, future, colorama, mando, radon
  Running setup.py install for future: started
  Running setup.py install for future: finished with status 'done'
Successfully installed colorama-0.4.4 future-0.18.2 mando-0.6.4 radon-5.1.0 six-1.16.0
+ python -m pip install flake8
Collecting flake8
  Using cached flake8-4.0.1-py2.py3-none-any.whl (64 kB)
Collecting mccabe<0.7.0,>=0.6.0
  Using cached mccabe-0.6.1-py2.py3-none-any.whl (8.6 kB)
Collecting pycodestyle<2.9.0,>=2.8.0
  Using cached pycodestyle-2.8.0-py2.py3-none-any.whl (42 kB)
Collecting importlib-metadata<4.3
  Using cached importlib_metadata-4.2.0-py3-none-any.whl (16 kB)
Collecting pyflakes<2.5.0,>=2.4.0
  Using cached pyflakes-2.4.0-py2.py3-none-any.whl (69 kB)
Collecting zipp>=0.5
  Using cached zipp-3.8.0-py3-none-any.whl (5.4 kB)
Collecting typing-extensions>=3.6.4
  Using cached typing_extensions-4.2.0-py3-none-any.whl (24 kB)
Installing collected packages: mccabe, zipp, typing-extensions, pyflakes, pycodestyle, importlib-metadata, flake8
Successfully installed flake8-4.0.1 importlib-metadata-4.2.0 mccabe-0.6.1 pycodestyle-2.8.0 pyflakes-2.4.0 typing-extensions-4.2.0 zipp-3.8.0
+ python -m pip install flake8-polyfill
Collecting flake8-polyfill
  Using cached flake8_polyfill-1.0.2-py2.py3-none-any.whl (7.3 kB)
Requirement already satisfied: flake8 in ./todo-list-aws/lib/python3.7/site-packages (from flake8-polyfill) (4.0.1)
Requirement already satisfied: mccabe<0.7.0,>=0.6.0 in ./todo-list-aws/lib/python3.7/site-packages (from flake8->flake8-polyfill) (0.6.1)
Requirement already satisfied: importlib-metadata<4.3 in ./todo-list-aws/lib/python3.7/site-packages (from flake8->flake8-polyfill) (4.2.0)
Requirement already satisfied: pyflakes<2.5.0,>=2.4.0 in ./todo-list-aws/lib/python3.7/site-packages (from flake8->flake8-polyfill) (2.4.0)
Requirement already satisfied: pycodestyle<2.9.0,>=2.8.0 in ./todo-list-aws/lib/python3.7/site-packages (from flake8->flake8-polyfill) (2.8.0)
Requirement already satisfied: zipp>=0.5 in ./todo-list-aws/lib/python3.7/site-packages (from importlib-metadata<4.3->flake8->flake8-polyfill) (3.8.0)
Requirement already satisfied: typing-extensions>=3.6.4 in ./todo-list-aws/lib/python3.7/site-packages (from importlib-metadata<4.3->flake8->flake8-polyfill) (4.2.0)
Installing collected packages: flake8-polyfill
Successfully installed flake8-polyfill-1.0.2
+ python -m pip install bandit
Collecting bandit
  Using cached bandit-1.7.4-py3-none-any.whl (118 kB)
Collecting PyYAML>=5.3.1
  Using cached PyYAML-6.0-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (596 kB)
Collecting stevedore>=1.20.0
  Using cached stevedore-3.5.0-py3-none-any.whl (49 kB)
Collecting GitPython>=1.0.1
  Using cached GitPython-3.1.27-py3-none-any.whl (181 kB)
Requirement already satisfied: typing-extensions>=3.7.4.3 in ./todo-list-aws/lib/python3.7/site-packages (from GitPython>=1.0.1->bandit) (4.2.0)
Collecting gitdb<5,>=4.0.1
  Using cached gitdb-4.0.9-py3-none-any.whl (63 kB)
Collecting pbr!=2.1.0,>=2.0.0
  Using cached pbr-5.9.0-py2.py3-none-any.whl (112 kB)
Requirement already satisfied: importlib-metadata>=1.7.0 in ./todo-list-aws/lib/python3.7/site-packages (from stevedore>=1.20.0->bandit) (4.2.0)
Collecting smmap<6,>=3.0.1
  Using cached smmap-5.0.0-py3-none-any.whl (24 kB)
Requirement already satisfied: zipp>=0.5 in ./todo-list-aws/lib/python3.7/site-packages (from importlib-metadata>=1.7.0->stevedore>=1.20.0->bandit) (3.8.0)
Installing collected packages: smmap, PyYAML, pbr, stevedore, gitdb, GitPython, bandit
Successfully installed GitPython-3.1.27 PyYAML-6.0 bandit-1.7.4 gitdb-4.0.9 pbr-5.9.0 smmap-5.0.0 stevedore-3.5.0
+ python -m pip install pytest
Collecting pytest
  Using cached pytest-7.1.2-py3-none-any.whl (297 kB)
Collecting attrs>=19.2.0
  Using cached attrs-21.4.0-py2.py3-none-any.whl (60 kB)
Requirement already satisfied: importlib-metadata>=0.12 in ./todo-list-aws/lib/python3.7/site-packages (from pytest) (4.2.0)
Collecting tomli>=1.0.0
  Using cached tomli-2.0.1-py3-none-any.whl (12 kB)
Collecting py>=1.8.2
  Using cached py-1.11.0-py2.py3-none-any.whl (98 kB)
Collecting iniconfig
  Using cached iniconfig-1.1.1-py2.py3-none-any.whl (5.0 kB)
Collecting packaging
  Using cached packaging-21.3-py3-none-any.whl (40 kB)
Collecting pluggy<2.0,>=0.12
  Using cached pluggy-1.0.0-py2.py3-none-any.whl (13 kB)
Requirement already satisfied: typing-extensions>=3.6.4 in ./todo-list-aws/lib/python3.7/site-packages (from importlib-metadata>=0.12->pytest) (4.2.0)
Requirement already satisfied: zipp>=0.5 in ./todo-list-aws/lib/python3.7/site-packages (from importlib-metadata>=0.12->pytest) (3.8.0)
Collecting pyparsing!=3.0.5,>=2.0.2
  Using cached pyparsing-3.0.9-py3-none-any.whl (98 kB)
Installing collected packages: iniconfig, tomli, pyparsing, py, attrs, pluggy, packaging, pytest
Successfully installed attrs-21.4.0 iniconfig-1.1.1 packaging-21.3 pluggy-1.0.0 py-1.11.0 pyparsing-3.0.9 pytest-7.1.2 tomli-2.0.1
+ python -m pip install boto3
Collecting boto3
  Using cached boto3-1.23.6-py3-none-any.whl (132 kB)
Collecting jmespath<2.0.0,>=0.7.1
  Using cached jmespath-1.0.0-py3-none-any.whl (23 kB)
Collecting s3transfer<0.6.0,>=0.5.0
  Using cached s3transfer-0.5.2-py3-none-any.whl (79 kB)
Collecting botocore<1.27.0,>=1.26.6
  Using cached botocore-1.26.6-py3-none-any.whl (8.8 MB)
Collecting python-dateutil<3.0.0,>=2.1
  Using cached python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
Collecting urllib3<1.27,>=1.25.4
  Using cached urllib3-1.26.9-py2.py3-none-any.whl (138 kB)
Requirement already satisfied: six>=1.5 in ./todo-list-aws/lib/python3.7/site-packages (from python-dateutil<3.0.0,>=2.1->botocore<1.27.0,>=1.26.6->boto3) (1.16.0)
Installing collected packages: urllib3, python-dateutil, jmespath, botocore, s3transfer, boto3
Successfully installed boto3-1.23.6 botocore-1.26.6 jmespath-1.0.0 python-dateutil-2.8.2 s3transfer-0.5.2 urllib3-1.26.9
+ python -m pip install moto
Collecting moto
  Using cached moto-3.1.10-py3-none-any.whl (1.8 MB)
Collecting xmltodict
  Using cached xmltodict-0.13.0-py2.py3-none-any.whl (10.0 kB)
Collecting responses>=0.9.0
  Using cached responses-0.20.0-py3-none-any.whl (27 kB)
Requirement already satisfied: importlib-metadata in ./todo-list-aws/lib/python3.7/site-packages (from moto) (4.2.0)
Collecting requests>=2.5
  Using cached requests-2.27.1-py2.py3-none-any.whl (63 kB)
Collecting Jinja2>=2.10.1
  Using cached Jinja2-3.1.2-py3-none-any.whl (133 kB)
Collecting pytz
  Using cached pytz-2022.1-py2.py3-none-any.whl (503 kB)
Collecting cryptography>=3.3.1
  Using cached cryptography-37.0.2-cp36-abi3-manylinux_2_24_x86_64.whl (4.0 MB)
Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in ./todo-list-aws/lib/python3.7/site-packages (from moto) (2.8.2)
Collecting MarkupSafe!=2.0.0a1
  Using cached MarkupSafe-2.1.1-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (25 kB)
Requirement already satisfied: botocore>=1.12.201 in ./todo-list-aws/lib/python3.7/site-packages (from moto) (1.26.6)
Requirement already satisfied: boto3>=1.9.201 in ./todo-list-aws/lib/python3.7/site-packages (from moto) (1.23.6)
Collecting werkzeug
  Using cached Werkzeug-2.1.2-py3-none-any.whl (224 kB)
Requirement already satisfied: s3transfer<0.6.0,>=0.5.0 in ./todo-list-aws/lib/python3.7/site-packages (from boto3>=1.9.201->moto) (0.5.2)
Requirement already satisfied: jmespath<2.0.0,>=0.7.1 in ./todo-list-aws/lib/python3.7/site-packages (from boto3>=1.9.201->moto) (1.0.0)
Requirement already satisfied: urllib3<1.27,>=1.25.4 in ./todo-list-aws/lib/python3.7/site-packages (from botocore>=1.12.201->moto) (1.26.9)
Collecting cffi>=1.12
  Using cached cffi-1.15.0-cp37-cp37m-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (427 kB)
Requirement already satisfied: six>=1.5 in ./todo-list-aws/lib/python3.7/site-packages (from python-dateutil<3.0.0,>=2.1->moto) (1.16.0)
Collecting charset-normalizer~=2.0.0
  Using cached charset_normalizer-2.0.12-py3-none-any.whl (39 kB)
Collecting certifi>=2017.4.17
  Using cached certifi-2022.5.18.1-py3-none-any.whl (155 kB)
Collecting idna<4,>=2.5
  Using cached idna-3.3-py3-none-any.whl (61 kB)
Requirement already satisfied: typing-extensions>=3.6.4 in ./todo-list-aws/lib/python3.7/site-packages (from importlib-metadata->moto) (4.2.0)
Requirement already satisfied: zipp>=0.5 in ./todo-list-aws/lib/python3.7/site-packages (from importlib-metadata->moto) (3.8.0)
Collecting pycparser
  Using cached pycparser-2.21-py2.py3-none-any.whl (118 kB)
Installing collected packages: pytz, xmltodict, werkzeug, pycparser, MarkupSafe, idna, charset-normalizer, certifi, requests, Jinja2, cffi, responses, cryptography, moto
Successfully installed Jinja2-3.1.2 MarkupSafe-2.1.1 certifi-2022.5.18.1 cffi-1.15.0 charset-normalizer-2.0.12 cryptography-37.0.2 idna-3.3 moto-3.1.10 pycparser-2.21 pytz-2022.1 requests-2.27.1 responses-0.20.0 werkzeug-2.1.2 xmltodict-0.13.0
+ python -m pip install mock==4.0.2
Collecting mock==4.0.2
  Using cached mock-4.0.2-py3-none-any.whl (28 kB)
Installing collected packages: mock
Successfully installed mock-4.0.2
+ python -m pip install coverage==4.5.4
Collecting coverage==4.5.4
  Using cached coverage-4.5.4-cp37-cp37m-manylinux1_x86_64.whl (205 kB)
Installing collected packages: coverage
Successfully installed coverage-4.5.4
+ pwd
/var/lib/jenkins/workspace/PIPELINE-FULL_STAGING
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Test)
[Pipeline] echo
Static program analysis:
[Pipeline] sh
+ bash pipelines/PIPELINE-FULL-STAGING/static_test.sh
++ radon cc src -nc
++ wc -l
+ RAD_ERRORS=0
+ [[ 0 -ne 0 ]]
++ radon mi src -nc
++ wc -l
+ RAD_ERRORS=0
+ [[ 0 -ne 0 ]]
+ flake8 src/__init__.py src/create.py src/decimalencoder.py src/delete.py src/get.py src/list.py src/todoList.py src/update.py
+ [[ 0 -ne 0 ]]
+ bandit src/__init__.py src/create.py src/decimalencoder.py src/delete.py src/get.py src/list.py src/todoList.py src/update.py
[main]	INFO	profile include tests: None
[main]	INFO	profile exclude tests: None
[main]	INFO	cli include tests: None
[main]	INFO	cli exclude tests: None
[main]	INFO	running on Python 3.7.5
Run started:2022-05-24 15:46:40.447001

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 194
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (0):
+ [[ 0 -ne 0 ]]
[Pipeline] echo
Unit testing:
[Pipeline] sh
+ bash pipelines/PIPELINE-FULL-STAGING/unit_test.sh
++ pwd
+ export PYTHONPATH=:/var/lib/jenkins/workspace/PIPELINE-FULL_STAGING
+ PYTHONPATH=:/var/lib/jenkins/workspace/PIPELINE-FULL_STAGING
+ echo 'PYTHONPATH: :/var/lib/jenkins/workspace/PIPELINE-FULL_STAGING'
PYTHONPATH: :/var/lib/jenkins/workspace/PIPELINE-FULL_STAGING
+ export DYNAMODB_TABLE=todoUnitTestsTable
+ DYNAMODB_TABLE=todoUnitTestsTable
+ python test/unit/TestToDo.py
/var/lib/jenkins/workspace/PIPELINE-FULL_STAGING/todo-list-aws/lib/python3.7/site-packages/moto/__init__.py:27: UserWarning: Module mock_dynamodb2 has been deprecated, and will be removed in a later release. Please use mock_dynamodb instead. See https://github.com/spulec/moto/issues/4526 for more information.
  f"Module {used} has been deprecated, and will be removed in a later release. Please use {recommended} instead. "
.........
----------------------------------------------------------------------
Ran 9 tests in 0.821s

OK
---------------------
Start: setUp
Creating Table with name:todoUnitTestsTable
End: setUp
---------------------
Start: test_delete_todo
Table name:todoUnitTestsTable
Response PutItem{'statusCode': 200, 'body': '{"id": "b45a3b3c-db78-11ec-b10b-12aa63d31ab1", "text": "Aprender DevOps y Cloud en la UNIR", "checked": false, "createdAt": "1653407200.9825916", "updatedAt": "1653407200.9825916"}'}
Id item:b45a3b3c-db78-11ec-b10b-12aa63d31ab1
Item deleted succesfully
End: test_delete_todo
---------------------
Start: tearDown
Table deleted succesfully
End: tearDown
---------------------
Start: setUp
Creating Table with name:todoUnitTestsTable
End: setUp
---------------------
Start: test_delete_todo_error
End: test_delete_todo_error
---------------------
Start: tearDown
Table deleted succesfully
End: tearDown
---------------------
Start: setUp
Creating Table with name:todoUnitTestsTable
End: setUp
---------------------
Start: test_get_todo
Table name:todoUnitTestsTable
Response put_item:{'statusCode': 200, 'body': '{"id": "b45a3b3d-db78-11ec-b10b-12aa63d31ab1", "text": "Aprender DevOps y Cloud en la UNIR", "checked": false, "createdAt": "1653407201.1646805", "updatedAt": "1653407201.1646805"}'}
Id item:b45a3b3d-db78-11ec-b10b-12aa63d31ab1
Result getItem:{'Item': {'id': 'b45a3b3d-db78-11ec-b10b-12aa63d31ab1', 'text': 'Aprender DevOps y Cloud en la UNIR', 'checked': False, 'createdAt': '1653407201.1646805', 'updatedAt': '1653407201.1646805'}, 'ResponseMetadata': {'RequestId': 'UO5M2JPIM1QO8FKOUXP9ZQWQOLK2JI4SPEA4FUVZ3EB9MRFLHCCB', 'HTTPStatusCode': 200, 'HTTPHeaders': {'server': 'amazon.com', 'x-amzn-requestid': 'UO5M2JPIM1QO8FKOUXP9ZQWQOLK2JI4SPEA4FUVZ3EB9MRFLHCCB', 'x-amz-crc32': '2097224312'}, 'RetryAttempts': 0}}
Response Get:{'id': 'b45a3b3d-db78-11ec-b10b-12aa63d31ab1', 'text': 'Aprender DevOps y Cloud en la UNIR', 'checked': False, 'createdAt': '1653407201.1646805', 'updatedAt': '1653407201.1646805'}
End: test_get_todo
---------------------
Start: tearDown
Table deleted succesfully
End: tearDown
---------------------
Start: setUp
Creating Table with name:todoUnitTestsTable
End: setUp
---------------------
Start: test_list_todo
Table name:todoUnitTestsTable
Response GetItems[{'id': 'b45a3b3e-db78-11ec-b10b-12aa63d31ab1', 'text': 'Aprender DevOps y Cloud en la UNIR', 'checked': False, 'createdAt': '1653407201.2433925', 'updatedAt': '1653407201.2433925'}]
End: test_list_todo
---------------------
Start: tearDown
Table deleted succesfully
End: tearDown
---------------------
Start: setUp
Creating Table with name:todoUnitTestsTable
End: setUp
---------------------
Start: test_put_todo
Table name:todoUnitTestsTable
Response put_item:{'statusCode': 200, 'body': '{"id": "b45a3b3f-db78-11ec-b10b-12aa63d31ab1", "text": "Aprender DevOps y Cloud en la UNIR", "checked": false, "createdAt": "1653407201.3987727", "updatedAt": "1653407201.3987727"}'}
End: test_put_todo
---------------------
Start: tearDown
Table deleted succesfully
End: tearDown
---------------------
Start: setUp
Creating Table with name:todoUnitTestsTable
End: setUp
---------------------
Start: test_put_todo_error
Table name:todoUnitTestsTable
Table name:todoUnitTestsTable
End: test_put_todo_error
---------------------
Start: tearDown
Table deleted succesfully
End: tearDown
---------------------
Start: setUp
Creating Table with name:todoUnitTestsTable
End: setUp
---------------------
Start: test_table_exists
Table name:todoUnitTestsTable
End: test_table_exists
---------------------
Start: tearDown
Table deleted succesfully
End: tearDown
---------------------
Start: setUp
Creating Table with name:todoUnitTestsTable
End: setUp
---------------------
Start: test_update_todo
Table name:todoUnitTestsTable
Response PutItem{'statusCode': 200, 'body': '{"id": "b45a3b42-db78-11ec-b10b-12aa63d31ab1", "text": "Aprender DevOps y Cloud en la UNIR", "checked": false, "createdAt": "1653407201.615916", "updatedAt": "1653407201.615916"}'}
Id item:b45a3b42-db78-11ec-b10b-12aa63d31ab1
Result Update Item:{'id': 'b45a3b42-db78-11ec-b10b-12aa63d31ab1', 'text': 'Aprender más cosas que DevOps y Cloud en la UNIR', 'checked': 'false', 'createdAt': '1653407201.615916', 'updatedAt': Decimal('1653407201618')}
End: test_update_todo
---------------------
Start: tearDown
Table deleted succesfully
End: tearDown
---------------------
Start: setUp
Creating Table with name:todoUnitTestsTable
End: setUp
---------------------
Start: atest_update_todo_error
Table name:todoUnitTestsTable
Response PutItem{'statusCode': 200, 'body': '{"id": "b45a3b43-db78-11ec-b10b-12aa63d31ab1", "text": "Aprender DevOps y Cloud en la UNIR", "checked": false, "createdAt": "1653407201.6987014", "updatedAt": "1653407201.6987014"}'}
End: atest_update_todo_error
---------------------
Start: tearDown
Table deleted succesfully
End: tearDown
+ pip show coverage
Name: coverage
Version: 4.5.4
Summary: Code coverage measurement for Python
Home-page: https://github.com/nedbat/coveragepy
Author: Ned Batchelder and 100 others
Author-email: ned@nedbatchelder.com
License: Apache 2.0
Location: /var/lib/jenkins/workspace/PIPELINE-FULL_STAGING/todo-list-aws/lib/python3.7/site-packages
Requires: 
Required-by: 
+ coverage run --include=src/todoList.py test/unit/TestToDo.py
/var/lib/jenkins/workspace/PIPELINE-FULL_STAGING/todo-list-aws/lib/python3.7/site-packages/moto/__init__.py:27: UserWarning: Module mock_dynamodb2 has been deprecated, and will be removed in a later release. Please use mock_dynamodb instead. See https://github.com/spulec/moto/issues/4526 for more information.
  f"Module {used} has been deprecated, and will be removed in a later release. Please use {recommended} instead. "
.........
----------------------------------------------------------------------
Ran 9 tests in 1.080s

OK
---------------------
Start: setUp
Creating Table with name:todoUnitTestsTable
End: setUp
---------------------
Start: test_delete_todo
Table name:todoUnitTestsTable
Response PutItem{'statusCode': 200, 'body': '{"id": "b58d83f6-db78-11ec-b10b-12aa63d31ab1", "text": "Aprender DevOps y Cloud en la UNIR", "checked": false, "createdAt": "1653407203.0083637", "updatedAt": "1653407203.0083637"}'}
Id item:b58d83f6-db78-11ec-b10b-12aa63d31ab1
Item deleted succesfully
End: test_delete_todo
---------------------
Start: tearDown
Table deleted succesfully
End: tearDown
---------------------
Start: setUp
Creating Table with name:todoUnitTestsTable
End: setUp
---------------------
Start: test_delete_todo_error
End: test_delete_todo_error
---------------------
Start: tearDown
Table deleted succesfully
End: tearDown
---------------------
Start: setUp
Creating Table with name:todoUnitTestsTable
End: setUp
---------------------
Start: test_get_todo
Table name:todoUnitTestsTable
Response put_item:{'statusCode': 200, 'body': '{"id": "b58d83f7-db78-11ec-b10b-12aa63d31ab1", "text": "Aprender DevOps y Cloud en la UNIR", "checked": false, "createdAt": "1653407203.2203653", "updatedAt": "1653407203.2203653"}'}
Id item:b58d83f7-db78-11ec-b10b-12aa63d31ab1
Result getItem:{'Item': {'id': 'b58d83f7-db78-11ec-b10b-12aa63d31ab1', 'text': 'Aprender DevOps y Cloud en la UNIR', 'checked': False, 'createdAt': '1653407203.2203653', 'updatedAt': '1653407203.2203653'}, 'ResponseMetadata': {'RequestId': 'LZ3FT67RUE5NQECK2F4ISA5A6537IUAEFE1YQLLQI2U1W6BKMWVH', 'HTTPStatusCode': 200, 'HTTPHeaders': {'server': 'amazon.com', 'x-amzn-requestid': 'LZ3FT67RUE5NQECK2F4ISA5A6537IUAEFE1YQLLQI2U1W6BKMWVH', 'x-amz-crc32': '2878458206'}, 'RetryAttempts': 0}}
Response Get:{'id': 'b58d83f7-db78-11ec-b10b-12aa63d31ab1', 'text': 'Aprender DevOps y Cloud en la UNIR', 'checked': False, 'createdAt': '1653407203.2203653', 'updatedAt': '1653407203.2203653'}
End: test_get_todo
---------------------
Start: tearDown
Table deleted succesfully
End: tearDown
---------------------
Start: setUp
Creating Table with name:todoUnitTestsTable
End: setUp
---------------------
Start: test_list_todo
Table name:todoUnitTestsTable
Response GetItems[{'id': 'b58d83f8-db78-11ec-b10b-12aa63d31ab1', 'text': 'Aprender DevOps y Cloud en la UNIR', 'checked': False, 'createdAt': '1653407203.3892567', 'updatedAt': '1653407203.3892567'}]
End: test_list_todo
---------------------
Start: tearDown
Table deleted succesfully
End: tearDown
---------------------
Start: setUp
Creating Table with name:todoUnitTestsTable
End: setUp
---------------------
Start: test_put_todo
Table name:todoUnitTestsTable
Response put_item:{'statusCode': 200, 'body': '{"id": "b58d83f9-db78-11ec-b10b-12aa63d31ab1", "text": "Aprender DevOps y Cloud en la UNIR", "checked": false, "createdAt": "1653407203.48856", "updatedAt": "1653407203.48856"}'}
End: test_put_todo
---------------------
Start: tearDown
Table deleted succesfully
End: tearDown
---------------------
Start: setUp
Creating Table with name:todoUnitTestsTable
End: setUp
---------------------
Start: test_put_todo_error
Table name:todoUnitTestsTable
Table name:todoUnitTestsTable
End: test_put_todo_error
---------------------
Start: tearDown
Table deleted succesfully
End: tearDown
---------------------
Start: setUp
Creating Table with name:todoUnitTestsTable
End: setUp
---------------------
Start: test_table_exists
Table name:todoUnitTestsTable
End: test_table_exists
---------------------
Start: tearDown
Table deleted succesfully
End: tearDown
---------------------
Start: setUp
Creating Table with name:todoUnitTestsTable
End: setUp
---------------------
Start: test_update_todo
Table name:todoUnitTestsTable
Response PutItem{'statusCode': 200, 'body': '{"id": "b58d83fc-db78-11ec-b10b-12aa63d31ab1", "text": "Aprender DevOps y Cloud en la UNIR", "checked": false, "createdAt": "1653407203.7782078", "updatedAt": "1653407203.7782078"}'}
Id item:b58d83fc-db78-11ec-b10b-12aa63d31ab1
Result Update Item:{'id': 'b58d83fc-db78-11ec-b10b-12aa63d31ab1', 'text': 'Aprender más cosas que DevOps y Cloud en la UNIR', 'checked': 'false', 'createdAt': '1653407203.7782078', 'updatedAt': Decimal('1653407203782')}
End: test_update_todo
---------------------
Start: tearDown
Table deleted succesfully
End: tearDown
---------------------
Start: setUp
Creating Table with name:todoUnitTestsTable
End: setUp
---------------------
Start: atest_update_todo_error
Table name:todoUnitTestsTable
Response PutItem{'statusCode': 200, 'body': '{"id": "b58d83fd-db78-11ec-b10b-12aa63d31ab1", "text": "Aprender DevOps y Cloud en la UNIR", "checked": false, "createdAt": "1653407203.8853884", "updatedAt": "1653407203.8853884"}'}
End: atest_update_todo_error
---------------------
Start: tearDown
Table deleted succesfully
End: tearDown
+ coverage report
Name              Stmts   Miss  Cover
-------------------------------------
src/todoList.py      64     15    77%
+ coverage xml
Post stage
[Pipeline] script
[Pipeline] {
[Pipeline] publishCoverage
Publishing Coverage report....
A total of 1 reports were found
Report coverage diff: 0.0%. Add to CoverageResult.
Group coverage diff: 0.0%. Add to CoverageResult.
Package coverage diff: 0.0%. Add to CoverageResult.
File coverage diff: 0.0%. Add to CoverageResult.
Class coverage diff: 0.0%. Add to CoverageResult.
Line coverage diff: 0.0%. Add to CoverageResult.
[Coverage] Computing coverage delta report
[Coverage] Reference build recorder is not configured
[Coverage] -> No reference build defined, falling back to previous build
[Coverage] -> Found reference result 'io.jenkins.plugins.coverage.CoverageAction@1e54fc57'
[Checks API] No suitable checks publisher found.
[Pipeline] }
[Pipeline] // script
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Build)
[Pipeline] echo
Package sam application:
[Pipeline] sh
+ bash pipelines/common-steps/build.sh
+ sam validate --region us-east-1
2022-05-24 15:46:46 Loading policies from IAM...
2022-05-24 15:46:46 Finished loading policies from IAM.
/var/lib/jenkins/workspace/PIPELINE-FULL_STAGING/template.yaml is a valid SAM Template
+ sam build
Building codeuri: /var/lib/jenkins/workspace/PIPELINE-FULL_STAGING/src runtime: python3.7 metadata: {} architecture: x86_64 functions: ['CreateTodoFunction', 'ListTodosFunction', 'GetTodoFunction', 'UpdateTodoFunction', 'DeleteTodoFunction']
Running PythonPipBuilder:ResolveDependencies
Running PythonPipBuilder:CopySource

Build Succeeded

Built Artifacts  : .aws-sam/build
Built Template   : .aws-sam/build/template.yaml

Commands you can use next
=========================
[*] Invoke Function: sam local invoke
[*] Deploy: sam deploy --guided
    
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Deploy)
[Pipeline] echo
Initiating Deployment
[Pipeline] sh
+ bash pipelines/common-steps/deploy.sh
+ sort -h
+ du -hs CHANGELOG.md README.md coverage.xml localEnvironment.json logs pipelines pytest.ini samconfig.toml src template.yaml test todo-list-aws
4.0K	CHANGELOG.md
4.0K	coverage.xml
4.0K	localEnvironment.json
4.0K	pytest.ini
4.0K	samconfig.toml
8.0K	template.yaml
12K	README.md
28K	test
48K	logs
48K	src
60K	pipelines
160M	todo-list-aws
+ sam deploy template.yaml --config-env staging --no-confirm-changeset --force-upload --no-fail-on-empty-changeset --no-progressbar

	Deploying with following values
	===============================
	Stack name                   : todo-list-aws-staging
	Region                       : us-east-1
	Confirm changeset            : False
	Deployment s3 bucket         : aws-sam-cli-managed-staging-samclisourcebucket-nosslvstaging
	Capabilities                 : ["CAPABILITY_IAM"]
	Parameter overrides          : {"Stage": "staging"}
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

Changeset created successfully. arn:aws:cloudformation:us-east-1:840621790817:changeSet/samcli-deploy1653407211/cb419801-5f55-4327-bf3a-b40ff94867e4


2022-05-24 15:47:02 - Waiting for stack create/update to complete

CloudFormation events from changeset
-------------------------------------------------------------------------------------------------
ResourceStatus           ResourceType             LogicalResourceId        ResourceStatusReason   
-------------------------------------------------------------------------------------------------
CREATE_IN_PROGRESS       AWS::DynamoDB::Table     TodosDynamoDbTable       -                      
CREATE_IN_PROGRESS       AWS::DynamoDB::Table     TodosDynamoDbTable       Resource creation      
                                                                           Initiated              
CREATE_COMPLETE          AWS::DynamoDB::Table     TodosDynamoDbTable       -                      
CREATE_IN_PROGRESS       AWS::Lambda::Function    GetTodoFunction          -                      
CREATE_IN_PROGRESS       AWS::Lambda::Function    DeleteTodoFunction       -                      
CREATE_IN_PROGRESS       AWS::Lambda::Function    CreateTodoFunction       -                      
CREATE_IN_PROGRESS       AWS::Lambda::Function    ListTodosFunction        -                      
CREATE_IN_PROGRESS       AWS::Lambda::Function    UpdateTodoFunction       -                      
CREATE_IN_PROGRESS       AWS::Lambda::Function    CreateTodoFunction       Resource creation      
                                                                           Initiated              
CREATE_IN_PROGRESS       AWS::Lambda::Function    ListTodosFunction        Resource creation      
                                                                           Initiated              
CREATE_IN_PROGRESS       AWS::Lambda::Function    GetTodoFunction          Resource creation      
                                                                           Initiated              
CREATE_IN_PROGRESS       AWS::Lambda::Function    UpdateTodoFunction       Resource creation      
                                                                           Initiated              
CREATE_IN_PROGRESS       AWS::Lambda::Function    DeleteTodoFunction       Resource creation      
                                                                           Initiated              
CREATE_COMPLETE          AWS::Lambda::Function    UpdateTodoFunction       -                      
CREATE_COMPLETE          AWS::Lambda::Function    ListTodosFunction        -                      
CREATE_COMPLETE          AWS::Lambda::Function    CreateTodoFunction       -                      
CREATE_COMPLETE          AWS::Lambda::Function    GetTodoFunction          -                      
CREATE_COMPLETE          AWS::Lambda::Function    DeleteTodoFunction       -                      
CREATE_IN_PROGRESS       AWS::ApiGateway::RestA   ServerlessRestApi        -                      
                         pi                                                                       
CREATE_IN_PROGRESS       AWS::ApiGateway::RestA   ServerlessRestApi        Resource creation      
                         pi                                                Initiated              
CREATE_COMPLETE          AWS::ApiGateway::RestA   ServerlessRestApi        -                      
                         pi                                                                       
CREATE_IN_PROGRESS       AWS::ApiGateway::Deplo   ServerlessRestApiDeplo   -                      
                         yment                    yment141b842de6                                 
CREATE_IN_PROGRESS       AWS::Lambda::Permissio   CreateTodoFunctionCrea   -                      
                         n                        tePermissionProd                                
CREATE_IN_PROGRESS       AWS::Lambda::Permissio   UpdateTodoFunctionCrea   -                      
                         n                        tePermissionProd                                
CREATE_IN_PROGRESS       AWS::Lambda::Permissio   ListTodosFunctionCreat   -                      
                         n                        ePermissionProd                                 
CREATE_IN_PROGRESS       AWS::Lambda::Permissio   DeleteTodoFunctionCrea   -                      
                         n                        tePermissionProd                                
CREATE_IN_PROGRESS       AWS::Lambda::Permissio   ListTodosFunctionCreat   Resource creation      
                         n                        ePermissionProd          Initiated              
CREATE_IN_PROGRESS       AWS::Lambda::Permissio   UpdateTodoFunctionCrea   Resource creation      
                         n                        tePermissionProd         Initiated              
CREATE_IN_PROGRESS       AWS::Lambda::Permissio   CreateTodoFunctionCrea   Resource creation      
                         n                        tePermissionProd         Initiated              
CREATE_IN_PROGRESS       AWS::Lambda::Permissio   GetTodoFunctionCreateP   -                      
                         n                        ermissionProd                                   
CREATE_IN_PROGRESS       AWS::Lambda::Permissio   DeleteTodoFunctionCrea   Resource creation      
                         n                        tePermissionProd         Initiated              
CREATE_IN_PROGRESS       AWS::Lambda::Permissio   GetTodoFunctionCreateP   Resource creation      
                         n                        ermissionProd            Initiated              
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
CREATE_COMPLETE          AWS::Lambda::Permissio   ListTodosFunctionCreat   -                      
                         n                        ePermissionProd                                 
CREATE_COMPLETE          AWS::Lambda::Permissio   UpdateTodoFunctionCrea   -                      
                         n                        tePermissionProd                                
CREATE_COMPLETE          AWS::Lambda::Permissio   CreateTodoFunctionCrea   -                      
                         n                        tePermissionProd                                
CREATE_COMPLETE          AWS::Lambda::Permissio   DeleteTodoFunctionCrea   -                      
                         n                        tePermissionProd                                
CREATE_COMPLETE          AWS::Lambda::Permissio   GetTodoFunctionCreateP   -                      
                         n                        ermissionProd                                   
CREATE_COMPLETE          AWS::CloudFormation::S   todo-list-aws-staging    -                      
                         tack                                                                     
-------------------------------------------------------------------------------------------------

CloudFormation outputs from deployed stack
-------------------------------------------------------------------------------------------------
Outputs                                                                                         
-------------------------------------------------------------------------------------------------
Key                 BaseUrlApi                                                                  
Description         Base URL of API                                                             
Value               https://lgobeau914.execute-api.us-east-1.amazonaws.com/Prod                 

Key                 DeleteTodoApi                                                               
Description         API Gateway endpoint URL for ${opt:stage} stage for Delete TODO             
Value               https://lgobeau914.execute-api.us-east-1.amazonaws.com/Prod/todos/{id}      

Key                 ListTodosApi                                                                
Description         API Gateway endpoint URL for ${opt:stage} stage for List TODO               
Value               https://lgobeau914.execute-api.us-east-1.amazonaws.com/Prod/todos           

Key                 UpdateTodoApi                                                               
Description         API Gateway endpoint URL for ${opt:stage} stage for Update TODO             
Value               https://lgobeau914.execute-api.us-east-1.amazonaws.com/Prod/todos/{id}      

Key                 GetTodoApi                                                                  
Description         API Gateway endpoint URL for ${opt:stage} stage for Get TODO                
Value               https://lgobeau914.execute-api.us-east-1.amazonaws.com/Prod/todos/{id}      

Key                 CreateTodoApi                                                               
Description         API Gateway endpoint URL for ${opt:stage} stage for Create TODO             
Value               https://lgobeau914.execute-api.us-east-1.amazonaws.com/Prod/todos/          
-------------------------------------------------------------------------------------------------

Successfully created/updated stack - todo-list-aws-staging in us-east-1

[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Integration Test after deploy)
[Pipeline] script
[Pipeline] {
[Pipeline] sh
+ aws cloudformation describe-stacks --stack-name todo-list-aws-staging --query Stacks[0].Outputs[?OutputKey==`BaseUrlApi`].OutputValue --region us-east-1 --output text
[Pipeline] echo
https://lgobeau914.execute-api.us-east-1.amazonaws.com/Prod

[Pipeline] echo
Initiating Integration Tests
[Pipeline] sh
+ bash pipelines/common-steps/integration.sh https://lgobeau914.execute-api.us-east-1.amazonaws.com/Prod
+ export BASE_URL=https://lgobeau914.execute-api.us-east-1.amazonaws.com/Prod
+ BASE_URL=https://lgobeau914.execute-api.us-east-1.amazonaws.com/Prod
+ pytest -s test/integration/todoApiTest.py
============================= test session starts ==============================
platform linux -- Python 3.7.5, pytest-7.1.2, pluggy-1.0.0
rootdir: /var/lib/jenkins/workspace/PIPELINE-FULL_STAGING, configfile: pytest.ini
collected 5 items

test/integration/todoApiTest.py ---------------------------------------
Starting - integration test Add TODO
Response Add Todo: {"id": "eed73a08-db78-11ec-90c3-a2f36052d54d", "text": "Integration text example", "checked": false, "createdAt": "1653407298.9884634", "updatedAt": "1653407298.9884634"}
ID todo:eed73a08-db78-11ec-90c3-a2f36052d54d
End - integration test Add TODO
.---------------------------------------
Starting - integration test Delete TODO
Response Add todo: {"id": "f0951018-db78-11ec-90c3-a2f36052d54d", "text": "Integration text example - Initial", "checked": false, "createdAt": "1653407302.0500407", "updatedAt": "1653407302.0500407"}
ID todo:f0951018-db78-11ec-90c3-a2f36052d54d
Response Delete Todo:<Response [200]>
Response Get Todo https://lgobeau914.execute-api.us-east-1.amazonaws.com/Prod/todos/f0951018-db78-11ec-90c3-a2f36052d54d: <Response [404]>
End - integration test Delete TODO
.---------------------------------------
Starting - integration test Get TODO
Response Add Todo: {'statusCode': 200, 'body': '{"id": "f25b6532-db78-11ec-90c3-a2f36052d54d", "text": "Integration text example - GET", "checked": false, "createdAt": "1653407304.989914", "updatedAt": "1653407304.989914"}'}
ID todo:f25b6532-db78-11ec-90c3-a2f36052d54d
Response Get Todo: {'checked': False, 'createdAt': '1653407304.989914', 'text': 'Integration text example - GET', 'id': 'f25b6532-db78-11ec-90c3-a2f36052d54d', 'updatedAt': '1653407304.989914'}
End - integration test Get TODO
.---------------------------------------
Starting - integration test List TODO
Response Add Todo: {'statusCode': 200, 'body': '{"id": "f2e54568-db78-11ec-90c3-a2f36052d54d", "text": "Integration text example", "checked": false, "createdAt": "1653407305.9311433", "updatedAt": "1653407305.9311433"}'}
ID todo:f2e54568-db78-11ec-90c3-a2f36052d54d
Response List Todo:[{'checked': False, 'createdAt': '1653407305.9311433', 'text': 'Integration text example', 'id': 'f2e54568-db78-11ec-90c3-a2f36052d54d', 'updatedAt': '1653407305.9311433'}]
End - integration test List TODO
.---------------------------------------
Starting - integration test Update TODO
Response Add todo: {"id": "f46b9356-db78-11ec-90c3-a2f36052d54d", "text": "Integration text example - Initial", "checked": false, "createdAt": "1653407308.489031", "updatedAt": "1653407308.489031"}
ID todo:f46b9356-db78-11ec-90c3-a2f36052d54d
Response Update todo: {'checked': 'true', 'createdAt': '1653407308.489031', 'text': 'Integration text example - Modified', 'id': 'f46b9356-db78-11ec-90c3-a2f36052d54d', 'updatedAt': 1653407310609}
Response Get Todo: {'checked': 'true', 'createdAt': '1653407308.489031', 'text': 'Integration text example - Modified', 'id': 'f46b9356-db78-11ec-90c3-a2f36052d54d', 'updatedAt': 1653407310609}
End - integration test Update TODO
.

============================== 5 passed in 14.59s ==============================
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