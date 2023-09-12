### AI与传统数据库 - ChatGPT风过之后 ｜ 从Duet AI说开来


OpenAI的突破震撼整个市场已经半年有余，在初期的震惊之后，整个业绩膝跳反应，全体搭车。训练大模型有之，抓紧囤货有之，直接改BP的最多。

靠数据库吃饭多年的我却纠结在思考漩涡中。N多年前的项目申请的PPT上就写过AI-powered Optimizer[^1]，而且是深思熟虑过的三步走（这样三年都有经费了）。后来慢慢的AI for DB或DB for AI陆续出现了，我已经记不清是在哪个东家的规划策略中了，大概是都有的。AI for DB，比如NLP to SQL（现在太多了[^2]）, ML-Based buffet pool 调优，当然还有万变不离其宗的优化器；DB for AL: 就是为在数据库里提供ML算子，或者直接脱离狭义的关系数据库，赶上embeded DB (即向量数据库）的风头[^3]，后者继续图数据库[^4]上深耕。

渴望成为风口的千百中的一只，思路却还停留在自己的茧房里。上面的东西在过去六七年场景中辩论过无数次，都有些东西，但作下来又都感觉不踏实。比如说，[NLP2SQL](https://github.com/nidmgh/techTrend/blob/main/NLP2SQL.py), 这是笔者化了两个小时写的人生第一个（也许是第二次？）python code，其中有半个小时在学习如何在浏览器上开一个可互动的对话框了。一个普通程序员两个小时的商业价值是很难飞起来的，即使在风口。

想了几个月，没有答案，不妨碍去探索。三人行必有我师，俗称“作业借我抄抄”。今天借Google的AI collaborator 工具 DuetAI[^8]谈谈自己的想法.

[^1]: 真正的idea来源于团队的优化器专家，现在是某top国产数据库的head of Engineering。我只是前台翻PPT的。
[^2]: 《当LLM遇到Database：阿里达摩院联合HKU推出Text-to-SQL新基准​》(阿里：https://developer.aliyun.com/article/1262738); TiDB Chat2Query(https://www.pingcap.com/chat2query-an-innovative-ai-powered-sql-generator-for-faster-insights/); 《数据库开发工具界的 ChatGPT 来了》(https://www.bilibili.com/video/BV1XT411r7HQ/； NineData：基于 AI(GPT) 的 SQL 优化，不好意思夹带私货） 
[^3]: 阿里最近宣传的PGVector和开源的chroma（https://github.com/chroma-core/chroma）
[^4]: NebulaGraph and TigerGraph
[^8]: 部分信息来源于： https://cloud.google.com/blog/products/ai-machine-learning/duet-ai-in-google-cloud-preview。Duet AI号称可以干很多事情。鉴于笔者的知识范围，只探究数据库/数据处理/云数据相关的内容。本文并不重点在google的Duet AI，而是借助其服务场景谈谈自身的思考。建议大家参阅原文和自己试试Duet AI，毕竟“原始材料”要靠谱的多。

#### 1. NLP2SQL之后呢？

自然语言到SQL面向的客户，期望解决的问题很明显：客户学习写SQL了。之后呢？真的不需要懂SQL了吗？ Google在讲这个问题的时候引用了一个化妆品L’Oréal的架构师的一段话。笔者个人也在新加坡拜访过SEPHORA的亚洲总部。换位思考一下，有几位读者能说清楚口红的颜色。既然说不清看不懂，那么如果销售员推荐一个YSL小金条1966[^A1]，在我脑海里比量子力学还难了。

同样的道理，通过自然语言生成了一个SQL，且不说性能调优问题。最终用户能够判断该查询的准确性，如何解读结果？自然语言到SQL并没有真正解决这个问题，而是需要把SQL Query的结果再解析出来，生成报告用户可以理解内容。AIGC完成自闭环。[Duet AI in Google Cloud - data analysis and visualization](https://www.youtube.com/watch?v=gtehwj1G4tU), 便是Google Next 23 keynote中的一个例子。NLP+BigQuery+Looker, 自然语言为输入，PPT为输出。

注意，在完成PPT向领导汇报这一个实际工作的同时，还解决了一个关键性的技术性问题。就是，让我们的客户真正的能够用其领域知识理解输出的结果。图表报告的正确性与否，是与客户的专业知识想互作用的，她/他的专业经验和日常感觉判断。因为只有这些客户才了解的业务的实际情况，而不是冷冰冰的数据库查询结果。上帝的归上帝，凯撒的归凯撒；SQL归数据库码农，口红色号归化妆专业人士，大家各司其职，贡献专业知识。

* 技术路径：NPL2SQL + Data Warehouse + Marp[^A5]

[^A5]: a Markdown to PPT tool. 笔者在过去10个月一直使用它。挺好玩，还不成熟。


[^A1]: 据说是10支大牌经典口红色号，反正我不懂。https://www.zhihu.com/tardis/zm/art/565109678?source_id=1003

#### 2. 数据库迁移：百里之行半九十

数据库迁移是几十年的老话题。其中数据库兼容性，数据迁移，Schema转换，应用重写（COBOL万岁 ），祥林嫂都觉得烦了。可问题和业务都还在，占有每一个CIO老总预算的40%（抱歉，记不得出处了）。其中简单的东西有各种工具都解决了，不管是数据库内核的兼容性[^B1]，还是转换工具的革新更新换代，已经把门槛推到了95%。这个数据来自笔者的小学一年级加减法：4年前在吉隆坡一角的会议室里的我给客户业务的分析结果。那是一个帮助马来西亚的电商从Oracle RAC迁移到PolarDB的例子，我们最后的困难也在这5%。从鉴于对客户信息的尊重，这里只分享公开的材料[“Goodbye Oracle! Exclusive Insights into PrestoMall’s Transition to Alibaba Cloud”](https://alibaba-cloud.medium.com/goodbye-oracle-exclusive-insights-into-prestomalls-transition-to-alibaba-cloud-d24b05058777), 从Oracle到PG需要手工修改80%的code，采用当时的自动化工具（programming language and schema conversion) 可以减少到10% , 使用当时的PolarDB兼容O的版本，减少到5%。

对的，客户CTO和我也都知道，数据库迁移的最后的5%是多么困难的一座山。很幸运，我们成功了。With good tools and many man-months power。**这5%便是AIGC可以带来的创新点**。

Duet AI 作为数据库开发者的辅助工具，可以再推进2～3%。除了可以比较把老朽的CPP[^B2]转化成代表新潮流GO外，它还可以把自适应的原始端的数据库API转化成目标端的数据库API，当然目标端是GCP自己的云数据库AlloyDB了。比较有趣的魔鬼在于细节，这里并不是革命，而一个个螺丝钉拧上去的革新。[Duet AI in Google Cloud - database management](https://www.youtube.com/watch?v=u6489QehgdQ) 展示从Oracle到 AlloyDB（PG为根基的云数据库) ，其中自动标识localtimestamp() 到 clock_timestamp()，并且举一反十的全局修改。这是一个把半天工作量削减到30分钟的小动作（销售人员会说削减到1分钟... 我不是个好销售）。

这点小改进并不专属于数据库迁移，但在这个场景下--数据库迁移的应用改造中，cost/return收效最好。因为迁移的开放与原应用的开发，已经有n多个代差，客户程序员也没有兴趣，也没有能力去理解原始程序。而原始应用中一定会有多年积攒的重复性的逻辑片段，通过机器学习来去举一反N才是程序猿copy/paste的最好朋友。

* 实现路径：existing data replication and schema conversation tool + drivers for cloud databases + GitHub co-pilot^[B5]



[^B1]: PG生态的EDB(aka Enterprise DB), 国内的PolarDB-O，Oceanbase-O
[^B2]: 坐在mainframe里的COBOL捋着胡子说：你过来呀？ 
[^B5]: copilot是技术关键。需要针对数据库应用定制。

#### 3. DBA对于数据库报警的漠不关心
刚刚接触云客户业务的时候，去约一位资深技术Lead。他说好啊，刚好晚上他值班，所以有空：“咱们晚上9点吧，赛银国际的一个酒吧，还是不错的”。我以前也做过值班经理工作，每次值班都如临大敌，非常紧张。因为支持的是大客户，“运气好”的时候，可以上新闻头版的。

这位是很资深的老员工，深耕集团内外技术支持多年。落座之后，先叫了杯酒，然后提到一般两人轮换值一天，他更愿意自己扛24小时。这样子只耽误一天时间。聊天的两个小时过程中，他的手机时刻都在震动着。他也不得不时不时瞟一眼报警，偶然中断一下我们兴致勃勃的八卦，去翻一下详细的信息。两年后，疫情期间，我遇到另一位正在值班的同事。酒吧好像已经关了（不知道是否是暂时的），但他值班的方式和流程没有变化。也许是我的心理作用，唯一变的就是报警更频繁了。

对比我当年的值班，这位老兄的确是处事不惊，泰然自若。可另一方面我每个班能有两个电话就已经是非常繁忙的，因为客户的DBA是我们最前沿的保护，他手里的脚本和自身的经验保证了报警的高质量，而不是直接推到我的手机上。而这位老兄手机上的几千次的所谓的报警为什么会发生呢？客户将IT服务通过云托管的方式“外包”给了云厂商。云的技术人员对于客户的业务其实是不了解的，无法真正的的判断报警的分级和处理的方法。所以常年来（为了免责也是一大原因）报警数量有增无减，造成了99.x%无用的信息。但消耗了大量的人工力量，系统报警的严重污染，用所谓的完整性，消耗了实际的服务效率。那位资深老哥值班的过程中，无法做有意义的事情，即不能为公司工作，也不能陪伴家人。也许同我一起八卦是最高效的产出了。


Google提出了[Duet AI in Google Cloud - troubleshooting issues](https://www.youtube.com/watch?v=MBAuTQdtZ0o)。其实这不是什么新东西。Snowflake的成功，就很大程度上归功于其Service with Scalability。Snowflake的运维每天生成几十T的日志数据，而且业务持续稳定增长。之所以能够跨越增服（业务）不增人（工程师）的创业公司门槛，便是有效的完成了日志自动化。在这个门槛上跌倒的的公司很多，包括现在的国内主力云服务商。

之前对于数据库系统的一些排错的方式，非常依赖于比较有前瞻性的SQL Error Message的设计。比如[MySQL 8.0 Error Message Reference](https://downloads.mysql.com/docs/mysql-errors-8.0-en.a4.pdf)有786页，体现了30年的积累。 现在AI大模型帮助可以更快的总结系统错误，分析系统重大问题之前的N个小时的状态，尤其是当时没有注意到的报警（帮助我那位值班的老哥，从无效的报警中解脱出来）。这便是新技术，面对旧场景的革新。

* 技术路径：时序数据库（一般的数仓也够了）+ 针对数据库日志的大模型训练 + 反馈机制[^C5].

[^C5]: 华人开发的时序数据库有TDEngine和Timeplus; Meta开源的Llama大家肯定听说过；反馈机制需要专门设计，暂时没有方案。  


<!--
#### 有容乃大，天下归心：API Management
Lego 李飞飞

https://www.youtube.com/watch?v=Cpp1FF5SlyY

[^D5]: 来源于阿里李飞飞老师在VLDB2023的主题演讲《Modernization of Databases in the Cloud Era: Building Databases that Run Like Legos》。本文是其关于乐高类比的延伸。
-->

####  写个尾巴
AI for DB和DB for AI上面两个方向当然都有各自的故事可以讲，我也都去讲过。个人以为数据库内核已经足够成熟，已经人力优化多年，现在的AL水平是无法提供实际提高的（个人并不反对这方面的学术工作或者大厂的research lab）。内核的提高还有待观望，与日常IT工作相关的DMaaS反而可以先发，利用今天的AI技术产生革命性的东西。上面的三个突破点的技术路线是可以立刻发力的

<!--
老狗不要去跟年轻人拼体力，那叫自不量力。选择自己技术领域，作为专家来去训练自己熟悉的模型才能有所突破。
-->

The above ideas were formed at Bodega Bay.

![](./images/BodegaBay.jpeg)



