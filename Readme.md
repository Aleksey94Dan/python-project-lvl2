![Python CI](https://github.com/Aleksey94Dan/python-project-lvl2/workflows/Python%20CI/badge.svg?event=push)
[![Test Coverage](https://api.codeclimate.com/v1/badges/33c148e507908cfe14ab/test_coverage)](https://codeclimate.com/github/Aleksey94Dan/python-project-lvl2/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/33c148e507908cfe14ab/maintainability)](https://codeclimate.com/github/Aleksey94Dan/python-project-lvl2/maintainability)
[![Build Status](https://travis-ci.org/Aleksey94Dan/python-project-lvl2.svg?branch=master)](https://travis-ci.org/Aleksey94Dan/python-project-lvl2)


# Description

This program builds the difference between two files. She knows how to work with formats: json and yml / yaml, as well as produce reports in json, plain and stylish.

# Requirements

You must have python version 3.6 installed. or higher.
Also you must have pip installed - The Python Package Installer¶

# Installation

    pip install -U pip
    pip install -i https://test.pypi.org/simple/ aleksey94dan-gendiff --extra-index-url https://pypi.org/simple

[![asciicast](https://asciinema.org/a/xKA6NvXMSEtydAgtxGvFVP4NL.svg)](https://asciinema.org/a/xKA6NvXMSEtydAgtxGvFVP4NL)

# Stylish

To display the difference in stylish format, enter the following command:

    gendiff -f default path/to/file1 path/to/file2
    gendiff --format default path/to/file1 path/to/file2
    gendiff path/to/file1 path/to/file2

[![asciicast](https://asciinema.org/a/sYmLOgg8aJ5N0itDmJiEynksL.svg)](https://asciinema.org/a/sYmLOgg8aJ5N0itDmJiEynksL)

# Plain

To display the difference in plain format, enter the following command:

    gendiff -f plain path/to/file1 path/to/file2
    gendiff --format plain path/to/file1 path/to/file2

[![asciicast](https://asciinema.org/a/TLfPKjvkZZOQpH85CYkpuzBPW.svg)](https://asciinema.org/a/TLfPKjvkZZOQpH85CYkpuzBPW)


# Json
To display the difference in json format, enter the following command:

    gendiff -f json path/to/file1 path/to/file2
    gendiff --format json path/to/file1 path/to/file2

[![asciicast](https://asciinema.org/a/smKwj45nCbkvbHge9AREQedRw.svg)](https://asciinema.org/a/smKwj45nCbkvbHge9AREQedRw)

# This is what happens if you enter an unsupported format or extension.

[![asciicast](https://asciinema.org/a/yCzPhgIS9nS8tXKMQiozJCuR1.svg)](https://asciinema.org/a/yCzPhgIS9nS8tXKMQiozJCuR1)