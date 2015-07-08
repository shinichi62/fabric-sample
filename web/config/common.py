#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *
from fabric.main import load_settings

def common(user='vagrant'):
    """共通"""
    env.environment = ''
    env.user = user
    env.repo_url = 'https://github.com/shinichi62/sandbox.git'
    env.branch = 'master'
    env.deploy_from = '/Users/shinichi62/sandbox'
    env.deploy_to = '~/sandbox'
    env.update(load_settings('pwd.txt'))
