# CC98电脑数码版爬虫—商品关键字通知

### 简介

相信大家都有这种经历，想从CC98电脑数码版收个二手电子产品，担心错过新商品一遍遍刷新网页。本爬虫运行在校园网络下的个人电脑或者树莓派（推荐）上，帮助用户自动检测新商品并根据关键词触发微信通知。

### CC98 API

CC98 向用户开放API，极大地方便了该程序的开发。

[CC98 API](https://api.cc98.org)

[GET-Topic-Board-boardId](https://api.cc98.org/Help/Api/GET-Topic-Board-boardId)

### 第三方存储LeanCloud

30000次/天的免费请求限额把萌新喂得饱饱的。

[LeanCloud](https://leancloud.cn)

[LeanCloud Python SDK 安装指南](https://leancloud.cn/docs/sdk_setup-python.html)

[LeanCloud Python 数据开发指南](https://leancloud.cn/docs/leanstorage_guide-python.html)

### 潜在异常处理

1. 突然断网
2. CC98 API 失去响应
	
	五秒后再次尝试
3. LeanCloud 存储失败

	下一轮爬虫继续尝试

### 微信实时提醒

基于 `方糖泡泡 Server酱` 的服务

[方糖泡泡 Server酱](http://sc.ftqq.com/3.version)

### Github

[getCC98ComputerDigitalBoard](https://github.com/vinci7/getCC98ComputerDigitalBoard)

