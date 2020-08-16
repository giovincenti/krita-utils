# Author: Giovanni Vincenti

from krita import *

# Basic attributes used through the script

new_doc_width = 1600
new_doc_height = 1200
author = "Giovanni Vincenti"
save_path = "/home/ubprof/Desktop/"
file_name = "test.kra" # I will change this later to include date+time

# I create a new document of size 1600x1200
newDoc = Krita.instance().createDocument(new_doc_width, new_doc_height, "Test", "RGBA", "U8", "", 120.0)

# The new document has a transparent background, and here I set it to white (so I can write on it)
newDoc.setBackgroundColor(QColor(255, 255, 255, 255))

# I want to save the document right away
newDoc.setFileName(save_path + file_name)
newDoc.save()

# setDocumentInfo to set information about who created it?

# The new document is added to the active window
Krita.instance().activeWindow().addView(newDoc)
