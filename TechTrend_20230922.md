# 数据库15分钟准则 ｜ MySQL 5.7 十月底 停服 ｜ 腾讯云推出向量数据库  
## 重要更新
### MySQL 5.7 EOL 倒计时
MySQL，全球最受欢迎的开源数据库，将在2023年10月底达到生命周期终点，这意味着其将不再更新或获得安全补丁。[参考](https://www.infoworld.com/article/3699117/update-or-migrate-planning-for-mysql-5-7-eol.html)

* 目前有超过一半的MySQL服务器正在运行5.7版本，这些服务器需要为此做好准备。
* 建议迁移：
	*  MySQL 8.0或更高
	* 迁移至其他兼容MySQL的云原生数据库，比如阿里的PolarDB, AWS的Azure
* 决策应基于对现有应用、升级或迁移的工作量估计、未来基础设施需求和成本效益分析的评估。 迁移工具：可以考虑采用云产商本身策略，或者[NineData的数据库工具](ninedata.cloud)

### 中国数据库走向国际的门槛： 15分钟准则

《云数据库技术》提出**数据库15分钟准则**。[参考](https://mp.weixin.qq.com/s/NlwtxtX8AOilsP5x0qRKYA)

作者根据其负责某顶级云厂商的数据库海外业务的经历，分享了他对于"15分钟测试"（TTHW: Time to hello world）的理解。如果无法通过“15分钟法则”，就意味着高昂的现场服务成本。从中国成长起来的TiDB和TDengine都成功地满足了这个测试。


解决方案分三类：

* Playground(例如Airbyte， TiDB)，
* 预生产（Serverless Instance/Cluster - Bigquery, Snowflake, GCP-RDS). 比如NineData为用户提供了 2 个免费的 MySQL 测试数据源[demo_datasource](https://docs.ninedata.cloud/quick_start/demo_datasource)，便是采用“预生产”手段，这样用户在账号建立后，就可以立刻体验SQL 开发，数据复制，备份等功能。
* IaC (AWS CloudFormation, HashiCorp's Terraform) 




## 云数据库更新详情 

### 阿里云

DTS:重新支持MySQL到ClickHouse的同步功能。[参考](https://help.aliyun.com/zh/dts/user-guide/synchronize-from-rds-mysql-to-clickhouse-cluster?spm=a2c4g.11186623.0.i2)

Redis：

* Tair（Redis企业版）持久内存型实例支持审计日志功能。[参考](https://help.aliyun.com/zh/redis/product-overview/release-notes?spm=a2c4g.11186623.0.0.49b951193lWMOm)
* 升级了性能监控中的CPU使用率指标。[参考](https://help.aliyun.com/zh/redis/product-overview/notice-on-the-upgrade-of-the-cpu-utilization-metric-in-performance-monitoring?spm=a2c4g.11186623.0.0.681d3e00i8YB39)

RDS MySQL：推出经济版集群系列规格[参考](https://help.aliyun.com/zh/rds/product-overview/cluster-edition-for-apsaradb-rds-for-mysql-supports-cost-effective-instance-types-from-20230912?spm=a2c4g.11186623.0.0.46061e504XX32t)

云数据库Memcache版:停止支持公网连接[参考](https://help.aliyun.com/document_detail/2543814.html?spm=a2c4g.2551263.0.0.262a4df0n7r4yh)




### 腾讯云

SQL Server:

* 腾讯云可观测平台实例监控页接入云数据库 SQL Server。
* 修改实例所属项目时，不会解绑安全组。[参考](https://cloud.tencent.com/document/product/238/43219)
* 手动备份增加保留时长策略选择，支持选择跟随自动备份保留时间的策略或跟随实例生命周期。[参考](https://cloud.tencent.com/document/product/238/70156)

向量数据库：

* 向量数据库目前处于公测阶段，支持多种索引类型和相似度计算方法，百万级 QPS 及毫秒级查询延迟。[参考](https://cloud.tencent.com/document/product/1709/94945)
* 新增 Embedding 功能。[参考](https://cloud.tencent.com/document/product/1709/98014)
* 新增 IVF 系列向量索引。[参考](https://cloud.tencent.com/document/product/1709/95428)
* 支持清空集合数据。[参考](https://cloud.tencent.com/document/product/1709/98684)
* 支持集合别名机制。[参考](https://cloud.tencent.com/document/product/1709/98686)
* 支持更新数据。[参考](https://cloud.tencent.com/document/product/1709/98667)
* 支持重建索引。[参考](https://cloud.tencent.com/document/product/1709/98690)
* Filter 能力增强。查询、更新、删除数据均支持 Filter 表达式过滤数据。[参考](https://cloud.tencent.com/document/product/1709/95477)

### 火山云
MongoDB数据库：

* 支持批量变更 Shard 分片。[参考](https://www.volcengine.com/docs/6447/72267)
* 控制台顶部导航栏增加项目资源筛选。[参考](https://www.volcengine.com/docs/6293/71107)
* 支持公网解析。[参考](https://www.volcengine.com/docs/6447/1108497)
* 支持回档库表数据。[参考](https://www.volcengine.com/docs/6447/1122036)

### AWS

RDS:

* 亚马逊RDS for Oracle现已在新区域支持M6i，R6i和R5b实例。[参考](https://aws.amazon.com/about-aws/whats-new/2023/09/amazon-rds-oracle-m6i-r6i-r5b-instances-new-regions/)
* 亚马逊CloudWatch为RDS性能洞察添加了新的Metric Math.[参考](https://aws.amazon.com/about-aws/whats-new/2023/09/amazon-cloudwatch-metric-math-rds-insights/)
* 亚马逊RDS现已支持SQL Server的X2iedn实例。[参考](https://aws.amazon.com/about-aws/whats-new/2023/09/amazon-rds-x2iedn-instances-sql-server/)
* 亚马逊RDS Performance Insights现已支持亚马逊RDS for SQL Server的SQL级别指标[参考](https://aws.amazon.com/about-aws/whats-new/2023/09/amazon-rds-performance-insights-sql-metrics-rds-server/)
* PostgreSQL 16.0 现已在亚马逊 RDS 数据库预览环境中可用。
[参考](https://aws.amazon.com/about-aws/whats-new/2023/09/postgresql-16-rds-database-preview-environment/)

### GCP

BigQuery:

* 已增加Connected Sheets返回结果的最大行数。[参考](https://cloud.google.com/release-notes#September_20_2023)

中东 me-central2（达曼）区域，新增： Cloud Bigtable；Cloud SQL for MySQL， PostgreSQL, SQL Server; Cloud Spanner. [参考](https://cloud.google.com/release-notes#September_19_2023)

AlloyDB for PostgreSQL:

* 对高可用主实例进行的维护操作现在大多数工作负载的停机时间少于一秒钟。[参考](https://cloud.google.com/alloydb/docs/overview#maintenance)
* AlloyDB for PostgreSQL 现已在以下地区提供：europe-west12 (都灵)； me-central1 (多哈)。[参考](https://cloud.google.com/alloydb/docs/locations)