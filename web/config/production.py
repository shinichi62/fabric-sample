#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *

@task
def production(user='vagrant'):
    """本番環境"""
    env.environment = 'production'
    env.user = user
