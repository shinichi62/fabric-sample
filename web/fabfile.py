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
    git_latest(env.REPO_URL, env.BRANCH, env.DEPLOY_FROM)
    # load balancer
    # apache stop
    # backup
    # deploy
    # apache start
    # load balancer
    # batch

    run('uname -a')
    print("repo_url: %s" % (env.REPO_URL))
    print("deploy_to: %s" % (env.DEPLOY_TO))

    print yellow("ヒント：戻すときは以下のコマンドを実行しましょう")
    print yellow("fab %s branch:master deploy" % (env.environment))

@task
def branch(branch):
    env.BRANCH = branch

def git_latest(repo_url, branch, dir):
    u"""Git から最新のソースを取得する

    Keyword arguments:
    repo_url -- リポジトリ URL
    branch -- ブランチ名
    dir -- クローンするディレクトリパス
    """
    if not os.path.exists(dir):
        os.makedirs(dir)
    if not os.path.exists(dir + '/.git'):
        local('git clone %s %s' % (repo_url, dir))
    else:
        with lcd(dir):
            local('git fetch')
            local('git reset --hard origin/%s' % branch)
            local('git clean -fdx')
