# MemoWriter Documents

## WorkFlow

* 클래스 기반으로 작동하기때문에, 변수에 할당하여 내부 메서드를 사용합니다.
* 메모를 기입할 때마다 클래스 내부적으로 **로그** 인스턴스가 업데이트됩니다.
    * 글번호(ID)가 매겨진 메모 내역이 로그 내부에 저장됩니다.
    * 글번호는 작성된 순서에 따라 자동으로 매겨집니다.

```python
writer = MemoWriter(author='고지형') # 작성자명을 기입하며 initialize
writer.write_xxxx() # 메모하기 
writer.show_xxxx() # 메모 보기
writer.export_xxxx() # 메모 저장하기
...
```



## Write: 메모하기

* `write_diary`, `write_schedule` 메서드를 호출하여 다이어리 또는 스케줄을 작성합니다.
* 함수 내부적으로 `input()` 함수를 통해 사용자에게 작성 가이드라인을 제공합니다.

#### Diary: 다이어리 작성

* 다이어리는 다음과 같은 양식으로 저장됩니다.
    `날짜:`
    `날씨:`
    `제목:`
    `내용: `

```python
>>> writer.write_diary()
>>> 날짜 입력: 2020-12-20
>>> 날씨 입력: 맑음
>>> 제목 입력: 어느 일요일의 아침
>>> 내용 입력: 생각보다 일찍 일어나서 아침에 커피를 마셨다.
[다이어리가 기록되었습니다]
작성 시간:2020-12-20 19:44:35
작성자:고지형

날짜: 2020-12-20
날씨: 맑음
제목: 어느 일요일의 아침
내용: 생각보다 일찍 일어나서 아침에 커피를 마셨다.
```

#### Schedule: 스케줄 작성

* 스케줄은 다음과 같은 양식으로 저장됩니다.
    `날짜:`
    `시간:`
    `내용:`

```python
>>>writer.write_schedule()
>>> 날짜 입력: 2020-12-22
>>> 시간 입력: 오후 2시
>>> 내용 입력: 코딩 테스트
[일정이 기록되었습니다]
작성 시간:2020-12-20 19:47:15
작성자:고지형

날짜: 2020-12-22
시간: 오후 2시
내용: 코딩 테스트
```

## Show: 메모 내역 확인하기

* `show_diary`, `show_schedule` 메서드를 호출하여 지금까지 작성한 메모를 조회합니다.

#### Diary: 다이어리 기록 확인

```python
>>> writer.show_diary()
[작성하신 다이어리 내역입니다]

글 번호: 0
작성자: 고지형
작성 시간: 2020-12-20 19:44:35
날짜: 2020-12-20
날씨: 맑음
제목: 어느 일요일의 아침
내용: 생각보다 일찍 일어나서 아침에 커피를 마셨다.


글 번호: 2
작성자: 고지형
작성 시간: 2020-12-20 19:48:41
날짜: 2020-12-20
날씨: 맑음
제목: 어느 일요일의 저녁
내용: 배가 많이 고파서 오늘은 삼겹살을 구워 먹었다.
    
# 작성한 다이어리가 없는 경우
>>> writer.show_diary()
[작성하신 다이어리 내역입니다]

작성 내역 없음
```

#### Schedule: 스케줄 기록 확인

```python
>>> writer.show_schedule()
[작성하신 일정 내역입니다]

글 번호: 1
작성자: 고지형
작성 시간: 2020-12-20 19:47:15
날짜: 2020-12-22
시간: 오후 2시
내용: 코딩 테스트


글 번호: 3
작성자: 고지형
작성 시간: 2020-12-20 19:49:28
날짜: 2020-12-23
시간: 오후 4시
내용: AI 세미나
    
# 작성한 스케줄이 없는 경우
>>> writer.show_diary()
[작성하신 일정 내역입니다]

작성 내역 없음
```

## Export: 메모 저장하기

* `export_diary`, `export_schedule` 메서드를 통해 작성한 메모를 텍스트 파일 형태로 저장합니다.
* `export_all` 메서드 호출 시 작성한 다이어리와 스케줄을 일괄 저장합니다.
* 작성된 내역이 없는 경우 파일이 생성되지 않으며, 알림 메시지가 출력됩니다.

#### Diary: 다이어리 기록 저장

```python
>>> writer.export_diary(save_path='./', name='오늘의 일기.txt')
다이어리가 저장되었습니다.	c:\Users\iloveslowfood\Documents\GitHub\Algorithms\etc\오늘의 일기.txt
    
# 작성 내역이 없는 경우
>>> writer.export_diary(save_path='./', name='오늘의 일기.txt')
저장할 다이어리 기록이 없습니다.
```

#### Schedule: 스케줄 기록 저장

```python
>>> writer.export_schedule(save_path='./', name='가까운 일정.txt')
일정이 저장되었습니다.	c:\Users\iloveslowfood\Documents\GitHub\Algorithms\etc\가까운 일정.txt
    
# 작성 내역이 없는 경우
>>> writer.export_schedule(save_path='./', name='가까운 일정.txt')
저장할 일정 기록이 없습니다.
```

#### 다이어리와 스케줄 일괄 저장

```python
>>> writer.export_all(save_path='./', name='지형이의 기록.txt')
다이어리가 저장되었습니다.	c:\Users\iloveslowfood\Documents\GitHub\Algorithms\etc\지형이의 기록_diary.txt
일정이 저장되었습니다.	c:\Users\iloveslowfood\Documents\GitHub\Algorithms\etc\지형이의 기록_schedule.txt
 
# 작성 내역이 모두 없는 경우
>>> writer.export_all(save_path='./', name='지형이의 기록.txt')
저장할 다이어리 기록이 없습니다.
저장할 일정 기록이 없습니다.

# 어느 하나만 작성 내역이 있는 경우
>>> writer.export_all(save_path='./', name='지형이의 기록.txt')
다이어리가 저장되었습니다.	c:\Users\iloveslowfood\Documents\GitHub\Algorithms\etc\지형이의 기록_diary.txt
저장할 일정 기록이 없습니다.
```

### Remove: 메모 삭제하기

* `remove_record` 메서드를 호출하여 기록된 메모를 삭제합니다.
* 메서드 내부에서 `input` 함수를 활용하여 메모 삭제 가이드라인을 제공합니다.
* 글번호를 입력받으면, 사용자가 내용을 간단히 확인하고 삭제를 최종 결정할 수 있도록 메모의 일부 내용(20자 이내)을 출력합니다.
* 삭제할 것인지 되물어보며, 승낙할 경우 삭제가 진행됩니다.

```python
>>> writer.remove_record()
삭제하실 글의 글 번호를 입력해주세요.
>>> 1
글 번호 1
작성자 고지형
작성 시간 2020-12-20 19:47:15
날짜: 2020-12-22
시간: 오후 2시 ...
삭제하시겠습니까?[y/n]
>>> y
삭제되었습니다.

# 글 번호 1에 해당되는 스케줄이 삭제되었음을 확인할 수 있음
>>> writer.show_schedule()
[작성하신 일정 내역입니다]

글 번호: 3
작성자: 고지형
작성 시간: 2020-12-20 19:49:28
날짜: 2020-12-23
시간: 오 ...
내용: AI 세미나
```

### 작성자명 변경하기

* `change_author` 메서드를 호출하여 메모의 작성자명을 수정할 수 있습니다.

```python
>>> writer.change_author(author='KOJIHYEONG')
작성자 이름이 변경되었습니다
고지형 => KOJIHYEONG
```

