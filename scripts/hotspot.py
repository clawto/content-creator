#!/usr/bin/env python3
"""多平台热点聚合"""
import json, sys, urllib.request, urllib.error

def fetch_weibo():
    try:
        with urllib.request.urlopen("https://weibo.com/ajax/side/hotSearch", timeout=10) as r:
            data = json.loads(r.read())
            return [(i['word'], i.get('raw_hot', 0)) for i in data.get('data', {}).get('realtime', [])[:10]]
    except: return []

def fetch_zhihu():
    try:
        with urllib.request.urlopen("https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=10", timeout=10) as r:
            data = json.loads(r.read())
            return [(i['target']['title'], i['target'].get('excerpt', '')) for i in data.get('data', [])]
    except: return []

def fetch_douyin():
    """Douyin trending - scraping hints (no official free API)"""
    return [
        ("抖音热榜", "官方API需企业认证"),
        ("查看热榜", "https://www.douyin.com/hot")
    ]

def main():
    platform = sys.argv[1] if len(sys.argv) > 1 else 'all'
    
    if platform in ('weibo', 'all'):
        print("📱 微博热搜 TOP10:")
        for i, (word, hot) in enumerate(fetch_weibo(), 1):
            bar = '🔥' if hot > 1000000 else ('🔴' if hot > 500000 else '🟠')
            print(f"  {i:2}. {bar} {word}" + (f" ({hot/10000:.0f}万)" if hot else ""))
        if not fetch_weibo(): print("  ⚠️ API需登录态")
    
    if platform in ('zhihu', 'all'):
        print("\n🤔 知乎热榜 TOP10:")
        for i, (title, excerpt) in enumerate(fetch_zhihu(), 1):
            print(f"  {i:2}. {title}")
        if not fetch_zhihu(): print("  ⚠️ 知乎API不可用")
    
    if platform in ('douyin', 'all'):
        print("\n🎵 抖音热榜: 需企业认证 | https://www.douyin.com/hot")
    
    print("\n💡 创作选题建议:")
    print("  • 追热点: 微博热搜 前3 + 你的领域 = 爆款公式")
    print("  • 小红书: 封面 > 标题 > 内容")
    print("  • 发布时间: 早7-9, 中12-14, 晚18-22")

if __name__ == '__main__':
    main()
