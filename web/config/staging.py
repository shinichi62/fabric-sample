#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *

def staging(user='vagrant'):
    """ステージング環境"""
    env.environment = 'staging'
