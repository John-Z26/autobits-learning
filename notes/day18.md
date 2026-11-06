# 2026-11-06 学生成绩统计系统

## 今日核心
只完成一件事：把统计结果输出到文件（requirements 第 10 项）。
提交 1 次 —— `feat: 增加统计报告导出到 output/report.txt`（0a29df8）

## 做了什么
- 新增 save_report()：调用已有的 avg_score / max_score / min_score / pass_num
  拿到返回值，用 f-string 拼成报告，写入 output/report.txt
- 菜单从 6 项扩到 7 项（新增"输出并打印统计结果"）
- 报告最终形态：
      学生成绩统计报告
      ====================
      学生总人数:2
      及格人数:2
      平均分:84.00
      最高分:Alice 92
      最低分:Bob 76

## 踩的坑（按出现顺序）
1. 每行都没写 `\n`，五句话全挤在一行
2. 用三引号写菜单时保留了代码缩进，第 2–7 项前面多出 12 个空格，
   比原来挤成一行还难看
3. output 目录不存在时 open 直接抛 FileNotFoundError，
   用 try/except 兜住，改成中文提示

## 学到的
- `open(path, 'w')` 会自动创建文件，但**不会创建目录**

## 明天
- 写 README（运行方式、数据格式、输出示例）
