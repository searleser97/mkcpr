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

class Error:
    @staticmethod
    def throwConfigFileNotFound(configFilePath: str):
        print("Error: Configuration file not found in \"" + configFilePath + "\"")
        print("To create a new configuration file use the -c flag")
        exit(0)

    @staticmethod
    def throwMalformedConfigFile():
        print("Error: Malformed configuration file, check syntax!")
        exit(0)

    @staticmethod
    def throwMandatoryEntryNotFoundInConfigFile(entryName: str):
        print("Error: Missing mandatory entry: \"" +
              entryName + "\" in config file")
        exit(0)

    @staticmethod
    def throwIncorrectTypeForEntryInConfigFile(entryName: str, correctType: str):
        print("Error: Type for entry \"" + entryName + "\" it should be of type:",
              correctType)
        exit(0)

    @staticmethod
    def throwUnsupportedPythonVersion():
        print("Error: Use python 3.5+ to execute this script")
        exit(0)

    @staticmethod
    def throwTemplateFileNotFound(path):
        print("Error: Tex template \"" + path + "\" not found")
        exit(0)

    @staticmethod
    def throwCodeFolderNotFound(path):
        print("Error: Code Folder \"" + path + "\" not found")
        exit(0)

    @staticmethod
    def throwOutputFileIOError(path):
        print("Error: Could not write output file \"" + path + "\"")
        exit(0)

    @staticmethod
    def throwTemplateFileIOError(path):
        print("Error: Could not read template file \"" + path + "\"")
        exit(0)