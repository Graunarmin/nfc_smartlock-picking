'''
Terminal Skript
zum Scannen nach Device: 
python2 -m nfc
Ausgabe: ** found SCM Micro SCL3711-NFC&RW PN533v2.7 at usb:003:009
'''

import nfc
from nfc.clf import RemoteTarget

clf = ContactlessFrontend()
assert clf.open('usb:003:009') is True

# bei neuem Tag immer ab hier noch mal:
target = clf.sense(RemoteTarget('106A'), RemoteTarget('106B'), RemoteTarget('212F'))
print(target)
tag = nfc.tag.activate(clf, target)
print(tag)
