# testapi

## 介绍
让接口测试起来更简单、人性化、更好玩  
公众号：小白科技之窗

### 接口测试需要接口的痛点：
- 接口文档的导入：swagger、har、curl
- 接口信息头：支持长字符串
- 接口断言：支持jsonpath与正则断言
- 接口数据：支持jsonpath提取数据

## 软件架构
    python3.* + requests + jmespath + pytest + pytest-HTML

## 安装教程
- 更新下载源
    `pip config set global.index-url https://pypi.douban.com/simple`
    
- 安装testapi
    `pip install -U testapi`

## 使用说明

```
from xiaobaiapi.xiaobaiapi import RequestClient


# 断言的案例
RequestClient(method='GET', url='http://127.0.0.1:8000', assertExpression='code', assertValue=200)

# 提取器的案例，提取的值存储在r.variable对象中
r = RequestClient(method='GET', url='http://127.0.0.1:8000/api/gettoken', extractorExpression='data.token', extractorVariable='token')
print(r.variable)

```


## 日志
| 版本 | 信息 |
| --- | --- |
| 0.1 | 完成单个接口断言及提取器 |
