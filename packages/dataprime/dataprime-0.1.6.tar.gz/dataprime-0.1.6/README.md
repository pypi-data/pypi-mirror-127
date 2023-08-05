## 
# 数据智脑计算引擎dataprime


dataprime是一款数据计算引擎，提供了数据钻取、过滤、生成、采样、聚合、排序等功能，输入dataframe对象，调用不同方法，即可返回相应的结果
​

## 一 快速开始

- 安装

`pip install dataprime`

- 使用
```python
import json

from dataprime_celery import DataPrime
import pandas as pd

# 准备数据
data = [
        {"name": "test1", "time": "2021-01-05", "score": 10},
        {"name": "test2", "time": "2021-01-12", "score": 20},
        {"name": "test3", "time": "2021-01-24", "score": 30}
]

# 过滤参数
filter_list = [
    {
        "column": "score",
        "dtype": "int",
        "filter": {
            "condition": "greater_than",
            "value": "10",
            "max": 0,
            "min": 0
        }
    }
]

data_frame = pd.read_json(json.dumps(data))

# 初始化一个DataPrime对象
dp = DataPrime(dataframe=data_frame)

# 调用方法进行处理, 返回一个dataframe对象
result = dp.filter(filter_list).dataframe

print(result)
```
​

## 二 使用文档
### 1.钻取 Drill
钻取是以一个时间字段为维度，将数据按年、月、日进行细分
​


- 参数字段

`drill_granularity_list` 钻取粒度列表，包含年、月、日
`drill_node_list` 钻取节点列表
`dimensions` 钻取字段
​


- 参数示例:
```python
drill_granularity_list = [
    {
        "value": "YEAR",
        "label": "年"
    },
    {
        "value": "MONTH",
        "label": "月"
    },
    {
        "value": "DAY",
        "label": "日"
    }
]

drill_node_list = [
    {
        "granularity": "",
        "point": "YEAR",
    },
    {
        "granularity": "YEAR",
        "point": "2021",
    },
    {
        "granularity": "MONTH",
        "point": "01",
    }
]

dimensions = [
    {
        "column": "time",
        "dtype": "datetime",
    }
]
```


- 使用示例
```python
result = dp.drill(drill_granularity_list, drill_node_list, dimensions).dataframe
```


### 2.过滤 Filter
过滤是根据某一个度量字段，通过一定条件来筛选需要的数据


- 参数示例
```python
filter_list = [
    {
        "column": "score",             # 过滤字段
        "dtype": "int",                # 字段类型
        "filter": {
            "condition": "less_than",  # 过滤条件
            "value": "100",            # 过滤值
            "max": 50,                 # 最大值, 区间判断时用到
            "min": 0                   # 最小值, 区间判断时用到
        }
    }
]
```


- 使用示例
```python
result = dp.filter(filter_list).dataframe
```


- condition选项

| **条件** | **值** |
| --- | --- |
| 等于 | equal |
| 不等于 | not_equal |
| 区间内 | in_between |
| 区间外 | out_between |
| 大于 | greater_than |
| 大于等于 | equal_greater_than |
| 小于 | less_than |
| 小于等于 | equal_less_than |
| 包含 | contains |
| 不包含 | not_contains |



### 3.生成器 Generator
生成器是在dataframe中新增一列，提供求和、求平均值、计算行等结果，例如有a、b两列，可以通过生成器生成"a-b-平均值"列
​


- 参数示例
```python
generated_metric_list = [
    {
        "dtype": "float",
        "operate": {
            "label": "均值",
            "value": "Avg"          # 生成类型
        },
        "source_col_list": [        # 源数据列
            {
                "column": "age",
                "dtype": "int"
            },
            {
                "column": "score",
                "dtype": "int"
            }
        ],
        "column": "age-score-均值"  # 生成列名称
    }
]
```

- 使用示例
```python
result = dp.generate(generated_metric_list).dataframe
```

- 生成类型

| **生成类型** | **值value** |
| --- | --- |
| 平均值 | Avg |
| 求和 | Sum |
| 计算行 | COUNT_COL |



### 4.采样 Sampling
采样是指通过`等距采样`、`随机采样`等方式，对数据进行采样，获取一定数量的行
​


- 参数示例
```python
sample = {
    "number": 5,      # 采样数量
    "type": "random"  # 采样方式, 随机:random  等距:equidistant
}
```

- 使用示例
```python
result = dp.sample(5, "random").dataframe
```


### 5.聚合 Aggregate
聚合是对数值(度量)列进行聚合，可以进行计数、求和、求平均值等聚合操作
​


- 参数示例
```python
aggregation_list = [
    {
        "column": "age",          # 源数据列
        "dtype": "int",
        "aggregation_option": {
            "label": "均值",
            "value": "mean"       # 聚合方法
        }
    },
    {
        "column": "score",
        "dtype": "int",
        "aggregation_option": {
            "label": "均值",
            "value": "mean"
        }
    }
]
```

- 可用的聚合方法

['count', 'sum', 'mean', 'median', 'std', 'var', 'max', 'min']
​


- 使用示例
```python
result = dp.aggregate(aggregation_list).dataframe
```


### 6.排序 Sorting
排序是根据某一个数据列进行升降排序
​


- 参数示例
```python
sort = {
	"condition": "desc",  # 升序:desc  降序:asc
    "column": "time"      # 排序字段
}
```

- 使用示例
```python
result = dp.order_by("time", "desc").dataframe
```


### 7.top N
top N是指按照某一列的值进行排序，取出前几行
​


- 参数示例
```python
top_n_param = {
    "column": "score",     # 排序字段
    "condition": "desc",   # 排序方式， 升序:desc  降序:asc
    "limit": 3             # 取出数量
}
```


- 使用示例
```python
result = dp.top_n("score", "desc", 3).dataframe
```
### 
### 8.统一入口
除了上述的单个方法外，也可以使用`dataprime.process_df_operator()`来同时进行多个数据处理操作,参数字段与上面相同
​


- 使用示例
```python
dataprime = DataPrime(
    dataframe=data_frame,
    **{
        "dimensions": dimension_list,
        "metrics": metric_list,
        "calculation_flow_nodes": calculation_flow_nodes,
        "generated_metric_list": generated_metric_list,
        "filter_list": filter_list,
        "aggregation_list": aggregation_list,
        "sample": sample,
        "drill_granularity_list": drill_granularity_list,
        "drill_node_list": drill_node_list,
        "sort": sort_param,
        "topn": top_n_param
    }
)

result = dataprime.process_df_operator()
```
### 9.链式调用
上述的单个数据处理方法可以进行链式调用，如:

`result = dp.order_by("time", "desc").sample(5, "random").dataframe`
