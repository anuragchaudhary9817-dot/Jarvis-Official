[app]
title = Jarvis
package.name = jarvis
package.domain = org.boss
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Milauna parne main kura haru yaha chhan:
requirements = python3,kivy==2.2.1,pillow,requests
orientation = portrait
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

# Permissions (Jarvis ko lagi internet ra audio chahincha)
android.permissions = INTERNET, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE

# Android API level (Default 33 or 34 rakhda ramro)
android.api = 33
