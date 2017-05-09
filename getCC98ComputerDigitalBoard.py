import requests
import leancloud
import time

url = "https://api.cc98.org/Topic/Board/562"
appId = "Your LeanCloud Application appId"
masterKey = "Your LeanCloud Application masterKey"
SCKEY = "Your ftpp server tyan SCKEY"

interval = 3

leancloud.init(appId, masterKey)
DigitalBoard = leancloud.Object.extend('DigitalBoard')

def pushMsg(text, desp=""):
	url = "http://sc.ftqq.com/" + SCKEY + ".send"
	condition = {'text': text, "desp": desp}
	res = requests.get(url, params=condition)
	return(res)

def getData(condition):
	try:
		res_str = requests.get(url, params=condition)
	except Exception as e:
		print(e)
		pass
	else:
		return res_str.json()

def insertLC(i):
	try:
		digitalBoard = DigitalBoard()
		digitalBoard.set('title', i['title'])
		digitalBoard.set('hitCount', str(i['hitCount']))
		digitalBoard.set('id', str(i['id']))
		digitalBoard.set('boardId', str(i['boardId']))
		digitalBoard.set('bestState', str(i['bestState']))
		digitalBoard.set('topState', str(i['topState']))
		digitalBoard.set('replyCount', str(i['replyCount']))
		digitalBoard.set('isVote', str(i['isVote']))
		digitalBoard.set('isAnonymous', str(i['isAnonymous']))
		digitalBoard.set('authorName', i['authorName'])
		digitalBoard.set('authorId', str(i['authorId']))
		digitalBoard.set('isLocked', str(i['isLocked']))
		digitalBoard.set('createTime', i['createTime'])
		digitalBoard.set('lastPostInfo', i['lastPostInfo'])
		digitalBoard.save()
	except Exception as e:
		print(e)
		pass
	else:
		print("insert successful: ", i['title'])

def crawler():
	condition = {'from': 0, 'to': 9}
	flag = True

	while flag:

		print("正在爬取 第", condition['from'],"个到篇", condition['to'], "篇 的帖子...")
		time.sleep(1)
		res = getData(condition)
		
		#处理断网或CC98 API失去响应的异常
		while not res:
			print("请求CC98 API失败，请等待5s后重试...")
			time.sleep(5)
			print("再次请求CC98 API...")
			time.sleep(0.5)

		for i in res:
			try:
				query = DigitalBoard.query
				query_count = query.equal_to('id', str(i['id'])).count()
				
				#Keyword
				if (query_count == 0):
					if ('iPad' in i['title']):
						print("\nThere's an iPad!!!\n" )
						pushMsg("new iPad!!!", i['title'])
					elif ('手环' in i['title']):
						print("\nThere's an 手环!!!\n" )
						pushMsg("new Band!!!", i['title'])
					insertLC(i)
				else:
					flag = False
					print("inserted ", i['title'])
					
			except Exception as e:
				print(e)
				pass

		#翻页
		tmp = condition['to']
		condition['from'] = condition['to'] + 1
		condition['to'] = tmp + 10


#主程序
if __name__ == "__main__":
	time.sleep(0.5)
	print("CC98 爬虫启动中...")
	time.sleep(0.5)
	print("CC98 爬虫已启动...")
	time.sleep(0.5)
	print("本爬虫以 十分钟/次 的频率爬取电脑数码版上的新帖子...\n")

	time.sleep(1)
	while True:
		crawler()
		print("\n", str(interval)+"s后开始下一轮爬虫...")
		time.sleep(interval)
		print("\n 新一轮爬虫开始...")
		time.sleep(1)



		