Jenkins CLI
=====

Yes, I know, there's plenty of Jenkins CLI's already, but guess what?

I don't care!


# Installation

Using pip:
```bash
pip install jenkinscli
```

From source:
```bash
git clone git@github.com:bernardoVale/jenkins-cli.git
cd jenkins-cli
python setup.py install
```

# Running inside a container

That's the way I use this tool by the way. 

Build the container:

```bash
make build
```

Add the following shell function to your `.bashrc` or `.zshrc`:

```bash
jenkins(){
    docker run -it --rm \
    -v ~/.jenkins_config.yml:/root/.jenkins_config.yml \
    jenkinscli $@
}
```

Open a new shell tab and there you go:
```bash
$ jenkins ping

Hello Bernardo Vale, we've connected to Jenkins Server version:2.7.4
```

# UNDER CONSTRUCTION

Inspired by: https://github.com/LD250/jenkins-cli-python

Written using Jenkins Python SDK: https://github.com/openstack/python-jenkins


# Examples


### Listing

List all jobs from Jenkins server
```
jenkins ls
```
List all jobs that matches string `deploy` ignore-case by default

```bash
jenkins ls deploy
```

Listing all jobs that belongs to a given view
```
jenkins ls --view deployers
```


### Running Jobs

Trigger job deploy-my-app

```
jenkins run deploy-my-app
```

Triggering a parametrized job that has two arguments:

```bash
jenkins run deploy-my-app branch=master force=true
```

### Getting Information

Collect information about deploy-my-app job

```
jenkins info deploy-my-app
```

### Reading Output

Read console log of job deploy-my-app

```
jenkins cat deploy-my-app
```

### Running Scripts

Executes a groovy script inside Jenkins
```bash
jenkins script script.groovy
```
