#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.pardir)
from fabric.api import *
from fabric.colors import yellow
from fabric.contrib.project import rsync_project
from config import common, develop, staging, production
from lib import branch, git_update, hipchat

# 共通処理
common()

@task
def deploy():
    """デプロイする"""
    git_update(env.repo_url, env.branch, env.deploy_from)
    rsync_project(remote_dir=env.deploy_to,
                  local_dir=env.deploy_from + '/',
                  exclude=('.git'),
                  delete=True)
    #run('uname -a')

    print yellow('ロールバックするときは以下のコマンドを実行しましょう')
    print yellow('fab -H %s %s branch:master deploy' % (env.hosts, env.environment))
