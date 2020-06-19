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
import json
from mkcpr.Error import Error


class Config:

    class EntryNameConstants:
        codeFolder = "code_folder"
        templatePath = "template_path"
        outputFilePath = "output_file_path"
        excluded = "excluded"
        columns = "columns"
        templatePlaceHolder = "template_placeholder"
        sortBefore = "sort_before"
        sortAfter = "sort_after"
        newpageForSectionIsEnabled = "enable_newpage_for_section"

    defaultConfigFilename = "mkcpr-config.json"

    mandatoryEntries = [EntryNameConstants.codeFolder,
                        EntryNameConstants.templatePath]

    def __init__(self):
        path = os.getcwd()
        self.properties = {
            Config.EntryNameConstants.codeFolder: os.path.join(path, "CodeFolder"),
            Config.EntryNameConstants.templatePath: os.path.join(path, "Template.tex"),
            Config.EntryNameConstants.outputFilePath: os.path.join(path, "Output.tex"),
            Config.EntryNameConstants.excluded: set(['.vscode', '__pycache__']),
            Config.EntryNameConstants.columns: 2,
            Config.EntryNameConstants.templatePlaceHolder: "CODE HERE",
            Config.EntryNameConstants.sortBefore: set([]),
            Config.EntryNameConstants.sortAfter: set([]),
            Config.EntryNameConstants.newpageForSectionIsEnabled: False
        }

    def write(self):
        path = os.path.join(os.getcwd(), Config.defaultConfigFilename)
        jsonoutput = {}
        for key, value in self.properties.items():
            if type(value) == set:
                jsonoutput[key] = list(value)
            else:
                jsonoutput[key] = value
        with open(path, 'w+') as f:
            json.dump(jsonoutput, f, indent=4)
        print("Configuration file written in: \"" + str(path) + "\"")

    def read(self):
        path = os.path.join(os.getcwd(), Config.defaultConfigFilename)
        jsonconfig = {}
        try:
            with open(path, "r") as f:
                jsonconfig = json.loads(f.read())
        except json.decoder.JSONDecodeError:
            Error.throwMalformedConfigFile()
        except (FileNotFoundError, IsADirectoryError):
            Error.throwConfigFileNotFound(path)

        for mEntry in self.mandatoryEntries:
            if mEntry not in jsonconfig:
                Error.throwMandatoryEntryNotFoundInConfigFile(mEntry)

        for key, value in self.properties.items():
            if key in jsonconfig:
                jsonconfigValue = jsonconfig[key]
                if type(value) == type(jsonconfigValue):
                    self.properties[key] = jsonconfigValue
                elif type(value) == set and type(jsonconfigValue) == list:
                    self.properties[key] = set(jsonconfigValue)
                else:
                    Error.throwIncorrectTypeForEntryInConfigFile(
                        key, type(value).__name__)

        if not os.path.isdir(self.codeFolderPath()):
            Error.throwCodeFolderNotFound(self.codeFolderPath())

        if not os.path.isfile(self.templatePath()):
            Error.throwTemplateFileNotFound(self.templatePath())
    
    def codeFolderPath(self):
        return self.properties[Config.EntryNameConstants.codeFolder]

    def templatePath(self):
        return self.properties[Config.EntryNameConstants.templatePath]

    def columns(self):
        return self.properties[Config.EntryNameConstants.columns]

    def placeholder(self):
        return self.properties[Config.EntryNameConstants.templatePlaceHolder]

    def outputFilePath(self):
        return self.properties[Config.EntryNameConstants.outputFilePath]

    def excluded(self):
        return self.properties[Config.EntryNameConstants.excluded]

    def sortBefore(self):
        return self.properties[Config.EntryNameConstants.sortBefore]
    
    def sortAfter(self):
        return self.properties[Config.EntryNameConstants.sortAfter]

    def newpageForSectionIsEnabled(self):
        return self.properties[Config.EntryNameConstants.newpageForSectionIsEnabled]

