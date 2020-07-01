[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)![GitHub release](https://img.shields.io/github/release/takkii/Lily.svg?style=flat)[![GitHub Status](https://img.shields.io/github/last-commit/takkii/Lily.svg?style=flat)](GitHub)

### プロジェクト名、Lily

#### マイマクロの保存先
>$HOME/Library/Containers/com.collabora.libreoffice-free/Data/Library/Application\ß Support/LibreOfficeVanilla/4/user/Scripts/python

#### 実際にLibreOfficeで作成されるディレクトリ

>$HOME/Library/Containers/com.collabora.libreoffice-free/Data/Library/Application\ Support/LibreOfficeVanilla/4/user/

#### ディレクトリ操作

```markdown
cd $HOME/Library/Containers/com.collabora.libreoffice-free/Data/Library/Application\ Support/LibreOfficeVanilla/4/user/

mkdir Scripts

cd $HOME (任意のユーザディレクトリ)

git clone https://github.com/takkii/Lily.git

cd Lily

mv python $HOME/Library/Containers/com.collabora.libreoffice-free/Data/Library/Application\ Support/LibreOfficeVanilla/4/user/Scripts
```

_※ マイマクロのためにディレクトリ操作するとCalcで実行することができる_

#### LibreOffice側で拡張機能APSOを検索

_→ (インストールまたは既存APSOを使う)_

[ メモ ]

```markdown
動作
・Pythonの標準機能は使える
・LibreOfficeでCalcではシートに反映できる

マイマクロ
・Hello.pyは、Helloなどの文字列操作を行う
・Num.pyは、数字の四則演算を行う
```
