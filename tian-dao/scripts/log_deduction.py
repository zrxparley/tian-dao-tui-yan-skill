#!/usr/bin/env python3
"""
天道推演记录器 - 将推演结果自动记录到工作目录
"""
import os
import json
from datetime import datetime

WORKSPACE = os.path.expanduser("~/WorkBuddy/20260420083922")
MEMORY_DIR = os.path.join(WORKSPACE, ".workbuddy", "memory")

def log_deduction(question, paths, causality, confidence, followups):
    """记录推演结果"""
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(MEMORY_DIR, f"deduction-{today}.md")

    # 确保目录存在
    os.makedirs(MEMORY_DIR, exist_ok=True)

    content = f"""
## 推演记录 - {datetime.now().strftime('%Y-%m-%d %H:%M')}

### 原始问题
{question}

### 多路径推演
"""
    for path in paths:
        content += f"""
**路径 {path['name']}** (概率: {path.get('probability', 'N/A')})
- 触发条件：{path.get('trigger', 'N/A')}
- 结果：{path.get('outcome', 'N/A')}
- 蝴蝶点：{path.get('butterfly', 'N/A')}
"""

    content += f"""
### 因果链条
{cAUSALITY}

### 置信度
{confidence}

### 待验证节点
"""
    for f in followups:
        content += f"- {f}\n"

    content += "\n---\n"

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(content)

    return f"已记录到 {log_file}"

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        data = json.loads(sys.argv[1])
        print(log_deduction(
            data['question'],
            data['paths'],
            data['causality'],
            data['confidence'],
            data['followups']
        ))