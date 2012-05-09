# -*- coding: utf-8 -*-
import os
import sys

def get_path(*args):
    """ Joins path args and returns absolute path """
    return os.path.join(os.path.abspath(''), *args)


def add_sys_path(*args):
    """ 
        add_sys_path(root, dir) -> appends root/dir/ do python-path 
    """
    path = os.path.join(*args)
    sys.path.append(path)


class Path(object):
    def __init__(self, mod_path):
        self.mod_path = os.path.realpath(mod_path).split('/')       
        self.file_name = self.mod_path[-1]
        self.project_name = self.mod_path[-2]

        self.PROJECT = self._make_path(self.mod_path[:-1])
        self.ROOT = self._make_path(self.mod_path[:-2])
        
    
    def _make_path(self, path_list):
        return str.join('/', path_list)
    
    def local(self, folder):
        return os.path.join(self.PROJECT, folder)

def setting_from_env(attr):
    if os.environ.has_key('DATABASE_URL'):
        from libs import heroku_settings as current_sets
    else:
        from libs import dev_settings as current_sets

    return getattr(current_sets, attr)