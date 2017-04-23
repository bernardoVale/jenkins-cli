Jenkins CLI
=====

Yes, I know, there's plenty of Jenkins CLI's already, but guess what?

I don't care!

# UNDER CONSTRUCTION

Inspired by: https://github.com/LD250/jenkins-cli-python

Written using Jenkins Python SDK: https://github.com/openstack/python-jenkins


# Examples

#### List all jobs from Jenkins server
```
jenkins ls
```

#### Collect information about deploy-my-app job

```
jenkins info deploy-my-app
```


#### Trigger job deploy-my-app

```
jenkins run deploy-my-app
```


#### Read console log of job deploy-my-app

```
jenkins cat deploy-my-app
```