## 2020-12-24 Data Structure
Playground for topics related to data structure

- 2021-01-19 data-container-comparison
  - comparing performance of different data containers that can hold named fields: namedtuple, dataclass, class
  - results (rough avg)
    - env: python 3.9.1, macos catalina 10.15.3, intel i3-1000NG4
    - create:
      - class: 1050ns
      - dataclass: 950ns
      - namedtuple: 930ns
    - attribute access:
      - class: 300ns
      - dataclass: 300ns
      - namedtuple (by name): 270ns
      - namedtuple (by index): 240ns
  - there's minor difference that may become useful when tuning for performance (~20%)
  