# -*- coding: utf-8 -*-
# File   : commands.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 12/03/2018
#
# This file is part of dotfiles.

import six
import os.path as osp
import subprocess
import contextlib

from .filters import ConditionalCallable
from .logging import get_logger

logger = get_logger(__file__)

__all__ = ['Command', 'Commands']


class CommandBase(ConditionalCallable):
    BASEPATH_CWD = '/'

    def __init__(self, cwd='/', filters=None):
        super(CommandBase, self).__init__(filters=filters)
        self.cwd = cwd

    def _get_working_dir(self ,cwd):
        return osp.join(CommandBase.BASEPATH_CWD, cwd)


class Command(CommandBase):
    def __init__(self, cmd, cwd='/', filters=None):
        super(Command, self).__init__(cwd=cwd, filters=filters)
        self.cmd = cmd

    def eval(self):
        cmd = self.cmd
        cwd = self._get_working_dir(self.cwd)
        logger.info('  Execute (cwd: "{}"): {}'.format(cwd, self.cmd))
        if isinstance(cmd, six.string_types):
            cmd = cmd.split()
        subprocess.check_call(cmd, cwd=cwd)


class Commands(CommandBase):
    def __init__(self, cwd, *args, filters=None):
        super(Commands, self).__init__(cwd=cwd, filters=filters)
        self.modules = args

    def eval(self):
        if self.cwd != '/':
            with append_dir(self.cwd):
                for m in self.modules:
                    m()
        else:
            for m in self.modules:
                m()


@contextlib.contextmanager
def change_dir(working_dir):
    backup = CommandBase.BASEPATH_CWD
    CommandBase.BASEPATH_CWD = working_dir
    logger.info('Change current working directory: "{}".'.format(working_dir))
    yield
    CommandBase.BASEPATH_CWD = backup


@contextlib.contextmanager
def append_dir(working_dir):
    backup = CommandBase.BASEPATH_CWD
    CommandBase.BASEPATH_CWD = osp.join(backup, working_dir)
    logger.info('Append current working directory: "{}".'.format(working_dir))
    yield
    CommandBase.BASEPATH_CWD = backup
