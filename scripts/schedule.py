#!/usr/bin/env python3
"""最佳发布时间建议"""
import sys
from datetime import datetime, timedelta

SCHEDULE = {
    '抖音':   {'best': [7, 12, 18, 21], 'desc': '碎片化时间高峰'},
    '小红书':  {'best': [8, 12, 17, 20], 'desc': '通勤+午休+下班后'},
    '知乎':    {'best': [8, 12, 19, 22], 'desc': '上班摸鱼+晚间深度阅读'},
    'B站':     {'best': [12, 17, 20, 22], 'desc': '饭点+睡前长视频'},
    '公众号':  {'best': [7, 12, 18, 21], 'desc': '节奏类似微信'}
}

def main():
    plt = sys.argv[1] if len(sys.argv) > 1 else 'all'
    now = datetime.now()
    
    for p, info in SCHEDULE.items():
        if plt != 'all' and p != plt:
            continue
        
        print(f"📅 {p} 最佳发布时间:")
        print(f"  {info['desc']}")
        for h in info['best']:
            label = f"{h}:00"
            if now.hour == h:
                label += " ← 现在！"
            elif now.hour == h - 1 and now.minute > 30:
                label += " ← 马上"
            print(f"    🕐 {label}")
        print()

if __name__ == '__main__':
    main()
