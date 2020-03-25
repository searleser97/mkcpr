#!/usr/bin/env python
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


from os import listdir
from os.path import isfile, isdir, join
import re
import json
import sys

codeFolder = "Reference"
templatePath = "ReferenceTemplate.tex"
outputFilePath = "Reference.tex"

excluded = set(['.vscode', '__pycache__'])
numberOfColumns = 2
TextToReplaceInTemplate = "CODE HERE"


output = ""


def printSectionType(sectionName, depth, isFile):
    global output
    vspace = 0
    style = '\\bfseries\\sffamily\\centering'
    if depth == 1:
        sectionType = 'section'
        style += '\\Huge'
        vspace = 2
    elif depth == 2:
        sectionType = 'subsection'
        style += '\\LARGE'
        vspace = 1
    elif depth == 3:
        sectionType = 'subsubsection'
        style += '\\Large'
        vspace = 1
    else:
        sectionType = 'paragraph'
        style += '\\large'
        vspace = 1
    if isFile:
        sectionName = sectionName[:sectionName.rfind('.')]
        style = '\\large\\bfseries\\sffamily\\underline'
        vspace = 0
    output += '\\' + sectionType + 'font{' + style + '}\n'
    if vspace:
        output += '\\vspace{' + str(vspace - 1) + 'em}\n'
    output += '\\' + sectionType + '*{' + sectionName + '}\n'
    if depth == 1:
        output += '\\markboth{' + sectionName.upper() + '}{}\n'
    output += '\\addcontentsline{toc}{' + sectionType + '}{' + sectionName + '}\n'
    if vspace:
        output += '\\vspace{' + str(vspace + 1) + 'em}\n'


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


def printFile(path, depth, sections):
    global output
    global numberOfColumns

    extension = sections[-1][sections[-1].rfind('.') + 1:]
    if extension == 'tex':
        output += '\\end{multicols*}\n'
        for i in range(len(sections)):
            printSectionType(sections[i], depth -
                             len(sections) + i + 1, i == len(sections) - 1)
        with open(path) as f:
            output += f.read() + '\n'
        output += '\\begin{multicols*}{' + str(numberOfColumns) + '}\n'
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
        needspace += needspaceForDepth(depth - i)
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


def main(currPath, depth, sections):
    global excluded
    if len(sections) and sections[-1] in excluded:
        return
    sortedDirs = sorted(
        listdir(currPath),
        key=lambda x: (
            x == 'Extras',
            x == 'Problems Solved',
            x != 'Coding Resources',
            x != 'Data Structures',
            isdir(join(currPath, x)),
            x.split('.')[0].lower()
        )
    )
    isFirst = True
    for dirOrFile in sortedDirs:
        f = join(currPath, dirOrFile)
        if isdir(f):
            if isFirst:
                isFirst = False
                sections.append(dirOrFile)
                main(f, depth + 1, sections)
            else:
                main(f, depth + 1, [dirOrFile])
        elif isfile(f) and re.fullmatch('.+\\.(cpp|c|py|java|tex)', dirOrFile):
            if isFirst:
                isFirst = False
                sections.append(dirOrFile)
                printFile(f, depth + 1, sections)
            else:
                printFile(f, depth + 1, [dirOrFile])


if __name__ == '__main__':
    configFilePath = join(sys.path[0], "mkcpr-config.json")

    if (len(sys.argv) == 2 and sys.argv[1] == "-h"):
        print("Usage:")
        print("\tpython mkcpr.py [CONFIG FILE PATH]")
        exit(0)

    if (len(sys.argv) == 2):
        configFilePath = sys.argv[1]
    else:
        print("Warning: Missing configuration file path in arguments (using default)")

    try:
        with open(configFilePath, 'r') as f:
            config = json.loads(f.read())
            try:
                codeFolder = config["codeFolder"]
                templatePath = config["templatePath"]
                outputFilePath = config["outputFilePath"]
            except KeyError as e:
                print("Error: Invalid config file. Missing", e, "entry in config file")
                exit(0)
            try:
                excluded = config["excluded"]
                numberOfColumns = config["columns"]
                TextToReplaceInTemplate = config["templatePlaceHolder"]
            except KeyError:
                pass
    except FileNotFoundError:
        print("Error: Configuration file not found in:", configFilePath)
        exit(0)
    sections = []
    main(codeFolder, 0, sections)
    with open(templatePath, 'r') as f:
        template = f.read()
        output = template.replace(TextToReplaceInTemplate, output)
        with open(outputFilePath, 'w') as f2:
            f2.write(output)
