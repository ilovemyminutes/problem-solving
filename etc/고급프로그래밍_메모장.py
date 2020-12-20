import os
from datetime import datetime
from collections import OrderedDict


class MemoWriter:
    def __init__(self, author: str):
        self.__author = author
        self.__log = list()
        self.__log_id = 0


    def write_diary(self):
        """다이어리를 작성하는 함수"""
        DATE = "날짜: " + input("날짜 입력:")
        WEATHER = "날씨: " + input("날씨 입력:")
        TITLE = "제목: " + input("제목 입력:")
        CONTENTS = "내용: " + input("내용 입력:")

        diary = self.__aggregate_text(DATE, WEATHER, TITLE, CONTENTS)
        log_time = self.__update_log("diary", diary)
        print(f"[다이어리가 기록되었습니다]\n작성 시간:{log_time}\n작성자:{self.__author}\n")
        print(diary)


    def write_schedule(self):
        """일정을 작성하는 함수"""
        DATE = "날짜: " + input("날짜 입력:")
        TIME = "시간: " + input("시간 입력:")
        CONTENTS = "내용: " + input("내용 입력:")

        schedule = self.__aggregate_text(DATE, TIME, CONTENTS)
        log_time = self.__update_log("schedule", schedule)
        print(f"[일정이 기록되었습니다]\n작성 시간:{log_time}\n작성자:{self.__author}\n")
        print(schedule)


    def show_diary(self):
        """지금까지 작성한 다이어리 내용을 출력하는 함수"""
        diary_list = self.__get_memo("diary")
        if diary_list:
            result = self.__merge_contents(diary_list)
            print("[작성하신 다이어리 내역입니다]\n")
            print(result)
        else:
            print("[작성하신 일정 내역입니다]\n")
            print("작성 내역 없음")


    def show_schedule(self):
        """지금까지 기록한 일정 내용을 출력하는 함수"""
        schedule_list = self.__get_memo("schedule")
        if schedule_list:
            result = self.__merge_contents(schedule_list)
            print("[작성하신 일정 내역입니다]\n")
            print(result)
        else:
            print("[작성하신 일정 내역입니다]\n")
            print("작성 내역 없음")


    def export_diary(self, save_path: str, name: str):
        """지금까지 작성한 다이어리를 저장하는 함수
        작성 내역이 없는 경우 저장되지 않음"""
        diary_list = self.__get_memo("diary")
        if diary_list:
            result = self.__merge_contents(diary_list)
            f = open(os.path.join(save_path, name), "w", encoding="utf-8")
            f.write(result)
            f.close()
            print(f"다이어리가 저장되었습니다.\t{os.path.abspath(os.path.join(save_path, name))}")
        else:
            print("저장할 다이어리 기록이 없습니다.")


    def export_schedule(self, save_path: str, name: str):
        """지금까지 작성한 스케줄을 저장하는 함수
        작성 내역이 없는 경우 저장되지 않음"""
        schedule_list = self.__get_memo("schedule")
        if schedule_list:
            result = self.__merge_contents(schedule_list)
            f = open(os.path.join(save_path, name), "w", encoding="utf-8")
            f.write(result)
            f.close()
            print(f"일정이 저장되었습니다.\t{os.path.abspath(os.path.join(save_path, name))}")
        else:
            print("저장할 일정 기록이 없습니다.")


    def export_all(self, save_path: str, name: str):
        """지금까지 작성한 다이어리, 스케줄을 저장하는 함수
        작성 내역이 없는 경우 저장되지 않음"""
        name, txt = name.split(".txt")[0], ".txt"
        diary_name = name + "_diary" + txt
        schedule_name = name + "_schedule" + txt
        self.export_diary(save_path, diary_name)
        self.export_schedule(save_path, schedule_name)


    def remove_record(self):
        idx = int(input("삭제하실 글의 글 번호를 입력해주세요."))
        record = list(filter(lambda x: x["id"] == idx, self.__log))[0]
        print("글 번호", idx)
        print("작성자", record["author"])
        print("작성 시간", record["time"])
        if len(record["contents"]) > 20:
            print(record["contents"][:20], "...")
        else:
            print(record["contents"])
        decision = input("\n삭제하시겠습니까?[y/n]")
        if decision == "y":
            self.__log.remove(record)
            print("삭제되었습니다.")


    def change_author(self, author: str):
        """작성자 이름을 변경하는 함수"""
        past_author = self.__author
        self.__author = author
        print("작성자 이름이 변경되었습니다")
        print(f"{past_author} => {self.__author}")


    def show_log(self):
        """작성 로그를 확인할 수 있는 함수"""
        print(self.__log)
        return self.__log


    @staticmethod
    def __aggregate_text(*args):
        """분할된 텍스트를 통합하는 함수"""
        result = ""
        for text in args:
            result += text + "\n"
        return result


    def __update_log(self, type_, contents):
        """로그를 업데이터하는 함수"""
        log_time = datetime.strftime(datetime.now(), format="%Y-%m-%d %H:%M:%S")
        self.__log.append(
            {
                "id": self.__log_id,
                "author": self.__author,
                "time": log_time,
                "type": type_,
                "contents": contents,
            }
        )
        self.__log_id += 1
        return log_time


    def __get_memo(self, type_: str):
        """메모 기록을 가져오는 함수"""
        result = list(filter(lambda x: x["type"] == type_, self.__log))
        return result


    def __merge_contents(self, contents_list: list) -> str:
        """작성한 글을 하나의 문자열로 병합한는 함수"""
        result = ""
        for idx, record in enumerate(contents_list):
            ID = "글 번호: " + str(record["id"])
            AUTHOR = "작성자: " + record["author"]
            TIME = "작성 시간: " + record["time"]
            CONTENTS = record["contents"]
            result += self.__aggregate_text(ID, AUTHOR, TIME, CONTENTS)
            if idx != len(contents_list) - 1:
                result += "\n"
        return result
