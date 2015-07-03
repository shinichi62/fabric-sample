#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *
from fabric.colors import red, yellow
from fabric.main import load_settings

import os, sys
sys.path.append(os.pardir)
from lib import hipchat

env.rcfile = 'local_settings'
env.update(load_settings(env.rcfile))

@task
def production(user='develop'):
    env.environment = 'production'
    env.user = user

@task
def staging(user='develop'):
    env.environment = 'staging'
    env.user = user

@task
def develop(user='vagrant'):
    env.environment = 'develop'
    env.user = user

@task
def deploy():
    # git clone or git pull
    path = '/Users/shinichi62/Fabric/tmp'
    repo_name = 'sandbox'
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.exists(path+'/'+repo_name):
        with lcd(path):
            local('git clone https://github.com/shinichi62/sandbox.git')
    else:
        with lcd(path+'/'+repo_name):
            local('git fetch --all')
            local('git reset --hard origin/master')
            local('git clean -fdx')

    # load balancer
    # apache stop
    # backup
    # deploy
    # apache start
    # load balancer
    # batch

    run('uname -a')
    print("repo_url: %s" % (env.repo_url))
    print("deploy_to: %s" % (env.deploy_to))

    print yellow("ヒント：戻すときは以下のコマンドを実行しましょう")
    print yellow("fab %s branch:master deploy" % (env.environment))
