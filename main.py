import sys

import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QFileDialog, \
    QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap, QImage

from PyQt5.QtCore import Qt
from core.core_utils import CoreUtils


class ImageProcessingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Processing Application')
        self.setGeometry(100, 100, 800, 600)

        main_layout = QHBoxLayout()

        # Left side: Image display
        self.image_label = QLabel()
        main_layout.addWidget(self.image_label)

        # Right side: Feature buttons
        feature_layout = QVBoxLayout()

        # Upload Photo Section
        upload_layout = QHBoxLayout()
        self.upload_label = QLabel('No photo uploaded')
        upload_button = QPushButton('Upload Photo')
        upload_button.clicked.connect(self.uploadPhoto)
        upload_layout.addWidget(self.upload_label)
        upload_layout.addWidget(upload_button)
        feature_layout.addLayout(upload_layout)

        # Buttons for Image Processing Operations
        btn_grid_transform = QPushButton('Grid Transformation')
        btn_grid_transform.clicked.connect(self.gridTransformation)
        feature_layout.addWidget(btn_grid_transform)

        btn_binary_transform = QPushButton('Binary Transformation')
        btn_binary_transform.clicked.connect(self.binaryTransformation)
        feature_layout.addWidget(btn_binary_transform)

        btn_rotate_image = QPushButton('Rotate Image')
        btn_rotate_image.clicked.connect(self.rotateImage)
        feature_layout.addWidget(btn_rotate_image)

        btn_crop_image = QPushButton('Crop Image')
        btn_crop_image.clicked.connect(self.cropImage)
        feature_layout.addWidget(btn_crop_image)

        btn_zoom_image = QPushButton('Zoom In/Out')
        btn_zoom_image.clicked.connect(self.zoomImage)
        feature_layout.addWidget(btn_zoom_image)

        btn_color_space_transform = QPushButton('Color Space Transformation')
        btn_color_space_transform.clicked.connect(self.colorSpaceTransform)
        feature_layout.addWidget(btn_color_space_transform)

        btn_histogram_stretching = QPushButton('Histogram Stretching')
        btn_histogram_stretching.clicked.connect(self.histogramStretching)
        feature_layout.addWidget(btn_histogram_stretching)

        feature_layout.addStretch()  # Add stretchable space at the end to push buttons to the top
        main_layout.addLayout(feature_layout)

        self.setLayout(main_layout)
        self.show()

    def uploadPhoto(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)",
                                                   options=options)
        if file_name:
            self.image = cv2.imread(file_name)
            self.displayImage(self.image)
            self.upload_label.setText('Photo uploaded')

    def displayImage(self, image):
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        qImg = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg.rgbSwapped())
        self.image_label.setPixmap(pixmap)

    def displayProcessedImage(self, image):
        height, width = image.shape
        bytes_per_line = 3 * width
        qImg = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg.rgbSwapped())
        self.image_label.setPixmap(pixmap)

    def gridTransformation(self):
        if hasattr(self, 'image'):
            self.image = CoreUtils.gridTransformation(self.image)
            if self.image is not None:
                self.displayProcessedImage(self.image)

    def binaryTransformation(self):
        if hasattr(self, 'image'):
            self.image = CoreUtils.binaryTransformation(self.image)
            if self.image is not None:
                self.displayProcessedImage(self.image)

    def rotateImage(self):
        if hasattr(self, 'image'):
            self.image = CoreUtils.rotateImage(self.image)
            if self.image is not None:
                self.displayImage(self.image)

    def cropImage(self):
        if hasattr(self, 'image'):
            self.image = CoreUtils.cropImage(self.image)
            if self.image is not None:
                self.displayImage(self.image)

    def zoomImage(self):
        if hasattr(self, 'image'):
            self.image = CoreUtils.zoomImage(self.image)
            if self.image is not None:
                self.displayProcessedImage(self.image)

    def colorSpaceTransform(self):
        if hasattr(self, 'image'):
            self.image = CoreUtils.colorSpaceTransform(self.image)
            if self.image is not None:
                self.displayProcessedImage(self.image)

    def histogramStretching(self):
        if hasattr(self, 'image'):
            self.image = CoreUtils.histogramStretching(self.image)
            if self.image is not None:
                self.displayProcessedImage(self.image)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageProcessingApp()
    sys.exit(app.exec_())
