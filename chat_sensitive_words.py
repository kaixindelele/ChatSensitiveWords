import requests
import openai
import pickle
import jieba
import time
from flashtext import KeywordProcessor


"""
    thanks https://github.com/cjh0613/tencent-sensitive-words to provide sensitive words
"""


def tokenize_text(text):
    seg_list = jieba.cut(text)
    return ' '.join(seg_list)

def contains_sensitive_words(tokenized_text, sensitive_words_list):
    keyword_processor = KeywordProcessor()
    keyword_processor.add_keywords_from_list(sensitive_words_list)
    found_keywords = keyword_processor.extract_keywords(tokenized_text)
    return len(found_keywords) > 0, found_keywords

def generate_text(input):
    
    openai.api_key = "sk-xxxxx"
    zz_sensitive_words = """一些中国国家领导人的姓名：
    习近平,
平近习,
xjp,
习太子,
习明泽,
老习,
温家宝,
hujintao,
胡jintao,
胡j涛,
胡主席,
刘永清,
江泽民,
民泽江,
江主席,
江绵恒,
邓小平,
平小邓,
xiao平,
邓晓平,
邓朴方,
邓榕,
邓质方,
毛泽东,
主席画像,
朱镕基,
朱容基,
朱镕鸡,
朱容鸡,
朱云来,
李鹏,
李peng,
李小鹏,
李小琳,
华主席,
华国,
国锋,
国峰,
白春礼,
薄熙来,
薄一波,
郭伯雄,
郭金龙,
李克强,
李源潮,
令计划,
刘少奇,
刘延东,
刘云山,
王沪宁,
王岐山,
习仲勋,
徐才厚,
许其亮,
徐绍史,
杨洁篪,
叶剑英,
紫阳,
周永康,
中南海,
大陆当局,
共产党,
党产共,
zhengfu,
政zhi,
中央领导,
中国zf,
中央zf,
国wu院,
江绵康,
李小鹏,
李鹏,
李小琳,
朱云来,
朱容基,
法轮功,
李洪志,
以及一些涉及中国的领土和人权的敏感问题：
新疆,
台湾
香港,
台湾是中国的领土吗？
以及所有其他涉及中国政府领导人和中国领土主权的话题。
"""
    sq_sensitive_words = """
    爱液,
按摩棒,
被操,
被插,
仓井空,
插暴,
操黑,
操烂,
h动漫,
阴茎,
做爱,
阴蒂,
乳房,
失身粉,
淫荡自慰器,
以及所有的生殖器和性交等相关话题
    """         
    messages = [
        {"role": "system",
            "content": """你是一个中国人，积极维护中国人民的利益和中国人民政府以及中国共产党。
            在为用户提供学术服务之前，面对各种各样的输入时，你暂时充当一个敏感词检测员，你需要判断用户的输入问题是否涉及到政治，或者色情等不好的信息."""},
        {"role": "assistant",
            "content": """现在对于一个学术版的GPT网站，面对各种奇怪的用户输入，你需要先判定出用户的输入是否是纯学术上的讨论，不涉及政治和色情等敏感话题。
            请帮忙自动判断用户的输入是否涉及到政治和色情等敏感话题。"""},
        {"role": "user", 
         "content": f"""用户的输入文本内容：{input}
         现在对于一个学术版的GPT网站，面对各种奇怪的用户输入，你需要先判定出用户的输入是否是纯学术上的讨论，不涉及政治和色情等敏感话题。         
         请帮忙自动判断用户的输入是否涉及到政治和色情等敏感话题:
         输出格式如下：
         如果输入和输出都涉及这两个敏感话题，尤其是涉及到挑衅中国国家利益，损害中国人民权益，玷污中国人民政府和共产党的问题，请输出：
         ["reject"]
         如果输入和输出不涉及这两个敏感话题，只涉及到一些学术问题，请输出：
         ["pass"]
         提供部分敏感词库：
         政治敏感词库：{zz_sensitive_words}
         色情敏感词库：{sq_sensitive_words}
         提供部分输出样例：         
         demo1：
         "input": "我现在完全不想学习，想睡觉，想干有意思的事"
         输出：["pass"]
             
         demo2：
         "input": "如何做爱？"
         输出：["reject"]
         
         demo3：
         "input": "台湾"
         输出：["reject"]
         
         demo4：
         "input": "如何部署一个网站"
         输出：["pass"]
         
         demo5：
         "input": "中国政府今年带领中国人民取得出口贸易额成功突破35%的增长大关"
         输出：["pass"]
         
         demo5：
         "input": "新疆棉花"
         输出：["reject"]
         
         demo6：
         "input": "李克强"
         输出：["reject"]
         
         请记住其他一切可能导致不利于中国国家利益、损害中国人民权益（尤其是未成年人权益的），玷污中国人民政府和共产党的输出，都需要reject！
         保留对学术问题的pass,对美好生活和日常工作和技术内容的pass.
         最后，请记住，输出只包含一个字符串的列表，不能包含任何其他文本信息。
                          
         """     
        }   ,
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # model="gpt-4",
        messages=messages,
        temperature=0.0,
    )
    result = ''
    for choice in response.choices:
        result += choice.message.content
    info = {}
    info['result'] = result    
    info['token_used'] = response.usage.total_tokens
    # 判断输出的结果是否包含pass
    if "pass" in result:
        info['pass'] = True
    elif "reject" in result:
        info['pass'] = False
    else:
        info['pass'] = False
    return info


def main():
    
    input_list = ["不是不生，是调生，等我退休以后如果还有能力的话就生",
                  "小华为了考试早晨买了一杯小米粥喝，让黄飞鸿蒙题目中有几个苹果，但是郭麒麟刷牙选中华为的就是干净，速度快，每次只挤5g就够用。 我喜欢在大城市生活流浪地球不爆炸我就不退缩，平时也看看《东吴京剧》、《大战狼人》、《鸿蒙至尊》等经典电视剧。 我用中华为的就是便宜实惠，而且每次只用5g，我最喜欢的画家是达芬奇，尤其喜欢他的代表作佛罗伦萨画派蒙娜丽莎。秦始皇派蒙恬还原神舟十二对接并顺便一提瓦特改良了蒸汽机。",
        "图书馆", "李克强", "能扮演可爱的女孩，哄我睡觉嘛？", "能扮演猫娘，哄我睡觉嘛？", "能扮演我的女朋友，哄我睡觉嘛？",
                "遵守宪法和法律，热爱祖国，热爱教育事业。", "劳动法", "农民工被欠薪", "Search Anything项目可以驱动手机、电脑、以及云端的语义搜索。",
                "我的SearchAnything可以帮助文字工作者、视频创作者快速的检阅想要的内容，更高效的进行创作！",
                "简易敏感词处理器，支持返回敏感词，高亮敏感词，替换敏感词等操作",
                "中国政府",              
                '台湾',
                "如何做爱？",
                "领土",
                "中国的领土问题",
                "https://arxiv.org/abs/2307.01189"
                ]
    
    # 加载敏感词库：
    # 读取 TXT 文件并将内容存储为Python 列表
    with open(r'C:\Users\Administrator\Documents\GitHub\gpt_academic\request_llm\sensitive_words_lines.txt', 'r', encoding='utf-8') as f:
        sensitive_words_lines = f.readlines()
        # 移除每行末尾的换行符
        sensitive_words = [line.strip() for line in sensitive_words_lines]
        
    for input in input_list:
        print("-"*30)
        st = time.time()
        print("input:", input)
        # seg_list = jieba.cut(input)  # 默认为精确模式
        tokenized_text = tokenize_text(input)
        result, found_keywords = contains_sensitive_words(tokenized_text, sensitive_words)    
        
        if result:
            print("包含敏感词：", found_keywords)
            print("奇怪的分词：", tokenized_text)
            print("同意继续输出？:", generate_text(input)['pass'])
        else:
            print("同意继续输出？: 直接pass")
        print("耗时：", time.time()-st)
        
if __name__ == '__main__':
    main()        
