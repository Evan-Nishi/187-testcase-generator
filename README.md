# Testcase Auto Generator

This is a quick script to generate altered testcases for CMPE-187 project.

## Setup


Run as sudo FROM THE PROJECT ROOT DIRECTORY [img-testcase-gen](/).  You also need to pip install Pillow:
`pip3 install Pillow`


Next put all images you wish to input in [./in](./in/).  Each image needs to be labelled accordingly: `<unit>-<subchapter>-<writing type>.<file extension>`

Writing type is either t for typed, m for messy, n for neat

For example 
`7-8-t.png`

It will output in the [./out](./out/) directory in the following format: `./out/<unit>/<subchapter>-<writing type>-r<deg rotated>-b<percent brightness>.<file extension>`


NOTE: if you are on windows you will need to change the paths format.