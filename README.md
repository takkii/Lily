### プロジェクト名、Lily

_LibreOfficeのあれこれ_

マイマクロの保存先
> $HOME/Library/Containers/com.collabora.libreoffice-free/Data/Library/Application Support/LibreOfficeVanilla/4/user/Scripts/python

実際にLibreOfficeで作成されるディレクトリ
>cd HOME/Library/Containers/com.collabora.libreoffice-free/Data/Library/Application Support/LibreOfficeVanilla/4/user/

>mkdir Scripts

>mv python $HOME/Library/Containers/com.collabora.libreoffice-free/Data/Library/Application Support/LibreOfficeVanilla/4/user/Scripts

※ pythonフォルダはLilyから移動してもよい。

#### LibreOffice側で拡張機能、APSOを検索

[ メモ ]

```markdown
動作
・Pythonの標準機能は使える
・LibreOfficeでCalcではシートに反映できる

マイマクロ
・Hello.pyは、Helloなどの文字列操作を行う
・Num.pyは、数字の四則演算を行う
```