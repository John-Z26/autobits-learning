# PR操作步骤

## Git 分支 + PR 完整流程

### 一、本地

```bash
# 1. 回到 main 并更新（这步最容易忘，忘了分支会基于旧代码）
git switch main
git pull

# 2. 建并切到新分支
git switch -c 分支名

# 3. 确认切换成功
git branch --show-current

# 4. 改文件……

# 5. 看改了什么
git status          # 哪些文件变了
git diff            # 具体哪几行变了

# 6. 暂存 + 提交
git add 文件名
git commit -m "前缀: 说明"

# 7. 第一次推（-u 绑定上游，之后只写 git push）
git push -u origin 分支名
```

### 二、GitHub 网页

8. 仓库首页出现黄色横幅 → 点「Compare & pull request」
   （没有横幅：Pull requests → New pull request → base=main, compare=分支）
9. 填标题（同 commit message）+ 描述（**写为什么改**）
10. 点「Create pull request」
11. 点「Merge pull request」→「Confirm merge」
12. 点「Delete branch」

### 三、回本地同步

```bash
git switch main
git pull
git log --oneline -3     # 确认自己的提交已经在 main 上
```

### 关键点

| 点 | 说明 |
|---|---|
| 建分支前必须 `git pull` | 否则分支基于旧的 main，合并时容易冲突 |
| 第一次 push 必须 `-u` | 绑定上游后，以后只写 `git push` |
| `-u` 绑了什么 | 让 Git 知道「本地这个分支对应远程哪个分支」，`git status` 才能提示“领先 2 个提交” |
| PR 和直接 merge 的区别 | 合并动作一样（都是 `git merge`），PR 多了**评审**和**记录** |
| 自己仓库 vs 别人仓库 | 自己的仓库 PR 是自律；别人的仓库没写权限，PR 是**唯一通道** |