
# mkcpr
### Competitive Programming Reference Builder Tool

## About
```mkcpr``` is a command line utility that helps you build your competitive programming reference PDF.

## Features

- Forget about undesired line breaks by specifying the lines of code you want together in the same page with a single comment before your lines of code.
- One single command and your reference will be ready to compile
- Easy setup with a single json file
- Highly configurable

## Installation

- Requirements:
  - python 3.5+

- Steps:
  1. Just download this repository

## Usage

```shell
python mkcpr [CONFIG FILE PATH]
```
The above command will generate a Tex file, which can be compiled with any Tex compiler of your preference.

## Configuration File Options

```json
{
  "codeFolder" : "Code Folder Path", // Path to your actual code for reference
  "templatePath" : "template.tex", // LaTex template path
  "outputFilePath" : "output.tex", // path where you want the LaTex code
  "excluded" : [".vscode", "__pycache__"], // folders not to consider
  "columns" : 2, // number of columns in your reference
  "templatePlaceHolder" : "CODE HERE", // text to replace in your template
  "sortBefore" : ["Data Structures"], // files or folders will appear first
  "sortAfter" : ["Extras"] /* file or folders will appear at the end */
}
```

## License

```mkcpr``` is licensed under the GNU General Public License v3.0