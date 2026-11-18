# textkit 안내

textkit은 글에서 단어를 세는 작은 연습용 모듈입니다.

## 준비

저장소를 복제한 뒤 저장소 폴더에서 아래 명령을 실행합니다. 따로 설치할 패키지는 없습니다.

## 사용법

`count_word`는 글을 받아 단어별 등장 횟수를 돌려줍니다. 대소문자는 구분하지 않습니다.

```python
from textkit import count_word

count_word('사과 배 사과')  # {'사과': 2, '배': 1}
```

`textkit.report`의 `top_words`는 가장 많이 나온 단어를 n개까지 돌려주고, `format_report`는 그 결과를 줄마다 "단어: 횟수"로 보여 줍니다.

## 시험

시험은 표준 라이브러리의 unittest로 돌립니다.

```sh
python -m unittest discover -s tests
```

## 설정

`config/settings.json`의 `top_n`은 보고서에 보여 줄 단어 수의 기본값입니다.
