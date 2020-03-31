
# mkcpr

### Competitive Programming Reference Builder Tool

## About

```mkcpr``` is a command line utility that helps you to build your competitive programming reference PDF.

## Requirements

- python 3.5+
- Online or local LaTex compiler
- A LaTex template (you can use the one provided in this repository ```template.tex```)
- Configuration File (described below)

## Configuration File Options

```jsonc
{
  "codeFolder" : "Code Folder Path", // Path to your actual code for reference
  "templatePath" : "template.tex", // LaTex template path
  "outputFilePath" : "output.tex", // path where you want the LaTex code
  "excluded" : [".vscode", "__pycache__"], // folders not to consider
  "columns" : 2, // number of columns in your reference
  "templatePlaceHolder" : "CODE HERE", // text to replace in your template
  "sortBefore" : ["Data Structures"], // files or folders will appear first
  "sortAfter" : ["Extras"] // file or folders will appear at the end
}
```

## Installation

- Steps:
  1. Download this repository
  2. Copy the script located in the root of this repository ```mkcpr``` to your working directory (or any location in your computer)
  3. Copy the template located in the root of this repository ```template.tex``` to your working directory
  3. Erase the downloaded repository
  4. Preferably add the new location of the script to your environment variables

## Usage

```shell
python3 mkcpr [CONFIG FILE PATH]
```
or just

```shell
mkcpr [CONFIG FILE PATH]
```

The above command will generate a Tex file, which can be compiled with any online or local Tex compiler of your preference.

## Features
- Build your reference just from your competitive programming code folder.

  <img src="https://codeforces.com/predownloaded/43/53/4353216697913b06f2909ee25b7d7fe586133501.png"/>

- Forget about undesired line breaks by specifying the lines of code you want together in the same page with a single comment before your lines of code.


<div>
  <div style="width: 100px; height: 10px; background: red;"></div>
  <img src="https://codeforces.com/predownloaded/29/ea/29ea463f8ac652c6bb5fa20fc1c7690546479333.png"/>
</div>

<div>
  <img src="https://codeforces.com/predownloaded/a1/4f/a14f0a93f62f3afb7d3519779c18d7e991948ed7.png" width="400" height="250"/>
  <img src="https://codeforces.com/predownloaded/f6/1e/f61ec142697979d7ebb5b3ec715e2856ebc2faaf.png" width="400" height="250"/>
</div>

- One single command and your reference will be ready to compile
- Build it with your own style

## Example

You can see an example of how a working directory would look like [here](https://github.com/searleser97/competitive-programming-reference)

## License

```mkcpr``` is licensed under the GNU General Public License v3.0