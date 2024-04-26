#!/bin/sh

/usr/local/bin/platypus \
  --droppable \
  --quit-after-execution \
  --app-icon '/Applications/Platypus.app/Contents/Resources/PlatypusDefault.icns' \
  --name 'GDrive Opener' \
  --interface-type 'None' \
  --interpreter '/usr/bin/python3' \
  --author 'msolo' \
  --bundle-identifier com.github.msolo.GDriveOpener \
  --uniform-type-identifiers 'public.item' \
  './gdrive-opener.py' \
  './GDrive Opener.app'