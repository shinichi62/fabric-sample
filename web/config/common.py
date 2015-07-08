#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *

def common(user='vagrant'):
    """共通"""
    env.environment = ''
    env.user = user
    env.repo_url = 'https://github.com/shinichi62/sandbox.git'
    env.branch = 'master'
    env.deploy_from = '/Users/shinichi62/Fabric/tmp/sandbox'
    env.deploy_to = '~/sandbox'
