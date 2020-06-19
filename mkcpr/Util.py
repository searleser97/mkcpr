'''
mkcpr "Competitive programming reference builder tool"
Copyright (C) 2020  Sergio G. Sanchez V.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

def needspaceForDepth(depth):
    if depth == 1:
        needspace = 4
    elif depth == 2:
        needspace = 3
    elif depth == 3:
        needspace = 2
    else:
        needspace = 1
    return needspace

def displayHelp():
    print("Usage:")
    print("\tmkcpr [CONFIG FILE PATH]")
    exit(0)