from krita import *

# I create a new document of size 1600x1200
newDoc = Krita.instance().createDocument(1600, 1200, "Test", "RGBA", "U8", "", 120.0)

# The new document has a transparent background, and here I set it to white (so I can write on it)
newDoc.setBackgroundColor(QColor(255, 255, 255, 255))

# I want to save the document right away, but it is not working yet as expected - look into setFileName() and then save()
newDoc.saveAs("/home/ubprof/Desktop/test.kra")
# newDoc.save()

# The new document is added to the active window
Krita.instance().activeWindow().addView(newDoc)
