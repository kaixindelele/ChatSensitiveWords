# ChatSensitiveWords
利用LLM来自动判别是否涉及敏感词。可以结合敏感词库和向量数据。

# Motivation：
在[chatpaper](https://chatwithpaper.org)中，我们免费提供了[学术版GPT](https://github.com/binary-husky/gpt_academic)完整功能，这里面有一个隐藏的对话功能，我们希望给大家提供一个学术对话接口，但防不住大家好奇，或者有极少数人故意攻击我们的输出。

因此我们需要紧急上线敏感词检测。尤其是针对政治敏感词和色情敏感词。

# 方案：
1. 传统敏感词库检测是否有敏感词
2. 如果有敏感词，让Chat来判断语义，是否有误杀。

# 使用步骤：
1. pip install -r requirements.txt
2. 替换api key
3. 确认敏感词库路径是否正确。

# 初步效果：
![1688477764180](https://github.com/kaixindelele/ChatSensitiveWords/assets/28528386/39f7ecf8-124f-4dd8-a751-9669ab2811b1)

![1688477785323](https://github.com/kaixindelele/ChatSensitiveWords/assets/28528386/a3d07a10-ebc3-4384-bb1a-9722a14f59d9)

# 欢迎大家一起玩耍
目前传统敏感词库的检测还没有做好，然后chat的prompt也没有调到最优。
