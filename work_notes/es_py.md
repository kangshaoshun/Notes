# ElasticSearch_python

## 基础概念
*Elasticsearch 是一个实时的分布式搜索分布引擎，它能让你以一个前所未有的速度和规模去探索你的数据，它被有做全文搜索，结构化搜索，分析以及这三个功能的组合*
Elasticsearch 鼓励你去探索与利用数据，而不是因为查询数据太困难，就让它们烂在数据仓库里面。

Elasticsearch可以这样准确的描述
+ 一个分布式的试试文档存储，每个字段可以被索引与搜索
+ 一个分布式实时分析搜索引擎
+ 能胜任上百个服务节点的扩展，并支持PB级别的结构化或者非结构化数据

## 增删改查 
es支持多种客户端，这里介绍熟悉的python客户端操作es.以下仅仅是常用api摘要，详细api参考[es_python](http://elasticsearch-py.readthedocs.io/en/master/index.html)

+ 增

		增加，一般称之为入库操作，使用的命令语句为：
		es.index(index="abcd", doc_type='efg', id=1, body=doc)

+ 删

		删除，有多种删除api,常用的是按照id删除，其他的可以参考详细链接（见上文）
		es.delete(index = "abcd", doc_type="efg", id = '123')
		注：通常删除之后不会立即生效，需要强制刷新es库：
			es.indices.refresh(index="abcd")
+ 改

		修改在es中其实是个假命题，实际中的修改是直接使用id相同的数据覆盖源数据即可
		操作和入库是一样的，将源数据拉取下来，修改相应字段，然后以同id入库，这样原库中的数据就会被覆盖，达到修改的效果
+ 查 

		查询在es中最为常用，也最为复杂：
		通过id获取单条数据:
			es.get(index=__index, doc_type=__doc_type, id='1234')
		通过复杂条件查询数据：
			res = es.search(index=__index, doc_type=__doc_type , body=query_dict)
			#query_dict 通过DSL查询，可以组合成很复杂的查询，下面详细介绍

## DSL查询语句

		



