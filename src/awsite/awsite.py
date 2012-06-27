#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (c) 2012 Ville Korhonen <ville@xd.fi>


import sys
import os

import pkg_resources

__name = 'awsite'
__version = pkg_resources.require(__name)[0].version

def main():
    print "%s v%s" % (__name, __version)    
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
