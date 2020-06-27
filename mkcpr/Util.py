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
from mkcpr.Error import Error

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

def getRootLevelForDocumentClass(documentClass):
    if documentClass in ["book", "report"]:
        return 0
    elif documentClass == "memoir":
        return 1
    else:
        return 2

def getTexCode(templatePath):
    texCode = ""
    try:
        with open(templatePath) as f:
            for line in f.readlines():
                if line[0] != '%':
                    texCode += line
    except (IsADirectoryError, FileNotFoundError):
        Error.throwTemplateFileNotFound(templatePath)
    except IOError:
        Error.throwTemplateFileIOError(templatePath)
    return texCode

fontSizeCommands = [
    "\\Huge",
    "\\huge",
    "\\LARGE",
    "\\Large",
    "\\large",
    "\\normalsize",
    "\\small",
    "\\footnotesize",
    "\\scriptsize",
    "\\tiny"
]

def getFontSizeFromCommand(commandString: str):
    for fontsize in fontSizeCommands:
        if fontsize in commandString:
            return fontsize
    return None