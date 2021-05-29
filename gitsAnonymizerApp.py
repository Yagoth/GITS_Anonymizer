# Created May 28, 2021 by Ko
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from constants import Constants


class GITSAnonymizerApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = Constants.APP_NAME.value
        self.left = 100
        self.top = 100
        self.width = 350
        self.height = 600

        # Set up assets
        self.h1Font = QFont()
        self.h1Font.setStyleHint(QFont.SansSerif)
        self.h1Font.setPixelSize(20)

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)

        # Make the background white
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('white'))
        self.setPalette(palette)

        # Make the window icon a laughing man
        self.setWindowIcon(QIcon(Constants.LAUGHING_MAN_FILE_LOCATION.value))

        self.loadLandingPage()
        self.show()

    def loadLandingPage(self):
        # Items will be laid out vertical on the page
        layout = QVBoxLayout()
        layout.setSpacing(10)

        # Set up a title label
        titleLabel = QLabel(self.title, self)
        titleLabel.setFont(self.h1Font)
        titleLabel.setWordWrap(True)
        titleLabel.setAlignment(Qt.AlignCenter)

        # Set up the laughing man image
        laughingManLabel = QLabel(self)
        LAUGHING_MAN_PIXMAP = QPixmap(Constants.LAUGHING_MAN_FILE_LOCATION.value)
        laughingManLabel.setPixmap(LAUGHING_MAN_PIXMAP)
        laughingManLabel.setAlignment(Qt.AlignCenter)

        # Set up the upload button
        uploadNewButton = QPushButton(Constants.UPLOAD_NEW.value, self)
        uploadNewButton.setToolTip("Upload a new image or video")
        uploadNewButton.setStyleSheet(
            "background-color: " + Constants.PRIMARY_BLUE.value + ";"
            "border: none;"
            "color: white;"
            "border-radius: 10px;"
            "text-align: center;"
            "font-size: 16px;"
            "padding: 10px 10px;"
        )

        # Add all of the above to the layout
        layout.addWidget(titleLabel)
        layout.addWidget(laughingManLabel)
        layout.addWidget(uploadNewButton)

        # Put the layout in a widget; make the widget the central widget
        widget = QWidget()
        widget.setLayout(layout)
        widget.setContentsMargins(int(self.width / 5), int(self.height / 5), int(self.width / 5), int(self.height / 4))
        self.setCentralWidget(widget)
