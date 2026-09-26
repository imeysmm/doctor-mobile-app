[app]

title = Doctor Mobile
package.name = doctormobile
package.domain = ir.doctormobile

source.dir = .
source.include_exts = py,json,png,jpg,kv

version = 1.0

requirements = python3==3.11.9,kivy,requests,urllib3,certifi,charset-normalizer==2.1.1

orientation = portrait
fullscreen = 0


[buildozer]

log_level = 2
warn_on_root = 1


[android]

android.api = 35
android.minapi = 24
android.ndk = 28c
android.archs = arm64-v8a,armeabi-v7a
android.accept_sdk_license = True
android.allow_backup = True

p4a.branch = develop