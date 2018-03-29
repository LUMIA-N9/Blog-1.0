# -*- coding: utf-8 -*-
'''
Configuration
'''

import config_default


class Dict(dict):
    '''
    Simple dict but supoort access as x.y style.
    '''

    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


def merge(defaults, override):
    r = {}
    for k, v in defaults.items():
        print('k is : %s' % k)
        print('v is : %s' % v)
        if k in override:
            print('k is in override')
            print('override is %s' % override)
            if isinstance(v, dict):
                print('v2 is : %s' % v)
                print('override[k] is %s' % override[k])
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    print('r is :%s' % r)
    return r


def toDict(d):
    D = Dict()
    for k, v in d.items():
        D[k] = toDict(v) if isinstance(v, dict) else v
    print('D is : %s' % D)
    print()
    return D


configs = config_default.configs

try:
    import config_override
    configs = merge(configs, config_override.configs)
    print('configs is :%s' % configs)
    print()
except ImportError:
    pass

configs = toDict(
    configs)  # 虽然经toDict函数处理过的configs内容没有改变，都是字典，但其可以通过 . 来访问属性，而不单单是xxx[key]
