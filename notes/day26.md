# 2026-11-14  P5736、venv 虚拟环境和三种格式比较

## P5736 质数筛：从 O(n) 到 O(√n)

为什么到 √x 就够：因为因子成对出现。
36 = 1×36 = 2×18 = 3×12 = 4×9 = 6×6
每对里小的那个一定 ≤ √36 = 6。试到 6 没找到，后面就不可能有。

实测 x=99991（质数）：到 x-1 用 1.82 ms，到 √x 用 0.01 ms，快 182 倍。

判断标准：写完看一眼数据范围，估算最坏循环次数，超过 10⁷ 就优化。
AC 只证明对了，不证明够好。

## venv：一个项目锁定一个 Python版本

### 为什么需要
机器上可能有多个版本的python，如： 3.8 / 3.13 / 3.14 我项目中models.py 第 158 行用了 match（3.10+），
在 3.8 下：SyntaxError: invalid syntax
—— 不是运行出错，是文件根本解析不了。
### 操作链（7步）
1. py -3.14 -m venv .venv          # 建（-m 是运行模块，不是 -venv）
2. .venv\Scripts\Activate.ps1      # 激活
3. pip -V                          # 确认 pip 指向 .venv（看路径，比看提示符可靠）
4. pip install pytest              # 装包
5. pip freeze > requirements.txt   # 导出清单
6. pip uninstall -r requirements.txt -y   # 卸干净
7. pip install -r requirements.txt        # 从清单恢复
### 三个容易误解的点
1. 激活只改当前窗口的 PATH，关掉就失效
2. 不激活就 pip install，会装到全局
3. .venv 被 gitignore，别人拿不到 —— 他拿到的是 requirements.txt（菜谱），不是厨房
### 删了重装的意义
不删就分不清"清单写对了"和"环境本来就有"。
删空 → 从清单恢复，是从零验证。

## JSON / YAML / CSV 三格式对比
1. 哪个手写最省事 
- 手写最省事 → 最麻烦：CSV → YAML → JSON
2. 哪个能写注释 
- 只有YAML支持
3. 哪个中文最容易出问题
-  CSV>JSON>YAML
4. 哪个 json.load 一行读进来 
- JSON
5. 三个文件各多大
- JSON>YAML>CSV
