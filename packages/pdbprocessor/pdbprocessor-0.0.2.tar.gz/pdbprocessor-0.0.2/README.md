# pdbprocessor
### A simple program for extracting basic information from files in PDB format.

### Basics

Usage:

    pdbprocessor [filepath] [mode]

Examples:

    pdbprocessor /home/user/Downloads/1wl3.pdb elemreport
    pdbprocessor 3bb5.pdb aacount SER
    
Use

    pdbprocessor

to enter interactive mode.
    
### File path format
The program supports Unix absolute file paths and all relative paths going down (i.e. without the use of ..). Relative paths with .. and Windows absolute paths are currently not supported.

### Modes
1. elemreport - creates a report on element composition of the protein
2. elemcount - counts the occurrences of a specific element
3. aareport - creates a report on amino acid composition of the protein
4. aacount - counts the occurrences of a specific amino acid

elemcount and aacount require an additional argument specifying the feature to be counted.

### Options
Options are available only in command mode, not in the interactive one. They should be written as arguments, after all necessary positional ones, separated by spaces. Currently available options:
- writefile - creates the output as a file instead of writing it to the console; in my opinion preferable in comparison with bash output redirection

### Installation
1. Download and uncompress the source files
2. Navigate to the "pdbprocessor" folder
3. Open the terminal
4. Run the following command:

Unix terminal:

    pip install .
    
__As of today, other means of installation do not work.__
