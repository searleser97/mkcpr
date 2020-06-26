

# mkcpr &middot; [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/searleser97/mkcpr/blob/master/LICENSE) [![PyPI version fury.io](https://badge.fury.io/py/mkcpr.svg)](https://pypi.org/project/mkcpr/)

### Competitive Programming Reference Builder Tool

## About

```mkcpr``` is a command line utility written in python that helps you to build your *Competitive Programming Reference* in PDF.

This command will generate a LaTex formatted file, which will be ready to be compiled into your new *Competitive Programming Reference*, using any online or local LaTex compiler of your preference.
## Usage

- In your working directory run:

```shell
mkcpr [-c|-h]
```
**Notes:**

- The configuration file ```mkcpr-config.json``` should be in the same working directory. (Same path where you run ```mkcpr```).
- ```-c``` flag creates a new configuration file ```mkcpr-config.json``` in the current directory.
- ```-h``` displays help.

## Requirements

- python 3.5+
- Online or local LaTex compiler
- Folder containing your codes for programming competitions
- LaTex template (you can use the one provided in this repository ```Example/Template.tex```)
- Configuration File ```mkcpr-config.json``` (described below)

## Installation

1. Run:
  ```shell
    pip install mkcpr --user
  ```
2. Copy the LaTex template ```Template.tex``` located in the ```Example``` folder of this repository to your working directory.
3. In your working directory run ```mkcpr -c``` to create a new configuration file ```mkcpr-config.json```.
4. Update ```mkcpr-config.json``` and ```Template.tex``` according to your needs. See the [Configuration file options](#configuration-file-options) section for reference.
5. You are now ready to run ```mkcpr``` in your working directory.

## Configuration File Options

```jsonc
{
  "code_folder": "/home/san/Projects/mkcpr/Example/CodeFolder", // Path to your actual code for reference
  "template_path": "/home/san/Projects/mkcpr/Example/Template.tex", // LaTex template path
  "output_file_path": "/home/san/Projects/mkcpr/Example/Output.tex", // path where you want the generated LaTex code to be
  "excluded": ["__pycache__", ".vscode"], // folders not to consider
  "columns": 2, // number of columns in your reference
  "template_placeholder": "CODE HERE", // text to replace in your template
  "sort_before": ["Data Structures"], // files or folders will appear first
  "sort_after": ["Extras"], // file or folders will appear at the end
}
```

## Features

- One single command and your reference will be ready to compile
- Build it with your own style
- support for most file extensions. (.cpp, .py, .java, .tex, .sh, ...)
- Build your reference just from your competitive programming code folder.

<table>
  <tr>
    <th> Folder Structure </th>
    <th> Table Of Contents </th>
  </tr>
  <tr>
    <td>
      <img src="https://codeforces.com/predownloaded/43/53/4353216697913b06f2909ee25b7d7fe586133501.png"/>
    </td>
    <td>
      <img src="https://codeforces.com/predownloaded/35/f5/35f510c1d145e2f3fb9fb147fcbf3febdff3ddf2.png"/>
    </td>
  </tr>
</table>

- Forget about undesired line breaks by specifying the lines of code you want together in the same page with a single comment before your lines of code.

<table>
  <tr>
    <td colspan="2">
      <img src="https://codeforces.com/predownloaded/29/ea/29ea463f8ac652c6bb5fa20fc1c7690546479333.png"/>
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://codeforces.com/predownloaded/a1/4f/a14f0a93f62f3afb7d3519779c18d7e991948ed7.png" width="400" height="250"/>
    </td>
    <td>
      <img src="https://codeforces.com/predownloaded/f6/1e/f61ec142697979d7ebb5b3ec715e2856ebc2faaf.png" width="400" height="250"/>
    </td>
  </tr>
</table>

## Example

You can see an example of how a working directory would look like in a real *Competitive Progamming Reference* [HERE](https://github.com/searleser97/competitive-programming-reference)

## License

```mkcpr``` is licensed under the [GNU General Public License v3.0](https://github.com/searleser97/mkcpr/blob/master/LICENSE)