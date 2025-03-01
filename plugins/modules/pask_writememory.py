#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Piolink Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type
from ansible_collections.piolink.pask.plugins.module_utils.pask_module import PaskModule,\
    try_except


module_args = dict(
    verify=dict(type="str", required=True)
)

name = 'write-memory'


class PaskWritememory(PaskModule):
    def __init__(self, name, module_args):
        super(PaskWritememory, self).__init__(name, module_args)

    @try_except
    def run(self):
        if self.module.params['verify'] == "yes":
            data = dict()
            self.resp = self.prest.post(self.url, data)


def main():
    writememory = PaskWritememory(name, module_args)
    writememory.set_param()
    writememory.run()
    writememory.set_result()


if __name__ == '__main__':
    main()
