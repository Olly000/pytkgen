#!/bin/python

#
# Copyright (c) 2011. All rights reserved.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301  USA

import tkgen

if __name__ == '__main__':
    tkgen = tkgen.Generator()
    root = tkgen.initialize('ui.xml', type = 'xml', title = 'Some test gui...')


    # config vars for checkboxes etc.
    c = tkgen.checkbox('check')

    def ok():
        print tkgen.entry('entry')
        print c.get()
        root.destroy()

    # add button behaviour
    tkgen.button('ok', ok)
    tkgen.button('cancel', root.destroy)

    root.mainloop()
