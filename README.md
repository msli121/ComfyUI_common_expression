# ComfyUI_common_expression

这是一个为 ComfyUI 设计的自定义节点，用于实现常见的逻辑判断功能。

## 安装方法

1. 克隆此仓库到 ComfyUI 的 custom_nodes 目录:cd ComfyUI/custom_nodes
git clone https://github.com/your_username/ComfyUI_common_expression.git
2. 安装依赖:pip install -r requirements.txt
3. 重启 ComfyUI

## 节点功能

此节点提供以下几种判断功能:

1. **KeywordInString 判断**  
   - 输入: 一个文本和一个关键词文本(使用逗号分隔)
   - 输出: 如果文本中包含任意一个关键词，则返回 True，否则返回 False

2. **KeywordAllInString 判断**  
   - 输入: 一个文本和一个关键词文本(使用逗号分隔)
   - 输出: 如果文本中包含所有关键词，则返回 True，否则返回 False

3. **常见比较判断**  
   - 支持操作符: ==, !=, >, <, >=, <=
   - 可以比较字符串或数值

## 使用示例

1. 判断文本中是否包含特定关键词:
   - 设置 operation 为 "KeywordInString"
   - input_a 输入待检查的文本
   - input_b 输入关键词，使用逗号分隔(例如: "关键词1,关键词2")

2. 比较两个数值大小:
   - 设置 operation 为 ">", "<" 等
   - input_a 和 input_b 输入要比较的数值
   - 节点会尝试将输入转换为数值进行比较，如果失败则比较字符串长度

## 更新日志

- v1.0: 初始版本，支持基本的逻辑判断功能

## 贡献

欢迎提交问题报告或拉取请求来改进此节点!    