[app]
title = Siti Remote
package.name = sitiremote
package.domain = org.user
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,pyjnius
orientation = portrait
fullscreen = 0

# --- CRITICAL PERMISSION ---
android.permissions = TRANSMIT_IR, INTERNET
android.api = 34
android.minapi = 21
android.sdk = 34
