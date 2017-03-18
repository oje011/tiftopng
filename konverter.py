import os
from PIL import Image

yourpath = str(raw_input("Mappen der de skannede bildene er: \n"))
converted = yourpath + "\konvertert"
if not os.path.exists(converted):
    try:
        os.makedirs(converted)
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

for subdir, dirs, files in os.walk(yourpath):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".tif"):
            print filepath
            filename = file[:-4]
            #pngfile = subdir + os.sep + filename + ".png"
            outfile = subdir + os.sep + "konvertert" + os.sep + filename + ".png"
            if os.path.isfile(outfile):
                print "Filen er allerede konvertert."
            else:
                try:
                    im = Image.open(filepath)
                    print "Konverterer bilde for: %s" % file
                    im.thumbnail(im.size)
                    im.save(outfile, "PNG", quality=100)
                except Exception, e:
                    print e

print "Bildene dine er nå konvertertert ;)"
