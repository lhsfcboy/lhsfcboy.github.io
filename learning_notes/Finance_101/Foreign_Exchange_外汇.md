# 外汇交易业务基础知识

FX is a continuous global business which we say operates on a 24 by 5.5 schedule – 24 hours a day, 5 and a half days a week.

The trading week begins with Wellington New Zealand open on Monday morning at 4am JST, and runs until NYC Close at 5:00pm EST on Friday afternoon (Sun 15:00 EST – Fri 17:00 EST).

Volume goes much higher during economic events or announcements which lead to currency volatility.

阅读本文需要读者有基本的股票证券市场知识。

## 报价

一个货币对报价中的第一个货币为基础货币，而第二个货币为报价货币。

- EUR/USD @1.25

如果您以1.1250买入欧元/美元，您将支付1.1250美元（USD）换取一单位的欧元（EUR）。

## 基差

货币对的期货价格和现货价格之间的差额被称为“基差”。

如果报价货币的短期利率低于基础货币的短期利率，期货应该以现货价格的折价交易。基差（期货减去现货）将报价为负数。

墨西哥比索/美元期货的美式报价为MXN/USD。墨西哥比索是基础货币。假设它的短期利率为4.25%，设美元的同等期限短期利率为0.70%。美元利率低于墨西哥比索利率。这意味着正利差，所以期货价格应该低于现货。 

###### Business Breakdown

- By Products: Spot/Forward vs Options
- By Market: G10 Currencies vs EM (Emerging Markets)
- By Flow: Edealing vs Franchise


###### Settlement

Spot is T+1 day if the currency pair is USD/CAD, USD/TRY, USD/PHP or USD/RUB.

###### G10 currencies vs EM (Emerging Markets)

United States dollar (USD)
Euro (EUR)
Pound sterling (GBP)
Japanese yen (JPY)
Australian dollar (AUD)
New Zealand dollar (NZD)
Canadian dollar (CAD)
Swiss franc (CHF)
Norwegian krone (NOK)
Swedish krona (SEK)

###### Ecnomic Events

- Monthly NFP announcement
  - Nonfarm Payroll - It is an influential statistic and economic indicator released monthly by the United States Department of Labor as part of a comprehensive report on the state of the labor market.
  - Nonfarm payroll employment is a compiled name for goods-producing, construction and manufacturing companies in the US. It does not include farm workers, private household employees, non-profit organization employees, or government employees
  
  
## 外汇市场结构

###### 银行间市场(インターバンク市場) 
証券取引所のような「中央」は存在しません。それがインターバンク市場です。ここに各銀行や証券会社がレートを提示して取引を行います。規模の大きな金融機関だけが参加するプロ同士のやりとりです。
ここでは、貿易の1件ごとの取引に応じて為替取引をするわけではありません。ある銀行にきた注文が、輸入企業Aからのドル買い150万ドル、輸出企業Bからのドル売り100万ドルがあったとしたら、差額の50万ドルをインターバンク市場で調達し、B社から受け取った100万ドルと合わせた150万ドルをA社の口座に入れてあげればいいのです。

このとき、ドルをいくらでどういうタイミングで調達するかの判断は完全に銀行に任せられています。この判断のことを「**ディーリング**」といい、できるだけ安くドルを調達できればそれだけ銀行の利益が増えることになります。

###### 与证券市场的对比
株式の取引の場合、そのほとんどは証券取引所でなされます。日本の場合、さらにそのほとんどが東証で行われます。証券会社はたくさんありますが、実店舗の証券会社でもネット証券でも、それらは東証へ注文を出すのを中継しているだけです。完全に同じ銘柄・注文内容・時刻に発注すれば、どの証券会社を利用しようとも、起こる結果は同一なのです。違うのは手数料（これは証券会社により異なります）だけです。

株式の場合、東証のリアルタイムの注文状況はどの証券会社でもわかるので、出した注文が取引所に届いたかどうかは東証のデータを見ていればわかります。ところが為替の場合、出した注文がその先にどう処理されるのか、注文を出した側からはまったくわからないブラックボックスなのです。

FX会社は何をしているのでしょうか？　一般個人の小口注文を受け付けるのは証券会社と同じですが、その先にインターバンク市場につながっているのが株式取引とは違うところです。FX会社がインターバンク市場に流す注文を「**カバー**」、注文が執行されることを「**カバーを取る**」と言います。

FX会社小口の注文を受け付ける，いちいちインターバンク市場に流さず、ある程度まとまった段階で「カバーを取る」

最近は、「インターバンク直結型」を謳ったFXのサービスもいくらか出てきました。これらは顧客の注文を逐一インターバンク市場に流すタイプのサービスですが、一般的には取引単位が大きい・約定率が低い・別途取引手数料が徴収される、といった傾向があります。

#### ディーラーの大損失に備える「行動制約・冷却ペナルティ」の例

（1）決まった時刻（NY市場のクローズや、ディーラーが別のディーラーに業務を交代する時刻）では、顧客の全ポジションをカバー済みの状態にするよう義務付ける
こうすれば、ディーラーも「遅くともあとXX時間ではカバー注文をしなければならない」と頭に入るので冷静になりますし、会社全体の一日ごとの損益額をはっきりさせるためにも有用です。

（2）週またぎ禁止
FX市場は土曜・日曜の約48時間は動きません。一日ごとには全部カバーしない場合でも、最低限週末だけはカバーしておこう、というものです。

週末の、カバー取引できない間に相場状況が急変することは非常にまれにしか起きませんが、起きるときは強烈な影響があります。


 
古くはニクソン・ショック（アメリカの金本位制放棄）がありますし、東日本大震災のときも地震発生は金曜の午後でしたが、被害の想定外の大きさが明らかになるのは相場が停止する土曜朝以降のことでした。

（3）上限数量、上限損失
ディーラーが未カバーで持っていいポジションサイズに上限を設けたり、その評価損が一定額に達したら強制的にカバーをさせる、というものです。

また、ディーラーが頭を冷やして冷静になる時間を強制的につくるために、「強制カバールールに抵触したディーラーはその後24時間はディーリング業務禁止」という社内規定を持っているところもあります

#### 交易术语

PIP   100 PIP = 1 JPY

##### 交易页面

Left Side, BID price < Right Side, Ask price.

ASKとBIDの差（表では2.1銭）をスプレッド


### 平盘
外汇平盘，指银行在办理代客结售汇业务或自身结售汇业务后，通过外汇交易市场将外汇结汇头寸卖出或买入外汇头寸，用于补充售汇头寸的交易。
银行收集个人客户外汇一定数量后，向国际外汇市场转嫁风险时的过程。
