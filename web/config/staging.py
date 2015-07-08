#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *

@task
def staging(user='vagrant'):
    """ステージング環境"""
    env.environment = 'staging'
    env.user = user
