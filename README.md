# safePower

<h4><<概要>></h4>
　ラズパイの欠点の一つに電源スイッチがないというのがあります。<br>
　スイッチの付いたUSB電源があれば、良いですが、それでもいきなり電源を切ると運が悪ければ、
microSDが壊れて起動できなくなることがあります。<br>
　そこで、安全に電源を入り切りできる基板を作りました。
　赤いスイッチで電源投入、もう一方のスイッチでシャットダウンしてから電源を切ります。
　機能としてはそれだけですが、安心感が違います。<br>
  ちゃんとしたケースに入れて外部スイッチを付ければ、子供や他人に使ってもらうのも安心です。<br>
  <br>
1.初心者にラズパイを使わせる場合<br>
2.ラズパイを組み込み外部スイッチで電源のon-offしたい場合<br>
などに、使えます。<br>
何気に、shutdownコマンドを入力して、シャットダウンを確認してから電源を切るのが面倒な人に最適です。<br>
<br>
おまけ的にDCプラグをつけていますので、一般のACアダプタ5V2A以上を使えます。
これにより、頻繁にUSBコネクタを抜き差ししてラズパイが壊れるのも防げます。

　すべてのソースプログラムを開示いたします。<br>

・LEDの色等指定はできません。<br>
・部品の仕様が変わる場合があります。 <br>
・基板のバージョンが変わる場合がありますが、機能等に違いはありません。<br>
・ラズパイは付属しません。<br>

<h4><<使用方法>></h4>
git clone https://github.com/momorara/safePower<br>
でラズパイにダウンロードしてください。<br>
インストールについては、インストール文書に従いインストールを行ってください。<br>

<h4><<使用説明資料>></h4>
説明書類の中の資料を確認ください。
お問い合わせに関しては、サポート.txtを参照ください。><br>

<h4><<動作環境>>></h4>
2023/8/4 bullseye 11.7で動作確認><br>

<h4><<ライセンス>></h4>
使用しているライブラリについては、ライブラリ制作者のライセンス規定を参照ください。
オリジナル部分については、オープソースとさせていただきます。
Released under the MIT license です。
プログラム自体はサンプルプログラムです。

