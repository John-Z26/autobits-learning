# 2026-11-08 建 dev 分支、解决一次冲突

## 做了什么
- 建 dev 分支，dev 和 main 各改 README 第一行，git merge dev 制造出一次冲突
- 删掉 <<<<<<< ======= >>>>>>> 三行标记，改成一行内容，git add + commit 完成合并
- git push + git push -u origin dev，把两个分支都推上去
- 项目全部做完（功能 10 条 + README + tag v0.1 + dev 分支）；算法今天没做

## 学了什么
- git commit -am 的 -a 只管已跟踪文件，新文件必须 git add
- git push -u 的 -u 是记住本地和远程分支的对应关系，以后直接 git push
- 冲突标记：<<<<<<< HEAD 是当前分支，======= 分界，>>>>>>> dev 是合进来的
- 解决冲突不是二选一，是自己决定最终内容

