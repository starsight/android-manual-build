import os

projectPath = r'C:\Users\zjhew\starsight\Android\MyApplication2'
androidSDKPath = r'C:\Users\zjhew\AppData\Local\Android\Sdk'
keystorePath = r'C:\Users\zjhew\starsight\Android-study\keystore.jks'

#清理目录
os.system(fr"rd /s /q build")
os.system("mkdir build")

os.system(
    fr'aapt2 compile -o {projectPath}\build\res.zip --dir  {projectPath}\app\src\main\res')
os.system(
    fr'aapt2 link {projectPath}\build\res.zip -I {androidSDKPath}\platforms\android-30\android.jar --java build --manifest {projectPath}\app\src\main\AndroidManifest.xml -o {projectPath}\build\app-debug.ap_')
os.system(
    fr'javac -d build -cp {androidSDKPath}\platforms\android-30\android.jar {projectPath}\app\src\main\java\com\example\myapplication\*.java')
os.system(
    fr'd8 --output {projectPath}\build\ --lib {androidSDKPath}\platforms\android-30\android.jar  {projectPath}\build\com\example\myapplication\*.class')
os.system(
    fr'{projectPath}\7za.exe u {projectPath}\build\app-debug.ap_ {projectPath}\build\classes.dex')
os.system(
    fr'{androidSDKPath}\build-tools\29.0.2\apksigner.bat sign -ks {keystorePath} --ks-key-alias wenjiehe --ks-pass pass:wenjie {projectPath}\build\app-debug.ap_')
os.system(fr'cd  {projectPath}\build & ren app-debug.ap_ app-debug.apk')
os.system(fr'adb install -r {projectPath}\build\app-debug.apk')
