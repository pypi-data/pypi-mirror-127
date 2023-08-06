# FTSA-TJPB

Welcome to FTSA (Automation Software Tests Framework) from TJPB (Courte of Justice, State of Paraiba / Brazil), or simply FTSA-TJPB.

This *framework* provides libraries to perform automated acceptance tests through _**web**_ and _**mobile**_ interfaces or _**services**_, API rest and _**database**_ tests.

This page provides a brief documentation for installation and operations that are allowed to perform with this client command prompt. 

Project at all is composed by the following modules:

* **CLI:** or *client*, that make available commands to prompt or terminals.
* **CORE:** that provide extensions of the [*Robot API*](http://robotframework.org/) in a series of *customized keywords* to TJPB context of tests automation. 
* **Central:** (*unavailable*) *web* environment to manage project and products, BDD requirements specification, test suites selection and execution (manual or automated, by version and baselines), and tests metrics and consolidated reports.

# FTSA-TJPB-CLI

## Instalação

*Your host machine must be able and configured with python 3.8+ and Docker Engine 20+.*  

### Pre-Requirements

1. You must configure in your host machine Oracle 11+, MySQL 8+ or PostgreSQL 10+ clients in order to run correctly tests. Bellow you can see a linux Fedora list of command that enable configuration you need (execute in presented order):

```
dnf upgrade -y && dnf update -y
dnf install -y python39 pip docker wget
dnf module install -y nodejs:12
dnf install -y libpq-devel
wget https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python3-8.0.25-1.fc34.x86_64.rpm
dnf localinstall -y mysql-connector-python3-8.0.25-1.fc34.x86_64.rpm
wget https://dev.mysql.com/get/Downloads/Connector-ODBC/8.0/mysql-connector-odbc-8.0.25-1.fc34.x86_64.rpm
dnf localinstall -y mysql-connector-odbc-8.0.25-1.fc34.x86_64.rpm
wget https://dev.mysql.com/get/Downloads/Connector-ODBC/8.0/mysql-connector-odbc-setup-8.0.25-1.fc34.x86_64.rpm
dnf localinstall -y mysql-connector-odbc-setup-8.0.25-1.fc34.x86_64.rpm
dnf install -y libaio libnsl
wget https://download.oracle.com/otn_software/linux/instantclient/19600/oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64.rpm
dnf localinstall -y oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64.rpm
```

2. Then, install FTSA-CLI pre-requirements:

```
pip install docker setuptools wheel twine
```

3. Finally, install FTSA-CLI:

```
pip install ftsa-tjpb
```

## List of Commands

Here, follow the list of commands you can use with this client:

1. `ftsa install`: installs all framework dependencies.
2. `ftsa upgrade`: upgrades all framework dependencies.
3. `ftsa uninstall`: uninstalls all framework dependencies.
4. `ftsa report`: runs tests using Docker engine, recording (in case of *web* ui) execution videos and generating execution result report.
    - `-i <tag>` or `--include <tag>`: includes a tag to the execution. Ex: -i uc001 -i uc002
    - `-e <tag>` or `--exclude <tag>`: excludes a tag of the execution. Ex: -e fe
    - `-nd` of `--nodocker`: ignores Docker and performs tests using local browser.
5. `ftsa docker-report`: runs tests using an **external docker engine**
    - `-i <tag>` or `--include <tag>`: includes a tag to the execution. Ex: -i uc001 -i uc002
    - `-e <tag>` or `--exclude <tag>`: excludes a tag of the execution. Ex: -e fe
    - `-n <network_name>` or `--net <network_name`: informs docker network (grid) name. Default: yyyymmdd_grid (year, month, day)
    - `-c <container_name>` or `--container <container_name>`: informs the docker execution container name. Default: execution_robot
    - `-p` or `--pull`: pulls the container image from Docker Hub although creating it locally using Dockerfile.
    - `-dh` or `--dockerhost`: informs IP or docker host name address to docker client host machine. Default: localhost.
    - `-nd` of `--nodocker`: ignores Docker and performs tests using local browser.
  
## Contact and support

*Carlos Diego Quirino Lima*
- **Email:** diego.quirino@tjpb.jus.br

*Felipe Dias*
- **Email:** felipe.dias@tjpb.jus.br

*Rogerio Trevian Nibon*
- **Email:** rogerio.nibon@tjpb.jus.br
