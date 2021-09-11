#!/bin/bash
cd "`dirname "$0"`"
pwd

echo

if [ -d ~/Library/Application\ Support/Glyphs\ 3 ]; then
    echo "正在拷貝檔案到 Glyphs 3 資料夾..."
    [ ! -d ~/Library/Application\ Support/Glyphs\ 3/Info ] && mkdir ~/Library/Application\ Support/Glyphs\ 3/Info
    cp ./Info/G3/* ~/Library/Application\ Support/Glyphs\ 3/Info/
    cp -r ./Info/Icons ~/Library/Application\ Support/Glyphs\ 3/Info/
    [ ! -d ~/Library/Application\ Support/Glyphs\ 3/Scripts ] && mkdir ~/Library/Application\ Support/Glyphs\ 3/Scripts
    [ ! -d ~/Library/Application\ Support/Glyphs\ 3/Scripts/vanilla ] && echo "您沒有安裝 vanilla 程式庫，請至 Glyphs 的外掛管理員安裝。"
    cp -r ./TaiwanTool ~/Library/Application\ Support/Glyphs\ 3/Scripts/
else
    echo "在電腦上找不到已安裝的 Glyphs 3"
fi 

echo

if [ -d ~/Library/Application\ Support/Glyphs ]; then
    echo "正在拷貝檔案到 Glyphs 2 資料夾..."
    [ ! -d ~/Library/Application\ Support/Glyphs/Info ] && mkdir ~/Library/Application\ Support/Glyphs/Info
    cp ./Info/G2/* ~/Library/Application\ Support/Glyphs/Info/
    cp -r ./Info/Icons ~/Library/Application\ Support/Glyphs/Info/
    [ ! -d ~/Library/Application\ Support/Glyphs/Scripts ] && mkdir ~/Library/Application\ Support/Glyphs/Scripts
    [ ! -d ~/Library/Application\ Support/Glyphs/Scripts/vanilla ] && echo "您沒有安裝 vanilla 程式庫，請至 Glyphs 的偏好設定裡安裝。"
    cp -r ./TaiwanTool ~/Library/Application\ Support/Glyphs/Scripts/
else
    echo "在電腦上找不到已安裝的 Glyphs 2"
fi 

echo
echo