import argparse
import re
import json
from .analyzer import UrmiAnalyzer


def main(text):
    a = UrmiAnalyzer()

    words = re.findall('\\b(\\w[\\w\\-]*\\w|\\w)\\b', text)
    analyses = a.analyze_words(words, format='json')
    print(json.dumps(analyses, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analyze Urmi words and sentences from command line.\n'
                                                 'Usage: python3 -m uniparser-urmi (Urmi word here.)')
    parser.add_argument('text', default='', help='Text in Christian Urmi (Latin-based Assyrian New Alphabet)')
    args = parser.parse_args()
    text = args.text
    main(text)
