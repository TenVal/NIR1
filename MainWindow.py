from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from Canvas import PlotCanvas
from in_file import ValueInFile


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('GUI.ui', self)
        self.setWindowTitle('Cancer')
        # self.setWindowState(Qt.WindowMaximized)
        self.lineEdit_l1.setPlaceholderText('0.0834')
        self.lineEdit_b.setPlaceholderText('5.85')
        self.lineEdit_d.setPlaceholderText('0.00873')
        self.lineEdit_e.setPlaceholderText('0.66')
        self.lineEdit_l3.setPlaceholderText('1.7')
        self.lineEdit_u.setPlaceholderText('10')
        self.lineEdit_days.setPlaceholderText('120')
        self.lineEdit_b_x.setPlaceholderText('0')
        self.lineEdit_b_y.setPlaceholderText('0')

        self.cancer_brain_1 = PlotCanvas(self, width=4.5, height=3)
        self.cancer_brain_1.move(20, 40)

        self.cancer_brain_2 = PlotCanvas(self, width=4.5, height=3)
        self.cancer_brain_2.move(460, 40)

        self.cancer_brain_3 = PlotCanvas(self, width=4.5, height=3)
        self.cancer_brain_3.move(20, 350)

        self.cancer_brain_4 = PlotCanvas(self, width=4.5, height=3)
        self.cancer_brain_4.move(460, 350)

        self.eq_cancer = PlotCanvas(self)
        self.eq_cancer.move(890, 40)
        toolbar_eq_cancer = NavigationToolbar(self.eq_cancer, self)
        toolbar_eq_cancer.resize(420, 30)
        toolbar_eq_cancer.move(890, 500)

        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_3.setMinimum(0)
        self.horizontalSlider_4.setMinimum(0)

        self.show()
        self.pushButton_calc.clicked.connect(self.on_clicked_calc)
        # self.horizontalSlider.sliderMoved.connect(self.on_slider_moved)
        # self.horizontalSlider_2.sliderMoved.connect(self.on_slider_moved_2)
        # self.horizontalSlider_3.sliderMoved.connect(self.on_slider_moved_3)
        # self.horizontalSlider_4.sliderMoved.connect(self.on_slider_moved_4)

        self.horizontalSlider.valueChanged.connect(self.on_slider_moved)
        self.horizontalSlider_2.valueChanged.connect(self.on_slider_moved_2)
        self.horizontalSlider_3.valueChanged.connect(self.on_slider_moved_3)
        self.horizontalSlider_4.valueChanged.connect(self.on_slider_moved_4)
        # self.pushButton_save.clicked.connect(self.on_clicked)

    def on_clicked_calc(self):
        """Create Graph of function"""
        try:
            l1 = float(self.lineEdit_l1.text())
        except ValueError:
            l1 = 0.0834
        try:
            b = float(self.lineEdit_b.text())
        except ValueError:
            b = 5.85
        try:
            d = float(self.lineEdit_d.text())
        except ValueError:
            d = 0.00873
        try:
            e = float(self.lineEdit_e.text())
        except ValueError:
            e = 0.66
        try:
            l3 = float(self.lineEdit_l3.text())
        except ValueError:
            l3 = 1.7
        try:
            u = float(self.lineEdit_u.text())
        except ValueError:
            u = 10
        try:
            days = float(self.lineEdit_days.text())
        except ValueError:
            days = 120

        self.horizontalSlider.setMaximum(days)
        self.horizontalSlider_2.setMaximum(days)
        self.horizontalSlider_3.setMaximum(days)
        self.horizontalSlider_4.setMaximum(days)

        check = self.checkBox.isChecked()
        values = self.eq_cancer.plot(check=check, l1=l1, b=b, d=d, e=e, l3=l3, u=u, days=days)
        in_file_v = ValueInFile(values)
        in_file_v.format_values()
        in_file_v.write_in()
        # file = open("values_cancer.txt", "r")
        # line_values = []
        # while True:
        #     line = file.readline()
        #     line = line.split("\t")
        #     line = [float(i) for i in line]
        #     line_values.append(line)
        #     if not line:
        #         break
        # file.close()

    def read_r_file(self, d):
        file = open("values_cancer.txt", "r")
        for i in range(d - 1):
            file.readline()
        line = file.readline()
        line = line.split("\t")
        r = [float(i) for i in line]
        file.close()

        return r[3]

    def get_x_y_r(self):
        try:
            x0 = float(self.lineEdit_b_x.text())
        except ValueError:
            x0 = 0
        try:
            y0 = float(self.lineEdit_b_y.text())
        except ValueError:
            y0 = 0
        if x0 * x0 / (65 * 65) + (y0 * y0) / (75 * 75) > 1:
            error = QMessageBox()
            error.setWindowTitle("Предупреждение")
            error.setText("Введенные координаты не подходят!")
            error.setInformativeText("Координаты выходят за границы рассматриваемой области мозга, "
                                     "пожалуйста, введите другие.")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            self.lineEdit_b_x.clear()
            self.lineEdit_b_y.clear()
            return[0, 0]
        else:
            return [x0, y0]

    def on_slider_moved(self):
        d = self.horizontalSlider.value()
        r = self.read_r_file(d)
        coordinates = self.get_x_y_r()
        self.label_sl_1.setText(str(d))

        self.cancer_brain_1.plot_sphere(r, coordinates[0], coordinates[1])

    def on_slider_moved_2(self):
        d = self.horizontalSlider_2.value()
        r = self.read_r_file(d)
        coordinates = self.get_x_y_r()
        self.label_sl_2.setText(str(d))

        self.cancer_brain_2.plot_sphere(r, coordinates[0], coordinates[1])

    def on_slider_moved_3(self):
        d = self.horizontalSlider_3.value()
        r = self.read_r_file(d)
        coordinates = self.get_x_y_r()
        self.label_sl_3.setText(str(d))

        self.cancer_brain_3.plot_sphere(r, coordinates[0], coordinates[1])

    def on_slider_moved_4(self):
        d = self.horizontalSlider_4.value()
        r = self.read_r_file(d)
        coordinates = self.get_x_y_r()
        self.label_sl_4.setText(str(d))

        self.cancer_brain_4.plot_sphere(r, coordinates[0], coordinates[1])
