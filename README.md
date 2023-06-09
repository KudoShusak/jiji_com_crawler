# jiji.com crawler
時事通信社のニュースサイト `www.jiji.com` から記事を収集します。  
Collect articles from `www.jiji.com`, the news site of Jiji Press.

## execution 
```
% python crawling_jiji_com.py
```

カレントディレクトリに２種類のファイル、`xxxxxxxx_xxxxxx_crawlingresult.log`と、`xxxxxxxx_xxxxxx_textdata.log`が出力されます。  
（`xxxxxxxx_xxxxxx`には、実行した日付と時刻からユニークな文字列が入ります）  
Two files, `xxxxxxxxxxxx_xxxxxx_crawlingresult.log` and `xxxxxxxxxxxx_xxxxxx_textdata.log`, will be output in the current directory.  
(where `xxxxxxxxxxxx_xxxxxxxx` is a unique string from the date and time of execution)

* `xxxxxxxx_xxxxxx_textdata.log`  
記事のテキストデータが保存されます。  
The text data of the article is saved.
* `xxxxxxxx_xxxxxx_crawlingresult.log`  
クロールしたURLと、htmlから抽出した記事のデータ（htmlタグ付きと、テキストデータ）が保存されます。  
The crawled URL and the article data (html tagged and text data) extracted from the html are saved.

## Saved data format

### xxxxxxxx_xxxxxx_textdata.log

１記事につき、１行のJSONフォーマットで保存されます。内容は下記の通り。  
One line per article will be saved in JSON format. The contents are as follows

```
{"text":"Article Data"}
{"text":"Article Data"}
{"text":"Article Data"}
.....
```

Example.
```
{"text": "俳優ら実演家、強まる懸念　「数時間で全てスキャン」―専門家は法整備指摘・生成ＡＩ\n　「数時間で全ての音域、声色をスキャンされる」。対話型人工知能（ＡＩ）「チャットＧＰＴ」に代表される生成ＡＩの急速な進展に対し、声優や俳優ら実演家の懸念が強まっている。日本芸能従事者協会（森崎めぐみ代表理事）は実演家らの権利保護を国に要望。専門家も法整備の必要性を指摘している。\n　同協会は会員にヒアリングを実施。ゲーム開発向けなどのため「動作」をデータ化するモーションキャプチャーに応じているというスタントマンは「『危険だから』とＡＩばかりになれば、技術も継承できず、死活問題になる」と回答した。舞踊家からは「映像上の舞踊をコピーされたらどうにでもなるし、振付師の存在価値もなくなる」と不安の声が上がったという。\n　森崎代表は「ＡＩに表現の技術を奪われると、多くの実演家らが仕事を失いかねない」と訴えた。\n　芸能従事者の契約や権利に詳しい佐藤大和弁護士は、実演家らの権利保護のため(1)顔や姿を含む肖像や声、動きなどに関する権利の法律による明文化(2)どのようなデータを基に生成したかなどの開示義務(3)対価の支払い義務(4)本人の意に沿わない使用の差し止め規定―などの必要性を指摘。「文化の発展とのバランスを取りながら、ＡＩ新法などの法整備が必要だ」と話した。\n　文化庁は、ＡＩを利用して生成した画像などの販売に関し、既存の著作物との「類似性」や「依拠性」が認められれば、通常の著作権侵害と同様に損害賠償請求などが可能で、刑事罰の対象にもなるとの見解を示している。同庁はＡＩと著作権の関係などについて啓発活動をする方針だ。"}
{"text": "２５年国連気候会議、ブラジル開催　アマゾンのベレンで―大統領\n　【サンパウロ時事】ブラジルのルラ大統領は２６日、２０２５年の国連気候変動枠組み条約第３０回締約国会議（ＣＯＰ３０）の開催地がブラジル北部ベレンに決まったと発表した。ベレンはアマゾン川の河口付近にある港湾都市で、背後には熱帯雨林が広がっている。\n　ルラ氏はツイッターに投稿した動画で「これまでエジプトやパリ、コペンハーゲンでＣＯＰに参加したが、すべての人が話すのはアマゾンだった。アマゾンの都市で開くのはどうか、アマゾンがどういうものか分かると問い掛けた」と述べた。"}
```

### xxxxxxxx_xxxxxx_crawlingresult.log

１記事につき、１行のJSONフォーマットで保存されます。内容は下記の通り。  
One line per article will be saved in JSON format. The contents are as follows
```
{"url": "https://www......", "contents": ["[Article data with html tags]","[Article data with only text extracted]"]}
{"url": "https://www......", "contents": ["[Article data with html tags]","[Article data with only text extracted]"]}
{"url": "https://www......", "contents": ["[Article data with html tags]","[Article data with only text extracted]"]}
.....
```

Example.
```
{"url": "https://www.jiji.com/jc/article?k=2023052600785&amp;g=soc", "contents": ["[<h1>俳優ら実演家、強まる懸念　「数時間で全てスキャン」―専門家は法整備指摘・生成ＡＩ</h1>, <p>\n\t　「数時間で全ての音域、声色をスキャンされる」。対話型人工知能（ＡＩ）「チャットＧＰＴ」に代表される生成ＡＩの急速な進展に対し、声優や俳優ら実演家の懸念が強まっている。日本芸能従事者協会（森崎めぐみ代表理事）は実演家らの権利保護を国に要望。専門家も法整備の必要性を指摘している。<br/>\n</p>, <p>\n\t　同協会は会員にヒアリングを実施。ゲーム開発向けなどのため「動作」をデータ化するモーションキャプチャーに応じているというスタントマンは「『危険だから』とＡＩばかりになれば、技術も継承できず、死活問題になる」と回答した。舞踊家からは「映像上の舞踊をコピーされたらどうにでもなるし、振付師の存在価値もなくなる」と不安の声が上がったという。<br/>\n\t　森崎代表は「ＡＩに表現の技術を奪われると、多くの実演家らが仕事を失いかねない」と訴えた。<br/>\n\t　芸能従事者の契約や権利に詳しい佐藤大和弁護士は、実演家らの権利保護のため(1)顔や姿を含む肖像や声、動きなどに関する権利の法律による明文化(2)どのようなデータを基に生成したかなどの開示義務(3)対価の支払い義務(4)本人の意に沿わない使用の差し止め規定―などの必要性を指摘。「文化の発展とのバランスを取りながら、ＡＩ新法などの法整備が必要だ」と話した。<br/>\n\t　文化庁は、ＡＩを利用して生成した画像などの販売に関し、既存の著作物との「類似性」や「依拠性」が認められれば、通常の著作権侵害と同様に損害賠償請求などが可能で、刑事罰の対象にもなるとの見解を示している。同庁はＡＩと著作権の関係などについて啓発活動をする方針だ。\n\t<img alt=\"\" height=\"1\" src=\"/news2/kiji_photos/square/dummy/dummy2.png\" width=\"1\"/></p>]", ["俳優ら実演家、強まる懸念　「数時間で全てスキャン」―専門家は法整備指摘・生成ＡＩ", "　「数時間で全ての音域、声色をスキャンされる」。対話型人工知能（ＡＩ）「チャットＧＰＴ」に代表される生成ＡＩの急速な進展に対し、声優や俳優ら実演家の懸念が強まっている。日本芸能従事者協会（森崎めぐみ代表理事）は実演家らの権利保護を国に要望。専門家も法整備の必要性を指摘している。", "　同協会は会員にヒアリングを実施。ゲーム開発向けなどのため「動作」をデータ化するモーションキャプチャーに応じているというスタントマンは「『危険だから』とＡＩばかりになれば、技術も継承できず、死活問題になる」と回答した。舞踊家からは「映像上の舞踊をコピーされたらどうにでもなるし、振付師の存在価値もなくなる」と不安の声が上がったという。", "　森崎代表は「ＡＩに表現の技術を奪われると、多くの実演家らが仕事を失いかねない」と訴えた。", "　芸能従事者の契約や権利に詳しい佐藤大和弁護士は、実演家らの権利保護のため(1)顔や姿を含む肖像や声、動きなどに関する権利の法律による明文化(2)どのようなデータを基に生成したかなどの開示義務(3)対価の支払い義務(4)本人の意に沿わない使用の差し止め規定―などの必要性を指摘。「文化の発展とのバランスを取りながら、ＡＩ新法などの法整備が必要だ」と話した。", "　文化庁は、ＡＩを利用して生成した画像などの販売に関し、既存の著作物との「類似性」や「依拠性」が認められれば、通常の著作権侵害と同様に損害賠償請求などが可能で、刑事罰の対象にもなるとの見解を示している。同庁はＡＩと著作権の関係などについて啓発活動をする方針だ。"]]}
{"url": "https://www.jiji.com/jc/article?k=2023052700192&amp;g=int", "contents": ["[<h1>２５年国連気候会議、ブラジル開催　アマゾンのベレンで―大統領</h1>, <p>\n\t　【サンパウロ時事】ブラジルのルラ大統領は２６日、２０２５年の国連気候変動枠組み条約第３０回締約国会議（ＣＯＰ３０）の開催地がブラジル北部ベレンに決まったと発表した。ベレンはアマゾン川の河口付近にある港湾都市で、背後には熱帯雨林が広がっている。<br/>\n</p>, <p>\n\t　ルラ氏はツイッターに投稿した動画で「これまでエジプトやパリ、コペンハーゲンでＣＯＰに参加したが、すべての人が話すのはアマゾンだった。アマゾンの都市で開くのはどうか、アマゾンがどういうものか分かると問い掛けた」と述べた。\n\t<img alt=\"\" height=\"1\" src=\"/news2/kiji_photos/square/dummy/dummy2.png\" width=\"1\"/></p>]", ["２５年国連気候会議、ブラジル開催　アマゾンのベレンで―大統領", "　【サンパウロ時事】ブラジルのルラ大統領は２６日、２０２５年の国連気候変動枠組み条約第３０回締約国会議（ＣＯＰ３０）の開催地がブラジル北部ベレンに決まったと発表した。ベレンはアマゾン川の河口付近にある港湾都市で、背後には熱帯雨林が広がっている。", "　ルラ氏はツイッターに投稿した動画で「これまでエジプトやパリ、コペンハーゲンでＣＯＰに参加したが、すべての人が話すのはアマゾンだった。アマゾンの都市で開くのはどうか、アマゾンがどういうものか分かると問い掛けた」と述べた。"]]}
```
