#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *
from fabric.colors import red, yellow

import os, sys
sys.path.append(os.pardir)
from lib import hipchat

@task
def production(user='develop'):
    env.environment = 'production'
    env.user = user
    env.roledefs.update({
        'web': [''],
        })

@task
def staging(user='develop'):
    env.environment = 'staging'
    env.user = user
    env.roledefs.update({
        'web': [''],
        })

@task
def develop(user='vagrant'):
    env.environment = 'develop'
    env.user = user
    env.roledefs.update({
        'web': ['192.168.33.10'],
        })

@roles('web')
@task
def deploy():
    run('uname -a')
    print yellow("ヒント：戻すときは以下のコマンドを実行しましょう")
    print yellow("fab %s branch:master deploy" % (env.environment))
