# safePower　2023/4/23

ラズパイの欠点の一つに電源スイッチがないというのがあります。
スイッチの付いたUSB電源があれば、良いですが、それでもいきなり電源を切ると運が悪ければ、
microSDが壊れて起動できなくなることがあります。
そこで、安全に電源を入り切りできる基板を作りました。
赤いスイッチで電源投入、もう一方のスイッチでシャットダウンしてから電源を切ります。
機能としてはそれだけですが、

1.初心者にラズパイを使わせる場合
　　　
2.ラズパイを組み込み外部スイッチで電源のon-offしたい場合

などに、使えます。
何気に、shutdownコマンドを入力して、シャットダウンを確認してから電源を切るのが
面倒な人に最適です。

おまけ的にDCプラグをつけていますので、一般のACアダプタ5V2A以上を使えます。

git clone https://github.com/momorara/safePower でラズパイにダウンロードしてください。

2023/4/30
  取扱説明書、組立説明書、部品図面をアップしました。
2023/5/7
  組立説明書修正
