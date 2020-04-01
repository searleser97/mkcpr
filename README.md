

# mkcpr

### Competitive Programming Reference Builder Tool

## About

```mkcpr``` is a command line utility written in python that helps you to build your *Competitive Programming Reference* in PDF.

This command will generate a $\text{LaTex}$ formatted file, which will be ready to be compiled into your new *Competitive Programming Reference*, using any online or local $\text{LaTex}$ compiler of your preference.
## Usage

- Linux & MacOS
```shell
python3 mkcpr [CONFIG FILE PATH]
```
- Windows

```shell
python mkcpr [CONFIG FILE PATH]
```
Note: ```[CONFIG FILE PATH]``` is an optional parameter with ```"mkcpr-config.json"``` as default value

## Requirements

- python 3.5+
- Online or local LaTex compiler
- Folder containing your codes for programming competitions
- LaTex template (you can use the one provided in this repository ```template.tex```)
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

1. Download this repository
2. Copy the script located in the root of this repository ```mkcpr``` to your working directory (or any location in your computer)
3. Copy the template and configuration files located in the root of this repository ```template.tex``` and ```mkcpr-config.json``` to your working directory
3. Erase the downloaded repository (optional)
4. Preferably add the new location of the script to your environment variables (optional)

## Features
- Build your reference just from your competitive programming code folder.
<div>
  <img src="https://codeforces.com/predownloaded/43/53/4353216697913b06f2909ee25b7d7fe586133501.png"/>
  <img src="https://codeforces.com/predownloaded/35/f5/35f510c1d145e2f3fb9fb147fcbf3febdff3ddf2.png"/>
</div>

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

You can see an example of how a working directory would look like [HERE](https://github.com/searleser97/competitive-programming-reference)

## License

```mkcpr``` is licensed under the GNU General Public License v3.0