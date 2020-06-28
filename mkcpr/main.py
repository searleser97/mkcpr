#!/usr/bin/env python3

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


import os
import re
import sys
from mkcpr.Config import Config
from mkcpr.Error import Error
from mkcpr import Util

config = Config()
output = ""


def printSectionType(sectionName, depth, isFile):
    global output
    global config

    style = config.getTitleStyle(depth, isFile)
    sectionType = config.sectionTypeForDepth(depth)

    output += "{\n"

    if len(style) > 0:
        output += style + "\n"

    if isFile:
        sectionName = sectionName[:sectionName.rfind('.')]

    sectionName = sectionName.replace("_", " ")
    output += "\\phantomsection\n"
    output += '\\' + sectionType + "*{" + sectionName + "}\n"
    if depth == config.rootLevel():
        output += "\\markboth{" + sectionName.upper() + "}{}\n"

    if not (depth == 0 and len(style) > 0):
        output += "\\addcontentsline{toc}{" + sectionType + "}{" + sectionName + "}\n"

    output += "}\n"


def printFile(path, depth, sections):
    global output
    global config

    extension = sections[-1][sections[-1].rfind('.') + 1:]
    if extension == 'tex':
        if config.columns() >= 2:
            output += '\\end{multicols*}\n'
        for i in range(len(sections)):
            printSectionType(sections[i], depth -
                             len(sections) + i + 1, i == len(sections) - 1)
        with open(path) as f:
            output += f.read() + '\n'
        if config.columns() >= 2:
            output += '\\begin{multicols*}{' + str(config.columns()) + '}\n'
        return
    if extension == 'h':
        extension = 'cpp'
    with open(path, 'r') as f:
        content = f.read()
    firstLine = content[:content.find('\n') + 1]
    needspace = 0
    if re.fullmatch(' *(?:#|(?://)) ?[1-9][0-9]*\\n', firstLine):
        content = content[len(firstLine):]
        needspace = int(firstLine.strip()[2:].strip())
    for i in range(len(sections)):
        needspace += Util.needspaceForDepth(depth - i)
    output += '\\needspace{' + str(needspace) + '\\baselineskip}\n'
    for i in range(len(sections)):
        printSectionType(sections[i], depth -
                         len(sections) + i + 1, i == len(sections) - 1)
    content = '\\begin{minted}{' + extension + '}\n' + content
    needspaces = set(re.findall(' *(?:#|(?://)) ?[1-9][0-9]*\\n', content))
    for needspace in needspaces:
        news = ''\
            '\\end{minted}\n'\
            '\\vspace{-12pt}\n'\
            '\\needspace{' + needspace.strip()[2:].strip() + '\\baselineskip}\n'\
            '\\begin{minted}{' + extension + '}\n'
        content = content.replace(needspace, news)
    content += '\n\\end{minted}\n'
    output += content + '\n'


def buildOutput(currPath, depth, sections):
    global config

    if len(sections) and sections[-1] in config.excluded():
        return
    sortedDirs = []
    orderFilePath = os.path.join(currPath, Config.orderFileName)
    if os.path.isfile(orderFilePath):
        with open(orderFilePath, 'r') as f:
            for item in f.read().split('\n'):
                if len(item) > 0:
                    sortedDirs.append(item)
    else:
        sortedDirs = sorted(
            os.listdir(currPath),
            key=lambda x: (
                x in config.sortAfter(),
                x not in config.sortBefore(),
                os.path.isdir(os.path.join(currPath, x)),
                x.split('.')[0].lower()
            )
        )
    isFirst = True
    for dirOrFile in sortedDirs:
        f = os.path.join(currPath, dirOrFile)
        if os.path.isdir(f):
            if isFirst:
                isFirst = False
                sections.append(dirOrFile)
                buildOutput(f, depth + 1, sections)
            else:
                buildOutput(f, depth + 1, [dirOrFile])
        elif os.path.isfile(f) and re.fullmatch('.+\\.(cpp|c|py|java|tex)', dirOrFile):
            if isFirst:
                isFirst = False
                sections.append(dirOrFile)
                printFile(f, depth + 1, sections)
            else:
                printFile(f, depth + 1, [dirOrFile])


def main():
    global output
    global config

    if sys.version_info[0] < 3:
        Error.throwUnsupportedPythonVersion()
    elif len(sys.argv) == 2 and sys.argv[1] == "-h":
        Util.displayHelp()
    elif len(sys.argv) == 2 and sys.argv[1] == "-c":
        config.write()
        exit(0)

    config.read()

    if config.columns() >= 2:
        output += "\\begin{multicols*}{" + str(config.columns()) + "}\n"

    sections = []
    buildOutput(config.codeFolderPath(), config.rootLevel() - 1, sections)

    if config.columns() >= 2:
        output += "\\end{multicols*}\n"

    template = Util.getTexCode(config.templatePath())
    output = template.replace(config.placeholder(), output)

    try:
        with open(config.outputFilePath(), 'w+') as f:
            f.write(output)
            print("Tex file written in \"" + config.outputFilePath() + "\"")
    except IOError:
        Error.throwOutputFileIOError(config.outputFilePath())
