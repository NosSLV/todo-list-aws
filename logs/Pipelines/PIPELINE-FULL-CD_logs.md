```
Started by user nos
Obtained pipelines/PIPELINE-FULL-CD/Jenkinsfile from git git@github.com:NosSLV/todo-list-aws.git
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in /var/lib/jenkins/workspace/PIPELINE-FULL-CD
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Declarative: Checkout SCM)
[Pipeline] checkout
Selected Git installation does not exist. Using Default
The recommended git tool is: NONE
using credential github
Cloning the remote Git repository
Cloning repository git@github.com:NosSLV/todo-list-aws.git
 > git init /var/lib/jenkins/workspace/PIPELINE-FULL-CD # timeout=10
Fetching upstream changes from git@github.com:NosSLV/todo-list-aws.git
 > git --version # timeout=10
 > git --version # 'git version 2.17.1'
using GIT_SSH to set credentials Acceso SSH a repositorio principal en Github
 > git fetch --tags --progress -- git@github.com:NosSLV/todo-list-aws.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git config remote.origin.url git@github.com:NosSLV/todo-list-aws.git # timeout=10
 > git config --add remote.origin.fetch +refs/heads/*:refs/remotes/origin/* # timeout=10
Avoid second fetch
 > git rev-parse refs/remotes/origin/master^{commit} # timeout=10
Checking out Revision 8dc4b3daf498b1786afe7e240e46670c6810afcf (refs/remotes/origin/master)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 8dc4b3daf498b1786afe7e240e46670c6810afcf # timeout=10
Commit message: "Local logs & README changes added"
First time build. Skipping changelog.
[Pipeline] }
[Pipeline] // stage
[Pipeline] withEnv
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Staging)
[Pipeline] echo
Starting staging job
[Pipeline] build (Building PIPELINE-FULL-STAGING)
Scheduling project: PIPELINE-FULL-STAGING
Starting building: PIPELINE-FULL-STAGING #4
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Merge)
[Pipeline] sh (Merging code to master)
+ set -x
+ git branch -a
* (HEAD detached at 8dc4b3d)
  remotes/origin/develop
  remotes/origin/feature
  remotes/origin/master
+ git checkout -b develop origin/develop
Previous HEAD position was 8dc4b3d Local logs & README changes added
Switched to a new branch 'develop'
Branch 'develop' set up to track remote branch 'develop' from 'origin'.
+ git checkout -b master origin/master
Switched to a new branch 'master'
Branch 'master' set up to track remote branch 'master' from 'origin'.
+ git merge develop
Updating 8dc4b3d..bb4da09
Fast-forward
 logs/Manual_SAM_deployment/SAM_logs.md             | 233 ++++++
 .../dynamo_api_sam_deployment.md                   |  47 ++
 logs/Pipelines/PIPELINE-FULL-CD_logs.md            |   0
 logs/Pipelines/PIPELINE-FULL-PRODUCTION_logs.md    |   0
 logs/Pipelines/PIPELINE-FULL_STAGING_logs.md       | 866 +++++++++++++++++++++
 logs/local/dynamo_api_local.md                     |   4 +-
 samconfig.toml                                     |   7 +-
 src/todoList.py                                    |   7 +
 8 files changed, 1160 insertions(+), 4 deletions(-)
 create mode 100644 logs/Manual_SAM_deployment/SAM_logs.md
 create mode 100644 logs/Manual_SAM_deployment/dynamo_api_sam_deployment.md
 create mode 100644 logs/Pipelines/PIPELINE-FULL-CD_logs.md
 create mode 100644 logs/Pipelines/PIPELINE-FULL-PRODUCTION_logs.md
 create mode 100644 logs/Pipelines/PIPELINE-FULL_STAGING_logs.md
[Pipeline] sshagent
[ssh-agent] Using credentials NosSLV (Acceso SSH a repositorio principal en Github)
[ssh-agent] Looking for ssh-agent implementation...
[ssh-agent]   Exec ssh-agent (binary ssh-agent on a remote machine)
$ ssh-agent
SSH_AUTH_SOCK=/tmp/ssh-QjpYjauZnuOW/agent.8818
SSH_AGENT_PID=8821
Running ssh-add (command line suppressed)
Identity added: /var/lib/jenkins/workspace/PIPELINE-FULL-CD@tmp/private_key_2455028304223166617.key (/var/lib/jenkins/workspace/PIPELINE-FULL-CD@tmp/private_key_2455028304223166617.key)
[ssh-agent] Started.
[Pipeline] {
[Pipeline] sh
+ git push origin master
Warning: Permanently added the ECDSA host key for IP address '140.82.113.3' to the list of known hosts.
To github.com:NosSLV/todo-list-aws.git
   8dc4b3d..bb4da09  master -> master
[Pipeline] }
$ ssh-agent -k
unset SSH_AUTH_SOCK;
unset SSH_AGENT_PID;
echo Agent pid 8821 killed;
[ssh-agent] Stopped.
[Pipeline] // sshagent
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Production)
[Pipeline] echo
Starting production job
[Pipeline] build (Building PIPELINE-FULL-PRODUCTION)
Scheduling project: PIPELINE-FULL-PRODUCTION
Starting building: PIPELINE-FULL-PRODUCTION #1
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