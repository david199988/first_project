# first_project

一个判断闰年的小工具。

## 用法

```bash
# 检查当前年份
./leap.py

# 检查指定年份（可传多个）
./leap.py 2024
./leap.py 1900 2000 2023

# 脚本里用，只输出 yes / no
./leap.py -q 2024
```

退出码：全部为闰年返回 `0`，否则返回 `1`。

## 规则

公历闰年：能被 4 整除，但不能被 100 整除；能被 400 整除的年份仍为闰年。

| 年份 | 闰年 |
|------|------|
| 2024 | ✅ |
| 2023 | ❌ |
| 1900 | ❌（整百年且不能被 400 整除） |
| 2000 | ✅（能被 400 整除） |

## 测试

```bash
python3 -m unittest -v
```

## 部署到新的 Linux 机器

整个工具没有任何第三方依赖，只需要 Python 3.10+。不需要 pip、不需要虚拟环境，拷两个文件就能跑。

### 0. 确认 Python 版本

```bash
python3 --version   # 需要 3.10 或更高
```

没有的话按发行版装：

```bash
sudo apt install python3        # Debian / Ubuntu
sudo dnf install python3        # RHEL / Rocky / AlmaLinux
sudo apk add python3            # Alpine
```

### 方式一：clone 仓库（推荐，方便后续 `git pull` 升级）

仓库是私有的，clone 前需要认证，任选一种：

```bash
# 用 gh CLI（如果机器上装了）
gh auth login
gh repo clone david199988/first_project && cd first_project

# 或者走 HTTPS，提示时输入用户名 + Personal Access Token
git clone https://github.com/david199988/first_project.git
```

然后在仓库目录里直接跑：

```bash
./leap.py
```

### 方式二：装成全局命令 `leap`

适合不想保留仓库目录、只想在任意路径下调用的场景。在仓库目录里执行：

```bash
sudo install -m 755 leap.py /usr/local/bin/leap
```

之后任意位置都能用：

```bash
leap 2024        # 2024 是闰年
leap -q 1900     # no
```

`/usr/local/bin` 一般已在 `$PATH` 里；如果是精简镜像，确认一下 `echo $PATH`，或改装到 `~/.local/bin/leap`（不需要 sudo）。

### 方式三：不 clone，直接传文件

适合无法访问 GitHub 的机器（脚本里 shebang 是 `/usr/bin/env python3`，改文件名不影响运行）：

```bash
scp leap.py user@host:/tmp/leap.py
ssh user@host 'sudo install -m 755 /tmp/leap.py /usr/local/bin/leap && leap'
```

### 验证部署

```bash
leap 2024 && leap -q 1900   # 前者应输出闰年并返回 0，后者输出 no
```

想跑单元测试，需要 `test_leap.py` 和 `leap.py` 在同一目录：

```bash
python3 -m unittest -v
```

### 定时检查（可选）

想在 12 月 31 日自动判断下一年是否为闰年，可以挂 cron：

```bash
0 23 31 12 *  /usr/local/bin/leap -q $(date +\%Y -d "+1 year") >> /var/log/leap.log 2>&1
```

注意 crontab 里 `%` 需要转义成 `\%`。

## 环境

Python 3.10+，无第三方依赖。