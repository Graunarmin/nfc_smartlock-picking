'''
Terminal Skript
zum Scannen nach Device: 
python2 -m nfc
Ausgabe: ** found SCM Micro SCL3711-NFC&RW PN533v2.7 at usb:003:009 (oder andere Zahl, dann auch unten die usb-Nummer ändern!)
'''

import nfc
from nfc.clf import RemoteTarget
import ndef

clf = nfc.ContactlessFrontend()
assert clf.open('usb:003:006') is True

# when switching the tags start again from here:
tag = clf.connect(rdwr={'on-connect': lambda tag: False})
print(tag)

# make sure the data is in ndef format
assert tag.ndef is not None

tag_id = '04236A2A124A81'

#record Types: https://ndeflib.readthedocs.io/en/stable/
tag.ndef.records = [ndef.TextRecord(tag_id)]

assert tag.ndef.has_changed is False

print(tag.ndef.records)




