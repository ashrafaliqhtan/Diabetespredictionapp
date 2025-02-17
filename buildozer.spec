[app]

# (str) Title of your application
title = DiabetesApp

# (str) Package name
package.name = diabetesapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.diabetesapp

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1.0

# (list) Application requirements
requirements = python3,kivy,absl-py,Babel,blinker,certifi,charset-normalizer,click,dash,dash-core-components,dash-html-components,dash-table,Flask,flask-babel,Flask-WTF,flatbuffers,google-pasta,grpcio,h5py,idna,importlib-metadata,itsdangerous,Jinja2,joblib,keras,Markdown,MarkupSafe,numpy,packaging,pandas,plotly,protobuf,Pygments,python-dateutil,pytz,requests,retrying,rich,scikit-learn,scipy,six,tenacity,tensorboard,tensorflow,termcolor,threadpoolctl,typing-extensions,urllib3,Werkzeug,wrapt,WTForms

# (str) Presplash of the application
presplash.filename = %(source.dir)s/assets/presplash.jpg

# (str) Icon of the application
icon.filename = %(source.dir)s/assets/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (string) Presplash background color (for new android_tools, use rgba in #AARRGGBB format)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow
android.presplash_color = #FFFFFF

# (list) Permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 30

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (str) Android architectures to build for, choices: armeabi-v7a, arm64-v8a
android.archs = armeabi-v7a,arm64-v8a

# (str) python-for-android branch to use, defaults to master
p4a.branch = develop

# (str) Bootstrap to use for android builds
p4a.bootstrap = sdl2

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
p4a.port = 8080

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
