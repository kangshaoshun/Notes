#coding:utf-8
import sys
import ujson as json
reload(sys)
sys.setdefaultencoding('utf-8')


d = {"kang":"shao", "shao":"shun", "meng":"ling", "peidian":[{"dian":"康绍舜"}]}

print json.dumps(d, indent=3, ensure_ascii=False)

