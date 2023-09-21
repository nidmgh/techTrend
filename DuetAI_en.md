### AI and Database - After the Hype of ChatGPT ｜ Reflections upon *Duet AI* 


OpenAI's breakthrough shocked the entire market, and the initial astonishment created knee-jerk reactions all over the place with everyone jumping on the bandwagon:  train LLM,  stock up GPU, and modify business plan.

On another hand, the integration of Databases and AI has been floating around long before openAI's hype:

* **AI for DB**: NLP2SQL[^A1] or ML-Based buffet pool, such as iBTune,[^A3] and certainly Query-Optimizer.  
* **DB for AI**: A special designed datastore or embedded/vector DB to provide high performance KNN[^A5]，or Graph Database[^A7] for AI and ML operators。

Myself took a quick exercise of [NLP2SQL](https://github.com/nidmgh/techTrend/blob/main/NLP2SQL.py), a two-hour development  demonstrating the power of OpenAI: 1) NLP2SQL; 2) 'teach' me how to code in Python. Impressed by the power of AI,  **I am not convinced that current AI technology is ready to revolutionize database** because RDBMS has been handcrafted by generations of elite engineers. 

Good news is that the Database service-related products probably can benefit from the innovation immediately, which partially coming from the recently *Duet AI* announcement.[^A9]

[^A1]: 《当LLM遇到Database：阿里达摩院联合HKU推出Text-to-SQL新基准​》(阿里：https://developer.aliyun.com/article/1262738); TiDB Chat2Query(https://www.pingcap.com/chat2query-an-innovative-ai-powered-sql-generator-for-faster-insights/); 《数据库开发工具界的 ChatGPT 来了》(https://www.bilibili.com/video/BV1XT411r7HQ/； NineData：AI(GPT)-powered SQL optimization） 
[^A3]: iBTune: Individualized Buffer Tuning for Large-scale Cloud Databases, VLDB'2019
[^A5]: PGVector, or chromaDB（https://github.com/chroma-core/chroma）
[^A7]: NebulaGraph and TigerGraph
[^A9]: https://cloud.google.com/blog/products/ai-machine-learning/duet-ai-in-google-cloud-preview。Duet AI covered a wide scenarios. This article only discusses database related.

#### 1. What happen to NLP2SQL？

Use case of NLP2SQL is clear: to bypass the learning curve of SQL. Really?

When discussing this issue, Google cited a statement from the architect of the cosmetic brand L’Oréal. I personally faced similar case when visiting SEPHORA's Asian headquarters in Singapore. Let's use an analogy: How many database developers can accurately describe the color of lipstick?  Give me the name of *Le Rogue No.1 by YSL* [^B1], I cannot pick it up from the shelf. How many cosmetics experts can verify the result of a query output? If not, how can him/her trust business decisions on a generated SQL? 

Both shade of lipstick and SQL query are **domain knowledge**, usually processed by different individuals.  



NLP2SQL only provides the 1st leg of the task.[^B5] The end-user still need to interpret the result of a generated SQL. Here is where AI-for-DB comes in to parse the results and generate reports that users can understand and validate its truthfulness. Hence, AIGC completes the loop.
[Duet AI in Google Cloud - data analysis and visualization](https://www.youtube.com/watch?v=gtehwj1G4tU) demonstrated in Google Next'23  with *NLP+BigQuery+Looker*. With natural language as input, and presentation slides as output,  the complexity of SQL and data warehouse is transparent to end-user. Now, they can understand the output results with their domain knowledge, where their professional experience and daily intuitive judgment kick in.

 "Render unto Caesar the things that are Caesar's, and unto God the things that are God's"; SQL to the database coders, lipstick shades to cosmetics professionals. **Everyone has their role, shining where their expertise lies.**

* Prototype architecture：NPL2SQL + Data Warehouse + Marp[^B7]


[^B1]: *The 50 Most Classic Lipstick Colors of All Time*, https://www.thecut.com/article/lipstick-colors.html
[^B5]: NLP2SQL only completes 10% of the task.
[^B7]: a Markdown to PPT tool. Myself used it in the past 10 months for homework presentations. 



#### 2. Database migration: the last part of an endeavor is the hardest to finish（行百里者半九十）

Database migration is a forever topic for decades, and issues of  compatibility, data migration, schema conversion, and application rewriting have even become tiresome in so many discussion. Yet, it still takes up 40% of CIO/CTO's budget. The cumbersome tasks have been improved with database kernel compatibility[^C1] or innovations in conversion tools[^C2] which pushing the threshold to 95%. My analysis for a client's business in a Kuala Lumpur conference room four years ago reached the number. It was a case of helping a Malaysian e-commerce company migrate from Oracle RAC to PolarDB, and our final challenge was in that 5%. The calculation can be found here [“Goodbye Oracle! Exclusive Insights into PrestoMall’s Transition to Alibaba Cloud”](https://alibaba-cloud.medium.com/goodbye-oracle-exclusive-insights-into-prestomalls-transition-to-alibaba-cloud-d24b05058777). Both the CTO and I knew the up-hill battle of the last 5%. Together we succeeded, with a few good tools and many man-months power。Hopefully, **This 5% is where AIGC can bring innovation**。

*Duet AI*, as a supplementary tool for database developers, can push forward another 2-3%. Not only can it compare and transform the legacy C++[^C3] into the trendy GO, but it can also convert the source database APIs into the target ones, the GCP's own cloud database *AlloyDB*. Although *Duet AI* won't bring revolution, its innovations are solid building-blocks to follow.

An interesting piece: [Duet AI in Google Cloud - database management](https://www.youtube.com/watch?v=u6489QehgdQ) demonstrates an application migration from *Oracle* to *AlloyDB*. It detects `localtimestamp()`, changes `clock_timestamp()`, and recommends the global changes. This small move could **reduces half a day's work to just 30 minutes**.


This "minor" improvement is not exclusive to database migration, but offers the best cost/return ratio.  Because database application migration often occurred years after the application was implemented. On one hand, the developers in charge of migration neither have the interest nor the capability to understand the original program; on another hand, the original applications undoubtedly contain many repetitive code snippet accumulated over the years. Utilizing machine learning to extrapolate from one code segment to many would be the best friend of a programmer.

* Prototype architecture：existing data replication and schema conversation tool + drivers for cloud databases + GitHub co-pilot[^C5]



[^C1]: EnterpriseDB/EDB, PolarDB for Oracle，Oceanbase for Oracle. 
[^C2]: AWS Schema Conversion Tool
[^C3]: how about COBOL on mainframe? 
[^C5]: co-pilot is the key

#### 3. DBA facing tons of system warnings

I was once sitting in a bar with a Sr. Cloud Database lead, while he was on a 24-hour-duty cycle. Throughout the two hours conversation, his phone was constantly vibrating. He also had to occasionally glance at the alerts, interrupting our enthusiastic gossip now and then to check the detailed information. And **ignore most of them**.

Why did the guy receive thousands of so-called alerts? 

Cloud clients  "outsources" their IT services to cloud providers. The technical staffs of the cloud providers, due to lack of understand the client's business, have limited options to triage and assess the alerts. For years (partly to avoid liability), the number of alerts has only increased, commonly one alert for a particular client be implemented generally to hundreds customers. This practice results in **99.x% of the alerts being useless**. This consumes a significant amount of human resources and severely pollutes the system with alerts. **The so-called completeness has severely compromised efficiency**. 



Google shows [Duet AI in Google Cloud - troubleshooting issues](https://www.youtube.com/watch?v=MBAuTQdtZ0o). The idea wasn't anything new. For example, *Snowflake*'s early success contributed from service with scalability . Snowflake's operations generate tens of terabytes of log data daily. The reason they could leap over the startup threshold of increasing service without adding engineers was due to effectively implementing the automation of log analysis.  

Previously, database systems heavily relied on the forward-thinking design of SQL Error Messages, such as the 786 pages of [MySQL 8.0 Error Message Reference](https://downloads.mysql.com/docs/mysql-errors-8.0-en.a4.pdf), a 30-years accumulation. Now, LLM models can  summarize system errors, and easily analyze the system's status for the hours before a major situation, especially the alerts that were overlooked by human at the time, a typical case that new technology applied to existing scenarios."



* Prototype architecture：TSDB/DW + LLM on database logs + feedback mechanism




####  Random words at the end

"AI for DB" and "DB for AI" all have their merits.  Database kernel has been matured with years' handcraft by elite engineers,  current general AI technology won't bring in eye-opening improvements（ academic researchs could be ). 

While the AI impact on DB kernel remains to be seen, DMaaS related to daily IT work can take the lead, utilizing today's AI technology to create revolutionary products. **The above three directions with prototype clear architecture paths can be pursued immediately.**


The above ideas were formed at Bodega Bay while watching pacific harbor seals swimming near the cliff.

![](./images/BodegaBay.jpeg)



