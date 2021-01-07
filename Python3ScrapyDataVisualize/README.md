- 适用于python的colab平台https://colab.research.google.com/notebooks/intro.ipynb#

- python基础

  - 基本数据类型（不用自己）：

  - 常用的数据结构：

    - number
      - 常用类型：int, float, bool,fractions,complex

    - string

    - list

    - tuple 与list类似但不可修改

    - dictionary

    - set

  - 常用运算符号

    - 逻辑运算符号：and/or/not

    - 成员运算符号：in/not in

    - 身份运算符：is, is not(判断是否是同一内存)

- 爬虫

  - 爬虫入门

    - request库:抓取网页

      - get(url,headers=headers)

      - post(url,data=JSON)

    - BeautifulSoup分析网页：集成在bs4库里面
      - demo：BeautifulSoup(xxx.html,'lxml').select("#main>div.mtop.fistMod)

    - 常用的反爬虫技巧：

      - 设置headers参数
        -  {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

      - 设置多个代理IP
        - proxies={ip1, ip2}

    - 多进程爬虫用的库是Pool()

  - scrapy使用（再看一次）

    - 一个scrapy爬虫的目录

      - [item.py](http://item.py/) 保存数据

      - [middlewares.py](http://middlewares.py/) 中间件

      - [pipelines.py](http://pipelines.py/) 核心处理

      - [setting.py](http://setting.py/)

      - scrapy.cfg

  - selenium的使用：

    - 定位位置（8种，主要使用）

      - find_element_by_css_selector

      - find_element_by_xpath

    - 操作：

      - 填充：先将填充框清零，再进行操作设置

        - driver.find_element_by_xpath("//*[@id='depCity']").clear()

        - driver.find_element_by_xpath("//*[@id='depCity']").send_keys(dep)

      - 滑动
        - ActionChains(driver).move_to_element(ac).perform()

      - 点击
        - driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[3]/div/div[2]/div/a").click()

  - 多进程请求：pool 函数 ：库multiprocessing

    - demo：

      - pool=Pool()

      - [pool.map](http://pool.map/)(get_all_data,dep_list.split())

  - 例子：

    - 用API爬取天气数据

    - 大型电商的相关数据进行抓取

- 数据清洗

  - Database

    - mongodb：pymongo库

      - 连接数据库：client=pymongo.MongoClient('[localhost](http://localhost/)',27017);

      - 新建数据库:db =client["db_name"];

      - 新建表: table = db["table_name"];

      - 写入数据:table.insert({"key1":value1,"key2":value2})

      - 删除数据:table.remove({"key":value});

      - 修改数据:table.update({"key":value,{"$set"}});

      - 查询数据:table.find({"key":value})

    - mysql：pymysql

      - connection

        - 例子：host, port,user,password, db, charset="utf8"

        - cursor

          - execute(op) 执行语句

          - fetchone取得结果集的下一行

          - fetchmany(size)取得结果集的下几行

          - fetchall()

          - rowcount()返回数据条数或者影响行数

          - close()关闭游标对象

        - commit

        - rollback

        - close

      - 使用SQLAlchemy

        - 表结构定义：

          - ID = Column(String(20),primary_key=true)

          - 

        - 连接

          - engine = create_engine('mysql+pymysql'://root:password@localhost:3306/test)

          - DBSession = sessionmaker(bind = engine);

  - NumPy常用
    - 常用数据结构：
      - Ndarray: np及其相关的函数

  - pandas常用 

    - Series

    - DataFrame：类似于Excel

    - 读取数据,筛选数据进行定位
      - df= pd.read_csv("D:/taobao_data.csv")

    - 行
      - df[0:3]

    - 列
      - df[['column_name']]

    - 块
      - df.ix[0:3,["column_name1",'column_name2']]

    - 查看表数据
      - [df.info](http://df.info/)()

    - 查看表的描述性统计
      - df.describe()

    - 分组
      - df.groupby(df['column_name'])

    - 分割

    - 合并

      - 数据库风格的合并

        - pd.merge(df1,df2,how=how)

        - how值的定义：outer, left, right

      - 索引上的合并

        - pd.merge(df1, df2, left_index=True, right_index=True)

        - df1.join(df2)

      - 轴向连接
        - pd.concat([pd1,pd2,pd3])

    - 变形

      - 行变列：data.stack()

      - 层次化索引，列变行：data.unstack()

      - 筛选：df = pd.pivot_table(df,values=[""],index=[""],columns=[""])

  - 缺失，异常，重复的简单处理方法

    - 查看是否有缺失值
      - df.isnull()

    - 删除行
      - df.dropna(axis=0)

    - 删除列
      - df.dropna(axis=1)

    - 使用统一字符串填充
      - df.fillna("missing")

    - 使用前一个数据代替
      - df.fillna(method='pad')

    - 使用后一个数据代替
      - df.fillna(method='bfill',limit=1)

    - 使用平均值df.mean()

  - 检测和过滤异常值

    - 基于统计与数据分布

      - 指定画图区域：fig,ax=plt.subplot(1,1,figsize(8,5))

      - ax.hist(df["row"],bins = 20);

      - 正态分布：值大于3个标准差

        - zscore = (d-d.mean())/d.std()

        - df["abnormal"] = zscore.abs()>3

    - 箱行图分析

      - df.boxplot(column="value", ax = ax)

      - 大于75% d>d.quantie(0.75)

    - 移除重复数据

      - 查看重复数据: df.duplicated("value");

      - 移除重复数据:df.drop_duplicates("value")

  - 时序数据处理

    - 日期/时间数据转换

      - 秒时间time.time()

      - 系统时间time.localtime()

      - 系统时间的转换

        - time.strftime('%Y-%y-%d-%x', time_localtime())

        - time.mktime(time_localtime())

      - 秒时间的转换
        - time.strftime('%Y-%y-%d-%x', time_localtime(time.time()))

    - 时序数据基础操作

      - 时间生成：pd.date_range(starttime)

        - 天 periods

        - 小时 freq = "H"

      - 时间序列
        - pd.Series(np.arange(31),index=pd.date_range());

  - 数据类型转换

    - 将某列数据集体转换：
      - df['Column'].astype("int")

    - 使用自定义函数：
      - df['Column'].apply(lambda x: x+1)

  - 正则表达式方法（与其他的语言类似）

  - 综合例子

- 数据可视化

  - matplotlib

    - 设定画图背景样式
      - mpl.style.use('ggplot')

    - 设定画布
      - fig,(ax1,ax2) =  plt.subplots(1,2,figsize = (12,4))

    - 画图及设定元素

      - df_mean.价格.plot(kind = 'barth',ax=ax1)

      - ax1.set_xlabel("各省份平均价格")

    - 自动调整格式

      - fig.tight_layout()

      - 更改kind属性

        - 折线图line

        - 柱状图bar

        - 箱行图box

        - 饼图pie

      - 散点图ax.scatter

  - echarts

  - pyecharts

    - matplotlib上面有的都有，除此之外

      - 漏斗图Funnel

      - 仪表盘Gauge

      - 水球图Liquid

      - 词云WorldCloud

      - 3D柱形图Bar3D

    - 使用Overlap在同一个画布画多个图形

      - overlap=Overlap()

      - overlap.add(bar)

      - overlap.add(line)

      - overlap.render('D:/linebar.html')