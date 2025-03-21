#!/bin/sh

# Make sure the Platypus app has installed it's CLI

/usr/local/bin/platypus \
  --droppable \
  --quit-after-execution \
  --app-icon '/Applications/Platypus.app/Contents/Resources/PlatypusDefault.icns' \
  --name 'GDrive Opener' \
  --app-version '1.1' \
  --interface-type 'None' \
  --interpreter '/usr/bin/python3' \
  --author 'msolo' \
  --bundle-identifier com.github.msolo.GDriveOpener \
  --uniform-type-identifiers 'public.item' \
  './gdrive-opener.py' \
  './GDrive Opener.app'