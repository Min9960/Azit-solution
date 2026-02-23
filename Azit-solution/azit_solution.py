from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, \
    QLabel, QLineEdit, QPushButton, QMessageBox
from azit_ser import DB, DB_CONFIG

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("자원 관리")
        self.db = DB(**DB_CONFIG)

        central = QWidget()
        self.setCentralWidget(central)
        vbox = QVBoxLayout(central)

        # 입력 필드
        form_box = QHBoxLayout()

        self.input_name = QLineEdit()
        self.input_carl = QLineEdit()
        self.input_cars = QLineEdit()
        self.input_q = QLineEdit()
        self.input_p = QLineEdit()
        self.input_lot = QLineEdit()
        self.input_log = QLineEdit()

        self.btn_add = QPushButton("추가")
        self.btn_add.clicked.connect(self.add_asset)

        form_box.addWidget(QLabel("제품명"))
        form_box.addWidget(self.input_name)
        form_box.addWidget(QLabel("대분류"))
        form_box.addWidget(self.input_carl)
        form_box.addWidget(QLabel("소분류"))
        form_box.addWidget(self.input_cars)
        form_box.addWidget(QLabel("갯수"))
        form_box.addWidget(self.input_q)
        form_box.addWidget(QLabel("가격"))
        form_box.addWidget(self.input_p)
        form_box.addWidget(QLabel("로트"))
        form_box.addWidget(self.input_lot)
        form_box.addWidget(QLabel("로그"))
        form_box.addWidget(self.input_log)
        form_box.addWidget(self.btn_add)

        # 테이블
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(
            ["ID", "제품명", "대분류", "소분류", "갯수", "가격", "로트", "로그"]
        )
        self.table.verticalHeader().setVisible(False)

        vbox.addLayout(form_box)
        vbox.addWidget(self.table)

        self.load_assets()

    def load_assets(self):
        rows = self.db.fetch_assets()  # 🔥 assets용 함수로 변경
        self.table.setRowCount(len(rows))
        for r, row in enumerate(rows):
            for c, value in enumerate(row):
                self.table.setItem(r, c, QTableWidgetItem(str(value)))
        self.table.resizeColumnsToContents()

    def add_asset(self):
        name = self.input_name.text().strip()
        carl = self.input_carl.text().strip()
        cars = self.input_cars.text().strip()
        q = self.input_q.text().strip()
        p = self.input_p.text().strip()
        lot = self.input_lot.text().strip()
        log = self.input_log.text().strip()
        if not name:
            QMessageBox.warning(self, "오류", "제품명을 입력하세요.")
            return
        self.db.insert_asset(name, carl, cars, q, p, lot, log)
        self.load_assets()