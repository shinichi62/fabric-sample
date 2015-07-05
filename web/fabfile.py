#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.pardir)
from fabric.api import *
from fabric.colors import red, yellow
from fabric.main import load_settings
from lib.git import *

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
    update(env.REPO_URL, env.BRANCH, env.DEPLOY_FROM)
    # load balancer
    # apache stop
    # backup
    # deploy
    # apache start
    # load balancer
    # batch

    #run('uname -a')

    print yellow("ロールバックするときは以下のコマンドを実行しましょう")
    print yellow("fab -H %s %s branch:master deploy" % (env.hosts, env.environment))
