# TaiwanKit 台灣字型工具

## 台灣文字表

![TaiwanPlist](Images/TaiwanPlist.png)

此工具是由兩部分組成，一為左側的字表（Info/Group-Taiwan.plist）。
注意，若您有自訂 Group.plist 檔案在先，在 Glyphs 2 下會被覆蓋，請做好備份。

此字表收錄了製作繁體中文字型時通常需要製作的符號、分類漢字表（如教育部字表、台客語漢字、姓氏與地名等），以及台客語拼音支援等。

在 Glyphs 3，右鍵選單會明確顯示出缺的字符是什麼字了，相當棒。可惜 Glyphs 2 還是只有顯示字符名稱。

![TaiwanPlist2](Images/TaiwanPlist2.png)

分類名稱加有 ㊟ 的項目，是搭配下面腳本程式使用的。


## 繁中字型符號幫手

![TWSymbolMate](Images/TWSymbolMate.png)

使用此腳本，可以將多數能夠程式化自動完成的符號字符全部自動產生完成。
包括：

* 做完半形符號後，自動產生全形符號。
* 自動產生圈號數字、括號數字的工具。
* 調整以上全形字符直排時上下方超界的字符（自動調整直排原點）。
* 自動鏡射、旋轉對稱的符號（也就是像括號、箭號等，只要製作一個，其他都可以自動產生出來）。
* 快速繪製產出表格符號的工具。

應該會讓製作符號的工程更快、更準確。


以上自動產出作業，都是以組件的方式生成的。除非自己拆開組件，否則都會跟著來源字符設計而跟隨改變，可保持兩者之間的一致性。


## 安裝

解開 TaiwanKit.zip 之後，右鍵點選 install.command ，選擇用終端機執行即可安裝。

![Install.png](Images/Install1.png)

有可能出現安全性警告，就勇敢接受他吧。

![Install.png](Images/Install2.png)


繁中字型符號幫手是基於 Python 與 vanilla 程式庫開發的，需要安裝相關程式庫。
安裝方法是：

### Glyphs 2

Glyphs > 偏好設定 > 外掛 > 模組 > 安裝模組

### Glyphs 3

視窗 > 外掛程式管理員 > 模組 ，請安裝 Python 與 Vanilla。

### 影片教學

完整的安裝與使用教學已經錄成 YouTube 影片，可在此網址觀看：
https://youtube.com/playlist?list=PL5uJ1QN0G69n69qHHexFMeKV2cnBpzNmb

影片裡當時是介紹手動複製方式安裝，透過 install.command 安裝可跳過手動複製的動作（容易不小心覆蓋整個資料夾，比較危險）。
