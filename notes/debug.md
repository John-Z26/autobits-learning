# Debug 记录
> 记录项目开发中真实遇到的三类问题：路径、数据格式、版本控制。
## 1. 换到其他目录运行时报 FileNotFoundError

**现象：**
从 C:\Users\ASUS 目录执行 C:\Student_statistics\.venv\Scripts\python.exe src\run.py，
报 FileNotFoundError: [Errno 2] No such file or directory: 'data/students.json'

**复现：**
1. 项目根目录下 python src/run.py → 正常运行
2. cd 到上一级，用绝对路径调同一个脚本 → 报错

**假设：**
第一反应是"data/students.json 没提交"。

**证据：**
- 在项目根目录 ls data/ → students.json 在，文件没丢
- 在 C:\Users\ASUS 下 ls data/ → 没有这个目录
- git status → 工作区干净，文件已提交

三条证据把"环境问题"和"文件丢失"都排除了。

**根因：**
`open('data/students.json')` 用的是相对路径，相对的是**当前工作目录**，
不是脚本文件所在目录。所以在别的目录运行时，程序会去那个目录下找 data/。

**修复：**
不改代码。README 中已声明"必须在项目根目录运行"。
（彻底的做法是用 `os.path.dirname(__file__)` 拼绝对路径，但这会牺牲"直接跑"的便利。）

**验证：**
回项目根目录执行 python src/run.py，正常加载 2 条记录。

## 2. JSON 缺少外层方括号导致 Extra data

**现象**
数据文件里并排写了两条学生记录、但外面没有 `[]`：

```json
{
  "id": "2026001", "name": "Alice", "score": 92
},
{
  "id": "2026002", "name": "Bob", "score": 76
}
```

运行时程序没有崩溃，而是打印：
错误:JSON 格式错误，第 6 行第 2 列：Extra data

**复现：**
把 data/students.json 的内容改成上面这样（去掉最外层的 `[` 和 `]`），
在项目根目录执行 python src/run.py。

**假设：**
第一反应是"程序应该会跳过出错的那条记录，继续加载剩下的"。
因为我在校验逻辑里写了"非法记录自动跳过并给警告"，
以为 JSON 解析层也是同样的按条容错。

**证据：**
- 提示只有一行，没有任何"学生信息加载完成，共 N 条"的输出 → 说明**一条都没加载**
- 把文件改回带 `[]` 的格式，立刻正常加载 2 条
- 报错位置是"第 6 行第 2 列"，不是第 1 行 → 说明解析器已经读完了第一段，是在**后面**才出问题

**根因：**
JSON 规范要求**一个文件顶层只能有一个值**。
解析器读到第一个 `{...}` 结束时，认为"文档到此为止"，
后面的 `,{...}` 就成了预期之外的多余数据 → Extra data。

这和我的假设正好相反：**JSON 解析是全有或全无的**——
任何一处不合法，整份文件都拿不到结果，不存在"跳过坏的那条"。
"跳过坏记录"那套逻辑，是我在拿到 list 之后逐条校验时才生效的。

**修复：**
在文件最外层加上 `[` 和 `]`，让顶层成为一个数组：
```json
[
  { "id": "2026001", "name": "Alice", "score": 92 },
  { "id": "2026002", "name": "Bob", "score": 76 }
]
```

**验证：**
重新运行，输出「学生信息加载完成，共 2 条有效记录」，两条都能查到。

## 3. 合并 dev 到 main 时 README.md 冲突

**现象：**
git merge dev 后提示：
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.

**复现：**
main 和 dev 都修改了 README.md 的标题行

**假设：**
以为 Git 会自动选一个版本（取新的或者取 main 的）

**证据：**
打开 README.md 看到 <<<<<<< HEAD / ======= / >>>>>>> dev 三段标记

**根因：**
两个分支改了同一文件的同一区域，Git 无法判断该保留哪个，就把决定权交给人

**修复：**
1. 手动删除 <<<<<<< ======= >>>>>>> 三行标记
2. 保留想要的内容（当时保留的是 main 的标题）
3. git add README.md → git commit

**验证：**
git log --graph 看到分叉和合并点；文件内容正确
