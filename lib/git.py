#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from fabric.api import *
from fabric.colors import yellow

@task
def branch(branch):
    u"""ブランチを指定する"""
    env.BRANCH = branch

def git_update(repo_url, branch, dir):
    u"""Git から最新のソースを取得する"""
    if not os.path.exists(dir):
        abort('ディレクトリを作成してください "mkdir %s"' % dir)
    if not os.path.exists(dir + '/.git'):
        local('git clone %s %s' % (repo_url, dir))
    else:
        with lcd(dir):
            local('git fetch')
            local('git reset --hard origin/%s' % branch)
            local('git clean -fdx')
