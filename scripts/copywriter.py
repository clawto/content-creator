#!/usr/bin/env python3
"""爆款标题/文案模板生成器"""
import sys, random

TITLE_TEMPLATES = {
    '小红书': [
        "震惊！{topic}竟然可以这样！第{n}条绝了",
        "学会这{n}个{topic}技巧，少走{n}年弯路",
        "男朋友偷偷学的{topic}，效果也太明显了吧",
        "全网都在找的{topic}攻略，我给你们整理好了",
        "分享一个超好用的{topic}方法，真的香！",
        "素人实测{n}天的{topic}，效果我服了",
    ],
    '抖音': [
        "如果你也想{topic}，一定要看完这条视频",
        "别再{topic}了！教你正确姿势",
        "{n}秒学会{topic}，第{n}个最重要",
        "普通人如何通过{topic}月入过万",
        "这条{topic}干货，建议收藏反复看",
    ],
    '知乎': [
        "如何高效地{topic}？{n}个方法让你事半功倍",
        "长期{topic}的人，后来都怎么样了？",
        "关于{topic}，你需要知道的{n}个真相",
        "有什么{topic}的技巧，让人相见恨晚？",
    ],
    'B站': [
        "【硬核】{topic}终极指南，全网最全没有之一",
        "你不懂的{topic}，这{n}分钟给你讲明白",
        "【干货】{topic}保姆级教程，手把手教学",
    ]
}

def generate(platform, topic, n=5):
    templates = TITLE_TEMPLATES.get(platform, TITLE_TEMPLATES['小红书'])
    print(f"🎯 {platform} 标题灵感 - {topic}:\n")
    
    for i, tmpl in enumerate(random.sample(templates, min(len(templates), 5)), 1):
        title = tmpl.replace('{topic}', topic).replace('{n}', str(n))
        print(f"  {i}. {title}")
    
    print(f"\n💡 标题公式:")
    print(f"  数字 + 痛点 + 解决方案 + 情绪词")
    print(f"  例: '{n}个{topic}技巧' → 数字感 + 实用性")

def main():
    platform = sys.argv[1] if len(sys.argv) > 1 else '小红书'
    topic = sys.argv[2] if len(sys.argv) > 2 else '护肤'
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    generate(platform, topic, n)

if __name__ == '__main__':
    main()
