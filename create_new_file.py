# Author: Giovanni Vincenti

from krita import *

# Basic attributes used through the script

newDocWidth = 1600
newDocHeight = 1200
author = "Giovanni Vincenti"

# I create a new document of size 1600x1200
newDoc = Krita.instance().createDocument(newDocWidth, newDocHeight, "Test", "RGBA", "U8", "", 120.0)

# The new document has a transparent background, and here I set it to white (so I can write on it)
newDoc.setBackgroundColor(QColor(255, 255, 255, 255))

# I want to save the document right away, but it is not working yet
newDoc.saveAs("/home/ubprof/Desktop/test.kra") # This saves a copy, but not the actual document
# newDoc.setFileName(...)
# newDoc.save()

# setDocumentInfo to set information about who created it?

# The new document is added to the active window
Krita.instance().activeWindow().addView(newDoc)
