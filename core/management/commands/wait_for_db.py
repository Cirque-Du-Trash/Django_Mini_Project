import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

class Command(BaseCommand):
    """Django 명령어로 DB 연결을 대기하는 커스텀 커맨드"""

    def handle(self, *args, **options):
        self.stdout.write('데이터베이스 연결을 기다리는 중...')
        db_conn = None
        attempts = 0

        while not db_conn and attempts < 10:
            try:
                db_conn = connections['default']
                db_conn.cursor()  # 연결 테스트
                self.stdout.write(self.style.SUCCESS('데이터베이스에 성공적으로 연결되었습니다!'))
            except OperationalError:
                attempts += 1
                self.stdout.write(f'데이터베이스 연결 재시도 ({attempts}/10)')
                time.sleep(1)

        if not db_conn:
            self.stdout.write(self.style.ERROR('데이터베이스 연결에 실패했습니다.'))