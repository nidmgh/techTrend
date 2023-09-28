# 阿里云PolarDB-X 2.0 备份恢复服务商业化 | 云厂商应对MySQL5.7 EOL，微软支持至2025

## 重要更新
### 拿到广告单的正确方式: 如何发布和获得产品更新？
文章讨论了获取云服务商数据库产品发布信息的问题。作者通过一个实习生收集阿里、华为、腾讯、火山，以及AWS, GCP, Azure等公司的数据库相关release note，并尝试从全手工到部分自动化的工作经历，对国内外云厂商产品更新信息发布方式进行了讨论与对比，并总结出了三点国际云厂商在产品更新信息发布上做的更好的地方：

* **支持RSS**订阅，且相关技术文档、更新动态可以被搜索引擎，爬虫检索到；
* **信息发布具体而微**，小的修复也可以在技术文档的更新动态中看到；
* **信息分类做得完善**，如亚马逊可以直接查看“数据库”这一大类别下所有具体产品的更新动态；微软在此基础上还可以根据新功能不同的发布状态再次进行筛选。
[参考](https://mp.weixin.qq.com/s/d4VXFxCeOyoxj48HxvdJbQ)

### MySQL 5.7 EOL 倒计时  
* 谷歌指出 Cloud SQL 打算结束对特定主要版本的支持时，其将至少提前 12 个月发送弃用通知以提醒项目所有者。此外，Cloud SQL 还将根据需要提供一些工具，以最大程度地减少升级中断。值得注意的是，为期 12 个月的期限结束时，任何未迁移到新的主要版本的实例都将自动升级。[参考](https://cloud.google.com/sql/docs/mysql/db-versions?hl=zh-cn)
* 亚马逊宣布其RDS标准对MySQL5.7的支持预计会在2023年12月终止，比社区生命周期终止日期要晚两个月。[参考](https://docs.aws.amazon.com/zh_cn/AmazonRDS/latest/UserGuide/MySQL.Concepts.VersionMgmt.html)
* 微软宣布对于使用MySQL的Azure数据库其支持将会延长至2025年9月，并给出了详细的停用时间线。[参考](https://learn.microsoft.com/en-us/azure/mysql/concepts-version-policy)

## 云数据库更新详情
### 阿里云 
PolarDB:

* 2023年10月27日起PolarDB-X 2.0备份恢复启动商业化[参考](https://help.aliyun.com/zh/polardb/polardb-for-xscale/backup-and-recovery-commercialized?spm=a2c4g.11186623.0.0.7d252782jHpFKL)
* PolarDB-X实例小版本16952556发布，新增和优化了部分功能，并修复了部分缺陷。[参考](https://help.aliyun.com/zh/polardb/polardb-for-xscale/release-notes?spm=a2c4g.11186623.0.0.61dd44502nUpT3)
* PolarDB-X存储节点xcluster-20230919版本发布，修复了一些问题。[参考](https://help.aliyun.com/zh/polardb/polardb-for-xscale/release-notes-for-the-polardb-x-storage-engine?spm=a2c4g.11186623.0.0.7e4e3e87VKG6X1)
* PolarDB-X日志节点polarx-cdc-kernel-2.3.0_4755313版本发布，优化了部分功能并修复了一些问题。[参考](https://help.aliyun.com/zh/polardb/polardb-for-xscale/release-notes-for-the-polardb-x-cdc-nodes?spm=a2c4g.11186623.0.0.2a426e1cvx28zz)

RDS：自2023年10月10日起，RDS将停止售卖RDS PostgreSQL 10版本实例，仅提供产品服务技术支持[参考](https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/end-of-sales-of-instances-running-postgresql-10-on-20231010?spm=a2c4g.11186623.0.0.30c36850dQTQQc)

DAS：对于集群和读写分离架构的实例，支持分别查看数据节点和代理节点的统计信息。（Redis引擎）[参考](https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/end-of-sales-of-instances-running-postgresql-10-on-20231010?spm=a2c4g.11186623.0.0.30c36850dQTQQc)

### 腾讯云 

DTS：

* 支持用户自行设置维护时间窗口，系统在设置的时间窗口内进行任务升级。[参考](https://cloud.tencent.com/document/product/571/93505)
* 任务失败状态持续14天后，系统将自动将任务状态扭转为结束。[参考](https://cloud.tencent.com/document/product/571/93504)
* 新增 TDSQL-C MySQL 到 MariaDB 数据同步链路。[参考](https://cloud.tencent.com/document/product/571/56152#9e472e11-e922-4d9b-a7da-31d5d99c4d79)
* MySQL 系列一致性校验功能优化，校验任务报错时提示错误详情。[参考](https://cloud.tencent.com/document/product/571/56152#9e472e11-e922-4d9b-a7da-31d5d99c4d79)

TDSQL-C MySQL：

* 数据库审计优化。[参考](https://cloud.tencent.com/document/product/1003/51268)

* 支持跨地域备份功能，实现数据库恢复的高可用性，满足数据可用性及安全性、异地备份恢复、异地容灾、长期归档数据、监管等功能。[参考](https://cloud.tencent.com/document/product/1003/98827)

MySQL:

* 数据库审计优化。[参考](https://cloud.tencent.com/document/product/236/41064)

### 火山云 
veDB MySQL：

* veDB MySQL 采用基于活跃请求数负载均衡策略，来保证多个只读节点之间的负载均衡。可以有效地提高只读节点利用率，提升整体性能。[参考](https://www.volcengine.com/docs/6357/1144266)
* veDB MySQL 支持事务拆分功能，能够将事务内第一个写请求之前的读请求发送到只读节点，降低主节点压力。[参考](https://www.volcengine.com/docs/6357/1144274)
* veDB MySQL 提供最终一致性、会话一致性、全局一致性三种一致性级别，来保证不同场景下业务对数据的一致性要求。[参考](https://www.volcengine.com/docs/6357/1144276)

缓存数据库Redis版:

* 支持将指定从节点切换为主节点，满足容灾演练或多可用区场景下就近连接的需求。[参考](https://www.volcengine.com/docs/6293/77778)
* 缓存数据库 Redis 版新增事件中心功能，支持通过计划内事件对指定实例所在的机器进行软硬件或网络升级，来保障数据库云服务的稳定性和可持续性。[参考](https://www.volcengine.com/docs/6293/1148725)
* 您可以根据业务需要将一个或多个参数配置放置在一个参数模板中，并将这些配置批量应用到相同数据库版本的实例中，提升参数管理和实例配置的效率。[参考](https://www.volcengine.com/docs/6293/1125903)
* 在 Redis 控制台上查看已修改参数的修改记录，包括已修改参数的名称、修改前后的参数值、参数修改状态、修改时间等。[参考](https://www.volcengine.com/docs/6293/1131863)

### AWS

RDS：

* Amazon RDS Custom for SQL Server现在支持更改服务器级别的排序规则。[参考](https://aws.amazon.com/about-aws/whats-new/2023/09/amazon-rds-custom-sql-server-changing-server-level-collation/)

Redshift：

* Amazon Redshift已在工作负载管理（WLM）中支持基于角色的访问控制[参考](https://aws.amazon.com/about-aws/whats-new/2023/09/amazon-redshift-role-based-access-control-wlm/)

DynamoDB：

* 新增DynamoDB对S3的增量导出功能 [参考](https://aws.amazon.com/about-aws/whats-new/2023/09/incremental-export-s3-amazon-dynamodb/)
* EventBridge Pipes现已在三个额外地区提供 [参考](https://aws.amazon.com/about-aws/whats-new/2023/09/amazon-eventbridge-pipes-new-additional-regions/)
* NoSQL Workbench现已支持生成人类可读的样本数据 [参考](https://aws.amazon.com/about-aws/whats-new/2023/09/human-readable-sample-data-nosql-workbench/)

DocumentDB：

* DocumentDB（兼容MongoDB）现已在香港地区提供[参考](https://aws.amazon.com/about-aws/whats-new/2023/09/amazon-documentdb-mongodb-hong-kong/)
* DocumentDB（兼容MongoDB）现在支持JSON模式验证[参考](https://aws.amazon.com/about-aws/whats-new/2023/09/amazon-documentdb-mongodb-json-schema-validation/)
* DocumentDB（兼容MongoDB）支持原地主版本升级 [参考](https://aws.amazon.com/about-aws/whats-new/2023/09/amazon-documentdb-mongodb-in-place-version-upgrade/)
 
### Azure
Azure SQL：

* 预览：Azure SQL数据库免费试用 [参考](https://azure.microsoft.com/en-us/updates/public-preview-azure-sql-database-free-offer/)
* SQL Managed Instance Business Critical的最大日志速率现已翻倍。[参考](https://techcommunity.microsoft.com/t5/azure-sql-blog/your-max-log-rate-on-sql-managed-instance-business-critical-is/ba-p/3899817)
* 现支持Amazon S3恢复备份到Azure SQL Managed Instance。
[参考](https://aka.ms/mi-s3-restore)

Azure Cosmos DB：

* 正式发布：Azure Synapse Link for Azure Cosmos DB现支持自定义分区 [参考](https://azure.microsoft.com/en-us/updates/generally-available-custom-partitioning-in-azure-synapse-link-for-azure-cosmos-db/)

MySQL：

* Preview：对 Azure Database for MySQL提供了用户可定制的灵活维护窗口[参考](https://azure.microsoft.com/en-us/updates/public-preview-azure-database-for-mysql-flexible-maintenance/)
* Azure Database for MariaDB将于2025年9月19日将停用，将迁移到Azure Database for MySQL Flexible Server[参考](https://azure.microsoft.com/en-us/updates/azure-database-for-mariadb-will-be-retired-on-19-september-2025-migrate-to-azure-database-for-mysql-flexible-server/)


Cache for Redis：

* 预览：Azure Cache for Redis Enterprise支持更多缓存大小的选项：E5, E200, 和 E400 SKUs. [参考](https://azure.microsoft.com/en-us/updates/public-preview-additional-cache-sizes-for-azure-cache-for-redis-enterprise/)

MariaDB：

* 2025年9月19日将停用Azure Database for MariaDB - 将迁移到Azure Database for MySQL Flexible Server [参考](https://azure.microsoft.com/en-us/updates/azure-database-for-mariadb-will-be-retired-on-19-september-2025-migrate-to-azure-database-for-mysql-flexible-server/)

### GCP

Cloud SQL：

* Cloud SQL高可用性推荐器会主动生成建议，通过提供数据冗余来帮助用户将重要实例纳入SLA。在区域停机或实例内存耗尽时，这可能会有所帮助。[参考](https://cloud.google.com/release-notes#September_26_2023)
* 所有Cloud SQL for MySQL Enterprise Plus版实例现在支持保留最多35天的事务日志以进行点时间恢复 [[参考]](https://cloud.google.com/sql/docs/mysql/backup-recovery/pitr)
* 以下版本更新目前正在进行中：MySQL 5.7.42已升级为MySQL 5.7.43。
2023年9月25日 [[参考]](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-43.html)
* 现已提供1.2版本的扩展。此扩展为访问Oracle数据库提供了一个外部数据包装器，使其更加容易和高效。欲了解更多信息，请查看配置PostgreSQL扩展。[[参考]](https://cloud.google.com/sql/docs/postgres/extensions)

BigQuery:

* BigLake元数据缓存启用表上的物化视图可以结构化云存储中的数据。这些物化视图功能类似于BigQuery管理存储表上的物化视图，包括自动刷新和智能调优的优点。此功能现已普遍可用（GA）。[[参考]](https://cloud.google.com/bigquery/docs/materialized-views-intro#biglake)
* 授权存储过程现在已经普遍可用（GA）。此功能可以与用户或组共享存储过程，而无需直接访问底层表格。[[参考]](https://cloud.google.com/release-notes#September_25_2023)
* BigQuery数据传输服务现已停止对Google AdWords的支持。 [[参考]](https://cloud.google.com/bigquery/docs/google-ads-transfer)

AlloyDB for PostgreSQL:

* AlloyDB现在提供基础实例，这些是只包含一个节点、位于一个区域的主实例。基础实例为高可用性实例提供了更低成本的替代方案，并适合在不需要高可用性的非生产环境中使用。 [[参考]](https://cloud.google.com/alloydb/docs/basic-instance)
* 数据库服务器与PostgreSQL版本15的兼容性目前处于预览状态。您可以创建具有PostgreSQL 15兼容性的集群。 [[参考]](https://cloud.google.com/alloydb/docs/cluster-create#preview-15)