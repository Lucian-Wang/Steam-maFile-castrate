# Steam maFile 阉割工具

## 项目简介

Steam-maFile-castrate 是一个用于批量处理 Steam maFile 文件的图形化工具，能够一键移除（“阉割”）所有 maFile 文件中的 `identity_secret` 字段，并将处理结果保存到指定目录，原始文件不会被覆盖。适合批量管理和分发 maFile 文件时，去除敏感信息。

## 主要功能

- 批量扫描指定目录下的所有 `.maFile` 或 `.json` 文件。
- 自动剔除每个文件中的 `identity_secret` 字段内容（置空）。
- 保证原始文件不被修改，所有处理后的文件按原有目录结构输出到新目录。
- 提供简单易用的图形界面（Tkinter 实现）。
- 操作日志实时输出，异常、跳过、成功等均有提示。

## 安装方法

1. 克隆本项目到本地：

   ```bash
   git clone https://github.com/Lucian-Wang/Steam-maFile-castrate.git
   cd Steam-maFile-castrate
   ```

2. 安装运行环境（推荐 Python 3.6 及以上版本）：

   - 仅依赖 Python 标准库，无需额外第三方依赖。

## 使用说明

1. 运行程序：

   ```bash
   python mafile_gui_strip.py
   ```

2. 操作步骤：

   - 在界面中点击“浏览”，选择待处理的 maFile 文件根目录（源目录）。
   - 再次点击“浏览”，选择处理后文件的保存目录（目标目录）。
   - 注意：源目录和目标目录不能相同。
   - 点击“批量阉割”，等待提示“全部完成！新文件已存到指定目录”。

3. 处理结果：

   - 每份 maFile 文件的 `identity_secret` 字段会被置空，其他内容保持不变。
   - 处理后的文件输出到指定保存目录，保持原有目录层级结构。
   - 原始文件不会被覆盖或修改。

## 依赖环境

- Python 3.6 及以上
- 标准库：`os`, `json`, `tkinter`

## 注意事项

- 请确保你有权访问和处理相关 maFile 文件，谨慎操作，防止泄露敏感信息。
- 目标目录建议为空目录，防止与已有文件冲突。
- 仅处理扩展名为 `.maFile` 或 `.json` 的文件，其他文件会被自动跳过。
- 如果文件内容格式异常，将自动跳过并显示错误信息。

## 贡献指南

欢迎提出 Issue 或 Pull Request 进行完善和功能建议。

1. Fork 本仓库，提交你的改动。
2. 保持代码风格一致，并尽量附带详细注释。
3. 测试你的改动，确保无误后发起 PR。

---

© [Lucian](https://lucian.wang/)

## 维护与反馈

维护者：[Lucian](https://lucian.wang/) · 邮箱：im@lucian.wang · [问题反馈](https://github.com/Lucian-Wang/Steam-maFile-castrate/issues)
