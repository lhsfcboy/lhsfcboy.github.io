# LaTeX

> 本文编辑于MarkDown格式下...


## 编译套装

两大选择

- TexLive
- MiKTeX

前者大而全, 体积上G. 
内置了可以处理中文的XeLaTeX.

MiKTeX体积小, 会在需要时自动下载配置缺少的包. 
同样内置了可以处理中文的XeLaTeX.

### 基本的排版流程


.tex --(latex)--> .dvi --(dvipdfmx)--> .pdf

.tex --(xelatex/pdf/atex) --> .pdf


### 一个编译的例子
```
latex -interaction=nonstopmode %.tex|（編譯 latex 檔案）
bibtex %.aux|（編譯論文引用的資料）
latex -interaction=nonstopmode %.tex|（再編譯一次）
latex -interaction=nonstopmode %.tex|（再編譯一次）
xdvi %.dvi（產生 pdf 檔）
```

使用XeLaTeX且没有参考文献时:
```
xelatex -interaction=nonstopmode %.tex|
xelatex -interaction=nonstopmode %.tex|
xelatex -interaction=nonstopmode %.tex|
xdvi %.dvi
```
省去了bibtex以避免无谓的编译警告

## 中文文档
LaTeX 中文文档的排版有各种方式，例如CCT，CJK，xeCJK 等等。
目前最优秀的方式是用ctex 文档类来排版中文文档，它在其它各种方式的基础上以一致的方式解决了中文排版的问题。
> \documentclass[UTF8]{ctexart}
使用这种方式，只需要将文档类从英文的article 改成ctexart，所有中文环境和章节编号等等都已经按照中文习惯设置好了，简单易行。另外，对于book 和report 文档类，也有对应的ctexbook 和ctexrep 中文文档类，其用法类似。

例子中的UTF8 这个可选参数指明了中文文档的编码。编码主要有这两种：GBK 和UTF8，而不同的LaTeX 编辑器对中文文档的默认编码不同。

## 附录

### LaTex常见的文件类型汇总

|扩展名|说明|
|----|----|
|.aux|存放交叉引用信息|
|.bbl|由BiBTeX 生成，会被LaTeX使用的参考文献列表|
|.bib|参考文献数据库，以便引用|
|.blg|存储BiBTeX日志|
|.bst|指定BiBTeX样式文件，即BiBTeX将.bib生成.bbl的格式，不同的期刊有不同的参考文献样式|
|.cls|定义文章的排版布局，即定义.tex稿件类型格式，使用\documentclass{article} 命令进行指定|
|.dtx|程序说明文件的源文件，含有类包程序*.cls、宏包程序*.sty、说明或格式程序*.tex和配置程序*.cfg等多|种程序。
|.ins|用来解压和重建.dtx文件。用户下载了一个LaTeX包后，通常会获取一个.dtx和一个.ins文件，使用*.ins|安装文件的好处就在于它能够一次性自动地完成对*.dtx文件的分类重建工作。
|.fd|新添加的字体描述文件，用来告知LaTeX新添加的字体|
|.dvi|一种不依赖设备的文件。.dvi文件是latex编译运行后的主要结果。用户可以使用DVI预览软件查看.dvi内容|。
|.pdf|PDF文件，文件是pdflatex编译运行后的主要结果。|
|.log|记录上一次编译器运行的日志。|
|.toc|存储对于章节目录，TEX 程序第一次编译文档时会生成 .toc 临时文件，下一次编译时将读取.toc |文件内容并生成新的目录。
|.lof|类似于.toc，不过是用来存储插图目录。|
|.lot|类似于.toc，不过是用来存储表格目录。|
|.idx|存储索引内容的文件，可用makeindex排序后创建索引文件.ind。|
|.ind|处理.idx文件得到的索引文件，下一次编译时将读取.ind文件内容并生成新的索引文件。|
|.ilg|makeindex的日志文件。|
|.sty|LaTeX宏包文件，使用\usepackage将.sty加载到LaTeX中。|
|.tex|LaTeX和TeX源文件，进行编译处理。|
