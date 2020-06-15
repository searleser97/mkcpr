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


from os import listdir, getcwd
from os.path import isfile, isdir, join
import re
import json
import sys

codeFolder = "Reference"
templatePath = "ReferenceTemplate.tex"
outputFilePath = "Reference.tex"
titlePagePath = ""

excluded = set(['.vscode', '__pycache__'])
numberOfColumns = 2
TextToReplaceInTemplate = "CODE HERE"
fontFamily = ""
tableOfContentsEnabled = True
clearDoublePage = False
newpageForSection = False

sortBefore = set()
sortAfter = set()


output = ""


def printSectionType(sectionName, depth, isFile):
    global output
    global newpageForSection
    
    vspace = 0
    style = '\\bfseries\\sffamily\\centering'
    if depth == 1:
        if newpageForSection:
            output += "\\newpage\n"
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
    sectionName = sectionName.replace("_", " ")
    output += '\\' + sectionType + 'font{' + style + '}\n'
    if vspace:
        output += '\\vspace{' + str(vspace - 1) + 'em}\n'
    output += '\\' + sectionType + '*{' + sectionName + '}\n'
    if depth == 1:
        output += '\\markboth{' + sectionName.upper() + '}{}\n'
    output += '\\addcontentsline{toc}{' + \
        sectionType + '}{' + sectionName + '}\n'
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
        if numberOfColumns >= 2:
            output += '\\end{multicols*}\n'
        for i in range(len(sections)):
            printSectionType(sections[i], depth -
                             len(sections) + i + 1, i == len(sections) - 1)
        with open(path) as f:
            output += f.read() + '\n'
        if numberOfColumns >= 2:
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


def buildOutput(currPath, depth, sections):
    global excluded
    if len(sections) and sections[-1] in excluded:
        return
    sortedDirs = sorted(
        listdir(currPath),
        key=lambda x: (
            x in sortAfter,
            x not in sortBefore,
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
                buildOutput(f, depth + 1, sections)
            else:
                buildOutput(f, depth + 1, [dirOrFile])
        elif isfile(f) and re.fullmatch('.+\\.(cpp|c|py|java|tex)', dirOrFile):
            if isFirst:
                isFirst = False
                sections.append(dirOrFile)
                printFile(f, depth + 1, sections)
            else:
                printFile(f, depth + 1, [dirOrFile])


class ConfigProperties:
    codeFolder = "codeFolder"
    templatePath = "templatePath"
    outputFilePath = "outputFilePath"
    excluded = "excluded"
    columns = "columns"
    templatePlaceHolder = "templatePlaceHolder"
    sortBefore = "sortBefore"
    sortAfter = "sortAfter"
    titlePagePath = "titlePagePath"
    fontFamily = "fontFamily"
    tableOfContents = "tableOfContents"
    clearDoublePage = "clearDoublePage"
    newpageForSection = "newpageForSection"


def outputConfigFile():
    path = getcwd()
    configJson = {ConfigProperties.codeFolder: join(path, "CodeFolderName"),
                  ConfigProperties.templatePath: join(path, "template.tex"),
                  ConfigProperties.outputFilePath: join(path, "output.tex"),
                  ConfigProperties.excluded: [".vscode", "__pycache__"],
                  ConfigProperties.columns: 2,
                  ConfigProperties.templatePlaceHolder: "CODE HERE",
                  ConfigProperties.sortBefore: ["Data Structures"],
                  ConfigProperties.sortAfter: ["Extras"],
                  ConfigProperties.tableOfContents: True,
                  ConfigProperties.titlePagePath: "",
                  ConfigProperties.tableOfContents: True,
                  ConfigProperties.fontFamily: "lmss",
                  ConfigProperties.newpageForSection: False
                  }
    with open('mkcpr-config.json', 'w') as f:
        json.dump(configJson, f, indent=4)


def main():
    global codeFolder
    global templatePath
    global outputFilePath
    global excluded
    global numberOfColumns
    global TextToReplaceInTemplate
    global sortBefore
    global sortAfter
    global output
    global titlePagePath
    global fontFamily
    global tableOfContentsEnabled
    global clearDoublePage
    global newpageForSection

    codeFolder = "Reference"
    templatePath = "ReferenceTemplate.tex"
    outputFilePath = "Reference.tex"

    excluded = set(['.vscode', '__pycache__'])
    numberOfColumns = 2
    TextToReplaceInTemplate = "CODE HERE"

    sortBefore = set()
    sortAfter = set()
    output = ""
    if sys.version_info[0] < 3:
        print("Error: Use python 3.5+ to execute this script")
        exit(0)
    configFilePath = join(getcwd(), "mkcpr-config.json")

    if (len(sys.argv) == 2 and sys.argv[1] == "-h"):
        print("Usage:")
        print("\tmkcpr [CONFIG FILE PATH]")
        exit(0)
    if (len(sys.argv) == 2 and sys.argv[1] == "-c"):
        outputConfigFile()
        print("Configuration file written in " +
              getcwd() + "/mkcpr-config.json")
        exit(0)

    if (len(sys.argv) == 2):
        configFilePath = sys.argv[1]

    try:
        with open(configFilePath, 'r') as f:
            try:
                config = json.loads(f.read())
            except json.decoder.JSONDecodeError:
                print("Error: Malformed configuration file")
                exit(0)
            try:
                codeFolder = config["codeFolder"]
                templatePath = config["templatePath"]
                outputFilePath = config["outputFilePath"]
            except KeyError as e:
                print("Error: Invalid config file. Missing",
                      e, "entry in config file")
                exit(0)
            if ConfigProperties.excluded in config:
                excluded = set(config[ConfigProperties.excluded])
            if ConfigProperties.columns in config:
                numberOfColumns = config[ConfigProperties.columns]
            if ConfigProperties.templatePlaceHolder in config:
                TextToReplaceInTemplate = config[ConfigProperties.templatePlaceHolder]
            if ConfigProperties.sortBefore in config:
                sortBefore = set(config[ConfigProperties.sortBefore])
            if ConfigProperties.sortAfter in config:
                sortAfter = set(config[ConfigProperties.sortAfter])
            if ConfigProperties.titlePagePath in config:
                titlePagePath = config[ConfigProperties.titlePagePath]
            if ConfigProperties.fontFamily in config:
                fontFamily = config[ConfigProperties.fontFamily]
            if ConfigProperties.clearDoublePage in config:
                clearDoublePage = config[ConfigProperties.clearDoublePage]
            if ConfigProperties.newpageForSection in config:
                newpageForSection = config[ConfigProperties.newpageForSection]
                if type(newpageForSection) is not bool:
                    print(
                        "Error in config: \"newpageForSection\" should be a boolean value (True or False)")
                    exit(0)
            if ConfigProperties.tableOfContents in config:
                tableOfContentsEnabled = config[ConfigProperties.tableOfContents]
                if type(tableOfContentsEnabled) is not bool:
                    print(
                        "Error in config: \"tableofcontents\" should be a boolean value (True or False)")
                    exit(0)
    except FileNotFoundError:
        print("Error: Configuration file not found in \"" + configFilePath + "\"")
        print("To create a new configuration file use the -c flag")
        exit(0)
    sections = []
    if not isdir(codeFolder):
        print("Error: Code Folder \"" + codeFolder + "\" not found.")
        exit(0)
    if len(titlePagePath) > 0:
        if not isfile(titlePagePath):
            print("Error: Title Page \"" + titlePagePath + "\" not found.")
            exit(0)
        titlePageExtension = titlePagePath.split('.')[-1]
        if titlePageExtension == "pdf":
            output = "\\includepdf{\"" + titlePagePath + "\"}\n"
        elif titlePageExtension == "tex":
            output = "\\include{\"" + titlePagePath + "\"}\n"
        output += "\\null\n"
        output += "\\thispagestyle{empty}\n"
        output += "\\newpage\n"
    if len(fontFamily) > 0:
        output += "\\fontfamily{" + fontFamily + "}\n"
        output += "\\selectfont\n"
    if numberOfColumns >= 2:
        output += "\\begin{multicols*}{" + str(numberOfColumns) + "}\n"
    if tableOfContentsEnabled:
        output += "\\tableofcontents\n"
        output += "\\newpage\n"
        if clearDoublePage:
            output += "\\cleardoublepage"
    buildOutput(codeFolder, 0, sections)
    if (numberOfColumns) >= 2:
        output += "\\end{multicols*}\n"
    try:
        with open(templatePath, 'r') as f:
            template = f.read()
            output = template.replace(TextToReplaceInTemplate, output)
            try:
                with open(outputFilePath, 'w+') as f2:
                    f2.write(output)
                    print("Tex file written in \"" + outputFilePath + "\"")
            except IOError:
                print("Cannot write \"" + outputFilePath + "\"")
                exit(0)
    except FileNotFoundError:
        print("Error: Tex template not found in \"" + templatePath + "\"")
        exit(0)
