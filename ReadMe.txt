
## 手动编译生成一个APK文件
aapt2 compile -o build/res.zip --dir .\app\src\main\res

aapt2 link build/res.zip -I C:\Users\zjhew\AppData\Local\Android\Sdk\platforms\android-30\android.jar --java build --manifest ./app/src/main/AndroidManifest.xml -o build/app-debug.ap_

javac -d build -cp C:\Users\zjhew\AppData\Local\Android\Sdk\platforms\android-30\android.jar C:\Users\zjhew\starsight\Android\MyApplication2\app\src\main\java\com\example\myapplication\*.java

d8 --output build/ --lib C:\Users\zjhew\AppData\Local\Android\Sdk\platforms\android-30\android.jar  build/com/example/myapplication/*.class

aapt package -f -m -J build -S .\app\src\main\res -I C:\Users\zjhew\AppData\Local\Android\Sdk\platforms\android-30\android.jar -M .\app\src\main\AndroidManifest.xml -F build/app-debug.ap_

// linux下运行
zip -j build/app-debug.ap_ build/classes.dex

// 修改扩展名ap_为apk

C:\Users\zjhew\AppData\Local\Android\Sdk\build-tools\29.0.2\apksigner.bat sign -ks C:\Users\zjhew\starsight\Android-study\keystore.jks --ks-key-alias wenjiehe --ks-pass pass:wenjie build/app-debug.apk

adb install -r C:\Users\zjhew\starsight\Android\MyApplication2\build\app-debug.apk
