#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *
from fabric.colors import red, yellow

@task
def production(user='develop'):
    env.environment = 'production'
    env.user = user
    env.roledefs.update({
        'wbb': [''],
        })

@task
def staging(user='develop'):
    env.environment = 'staging'
    env.user = user
    env.roledefs.update({
        'wbb': [''],
        })

@task
def develop(user='vagrant'):
    env.environment = 'develop'
    env.user = user
    env.roledefs.update({
        'wbb': ['192.168.33.10'],
        })

@roles('wbb')
@task
def deploy(release=''):
    run('uname -a')
    print yellow("ヒント：戻すときは以下のコマンドを実行しましょう")
    print yellow("fab %s deploy:feature/ABC" % (env.environment))