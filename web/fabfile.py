#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *
from fabric.colors import yellow
from fabric.contrib.project import rsync_project

import os
import sys
sys.path.append(os.pardir)
import config
import lib

# 初期化
config.common.common()

@task
def develop(user='vagrant'):
    """開発環境"""
    config.develop.develop(user)

@task
def staging(user='vagrant'):
    """ステージング環境"""
    config.staging.staging(user)

@task
def production(user='vagrant'):
    """本番環境"""
    config.production.production(user)

@task
def branch(branch):
    """ブランチを指定する"""
    lib.git.branch(branch)

@task
def deploy():
    """デプロイする"""
    lib.git.git_update(env.repo_url, env.branch, env.deploy_from)
    rsync_project(remote_dir=env.deploy_to,
                  local_dir=env.deploy_from + '/',
                  exclude=('.git'),
                  delete=True)
    #run('uname -a')

    print yellow('ロールバックするときは以下のコマンドを実行しましょう')
    print yellow('fab -H %s %s branch:master deploy' % (env.hosts, env.environment))
