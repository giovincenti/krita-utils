# Simple Krita Scripting

I have found that [Krita](https://krita.org/en/) is a fantastic tool to use in my remote teaching, paired with a Wacom [Intuos Pro](https://www.wacom.com/en-us/products/pen-tablets/wacom-intuos-pro) tablet. There are, however, several things that I would like to automate. Here I share my findings and early steps in Krita scripting, so others in the same boat may benefit as well.

## My Setup

* Lenovo ThinkPad L450
* Linux Ubuntu 18.04 LTS
* Gnome Classic Mode
* Krita 4.3.0

## TODO

I am currently working on the following scripts, which are meant to automate my workflow when teaching online:

* Create a new document and save it immediately with the name format 2020-12-25-02-46.kra
  * I don't have to worry about the consistency of the naming, and halting lecture so that I can create a new page for notes
* Save all active documents with the original file name and export them automatically to PNG
  * With this system, I will be able to save all active pages of notes, and convert them to a file format that students can use
* Set the brush size and eraser size at startup
  * Every time I start Krita, the size of the brush and eraser are set to the original default (which does not work for me)

## Resources

* [Krita Scripting](https://kritascripting.wordpress.com/)
* [Introduction to Python Scripting for Krita](https://docs.krita.org/en/user_manual/python_scripting/introduction_to_python_scripting.html)
* [Krita API Reference](https://api.kde.org/appscomplete-api/krita-apidocs/index.html)
  * [Krita Class Reference](https://api.kde.org/appscomplete-api/krita-apidocs/libs/libkis/html/classKrita.html)
  * [Krita.cpp Source File](https://api.kde.org/appscomplete-api/krita-apidocs/libs/libkis/html/Krita_8cpp_source.html)
  * [Document Class Reference](https://api.kde.org/appscomplete-api/krita-apidocs/libs/libkis/html/classDocument.html)
