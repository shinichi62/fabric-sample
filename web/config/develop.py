#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *

def develop(user='vagrant'):
    """開発環境"""
    env.environment = 'develop'
