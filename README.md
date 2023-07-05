# ChatSensitiveWords
利用LLM+敏感词库，来自动判别是否涉及敏感词。已经在[chatpaper](https://chatwithpaper.org)上线！

# Motivation：
在[chatpaper](https://chatwithpaper.org)中，我们免费提供了[学术版GPT](https://github.com/binary-husky/gpt_academic)完整功能，这里面有一个隐藏的对话功能，我们希望给大家提供一个学术对话接口，但防不住大家好奇，或者有极少数人故意攻击我们的输出。

因此我们需要紧急上线敏感词检测。尤其是针对政治敏感词和色情敏感词。

# 方案：
1. 传统敏感词库检测是否有敏感词
2. 如果有敏感词，让Chat来判断语义，是否有误杀。
3. 输出敏感词检测（待做）

# 使用步骤：
1. pip install -r requirements.txt
2. 替换api key
3. 确认敏感词库路径是否正确。

# 初步效果：
<details><summary><code><b>一些有意思的案例截图</b></code></summary>
  
![GO5YV8RZ$$FOQ) 4 CEBHKG](https://github.com/kaixindelele/ChatSensitiveWords/assets/28528386/1a05c2a1-8572-4744-aa12-6098bb0b0826)

![M MNO8I853}YN RNLCGXNPR](https://github.com/kaixindelele/ChatSensitiveWords/assets/28528386/d46a16af-2b38-4ccb-856b-263b0c5aac00)

![FA LNCEEAC(XT05JVAQUJ~4](https://github.com/kaixindelele/ChatSensitiveWords/assets/28528386/23ca1586-3ed1-418d-8093-20999e9c6c03)

![7JU@}TJ 0)N8Z3{Z_63FE H](https://github.com/kaixindelele/ChatSensitiveWords/assets/28528386/eefd58ff-44e9-439c-8d4b-fbbd9e0ac8e8)

</details>

# 时间消耗分析：
无敏感词的情况，消耗0.2s左右

有敏感词，消耗0.2+0.8s左右。

欢迎大家在本地测试和评估。
**千万别在我们的学术版上测试！**

# 欢迎大家一起玩耍
目前传统敏感词库的检测还没有做好，然后chat的prompt也没有调到最优。

欢迎大家star和pull新功能！

# 如果对搭网站的朋友有帮助的话，也欢迎打赏, 感谢认可！

![8F26{U54RLC EUL6(MNEZPA](https://github.com/kaixindelele/ChatSensitiveWords/assets/28528386/1e87e11a-fbe2-4f7d-a754-ce8f596c0a4d)

## 请不要打包卖钱，如果卖钱的话，分我点...


# Starchart

[![Star History Chart](https://api.star-history.com/svg?repos=kaixindelele/ChatSensitiveWords&type=Date)](https://star-history.com/#kaixindelele/ChatSensitiveWords&Date)

## Contributors

<a href="https://github.com/kaixindelele/ChatSensitiveWords/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=kaixindelele/ChatSensitiveWords" />
</a>


## 项目引用：
Please cite the repo if you use the data or code in this repo.

```
@misc{ChatPaper,
  author={Yongle Luo},
  title = {ChatSensitiveWords: Use LLM and sensitive word library to check sensitive input text.},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/kaixindelele/ChatSensitiveWords}},
}
```

