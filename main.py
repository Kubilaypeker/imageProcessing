from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout, \
    QWidget, QScrollArea
from PyQt5.QtGui import QPixmap, QImage, QTransform
from PyQt5.QtCore import Qt
import sys

from core.core_utils import CoreUtils


class ImageApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Processing App')

        self.image = None
        self.originalImage = None
        self.imageLabel = QLabel(self)
        self.imageLabel.setAlignment(Qt.AlignCenter)

        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setWidget(self.imageLabel)

        loadButton = QPushButton('Load Image', self)
        loadButton.clicked.connect(self.loadImage)

        resetButton = QPushButton('Reset Image', self)
        resetButton.clicked.connect(self.resetImage)

        saveButton = QPushButton("Save Image")
        saveButton.clicked.connect(self.saveImage)

        grayButton = QPushButton('Gray Scale', self)
        grayButton.clicked.connect(self.grayScale)

        binaryButton = QPushButton('Binary Threshold', self)
        binaryButton.clicked.connect(self.binaryThreshold)

        rotateButton = QPushButton('Rotate', self)
        rotateButton.clicked.connect(self.rotateImage)

        cropButton = QPushButton('Crop', self)
        cropButton.clicked.connect(self.cropImage)

        zoomButton = QPushButton('Zoom', self)
        zoomButton.clicked.connect(self.zoomImage)

        unzoomButton = QPushButton('Unzoom', self)
        unzoomButton.clicked.connect(self.unzoomImage)

        hsvButton = QPushButton('RGB to HSV', self)
        hsvButton.clicked.connect(self.rgbToHsv)

        histButton = QPushButton('Histogram', self)
        histButton.clicked.connect(self.histogram)

        stretchButton = QPushButton('Stretch Histogram', self)
        stretchButton.clicked.connect(self.stretchHistogram)

        addImageButton = QPushButton('Add Images', self)
        addImageButton.clicked.connect(self.addImages)

        sliceImageInHalfButton = QPushButton("Slice Image in Half")
        sliceImageInHalfButton.clicked.connect(self.sliceImageInHalf)

        contrastButton = QPushButton('Increase Contrast', self)
        contrastButton.clicked.connect(self.increaseContrast)

        meanConvButton = QPushButton('Mean Convolution', self)
        meanConvButton.clicked.connect(self.meanConvolution)

        prewittButton = QPushButton('Prewitt Edge Detection', self)
        prewittButton.clicked.connect(self.prewittEdgeDetection)

        saltPepperButton = QPushButton('Add Salt & Pepper Noise', self)
        saltPepperButton.clicked.connect(self.addSaltPepperNoise)

        meanFilterButton = QPushButton('Mean Filter', self)
        meanFilterButton.clicked.connect(self.meanFilter)

        medianFilterButton = QPushButton('Median Filter', self)
        medianFilterButton.clicked.connect(self.medianFilter)

        unsharpButton = QPushButton('Unsharp Mask', self)
        unsharpButton.clicked.connect(self.unsharpMask)

        dilateButton = QPushButton('Dilate', self)
        dilateButton.clicked.connect(self.dilate)

        erodeButton = QPushButton('Erode', self)
        erodeButton.clicked.connect(self.erode)

        openMorphButton = QPushButton('Open Morph', self)
        openMorphButton.clicked.connect(self.openMorph)

        closeMorphButton = QPushButton('Close Morph', self)
        closeMorphButton.clicked.connect(self.closeMorph)

        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(loadButton)
        buttonLayout.addWidget(resetButton)
        buttonLayout.addWidget(saveButton)
        buttonLayout.addWidget(grayButton)
        buttonLayout.addWidget(binaryButton)
        buttonLayout.addWidget(rotateButton)
        buttonLayout.addWidget(cropButton)
        buttonLayout.addWidget(zoomButton)
        buttonLayout.addWidget(unzoomButton)
        buttonLayout.addWidget(hsvButton)
        buttonLayout.addWidget(histButton)
        buttonLayout.addWidget(stretchButton)
        buttonLayout.addWidget(addImageButton)
        buttonLayout.addWidget(sliceImageInHalfButton)
        buttonLayout.addWidget(contrastButton)
        buttonLayout.addWidget(meanConvButton)
        buttonLayout.addWidget(prewittButton)
        buttonLayout.addWidget(saltPepperButton)
        buttonLayout.addWidget(meanFilterButton)
        buttonLayout.addWidget(medianFilterButton)
        buttonLayout.addWidget(unsharpButton)
        buttonLayout.addWidget(dilateButton)
        buttonLayout.addWidget(erodeButton)
        buttonLayout.addWidget(openMorphButton)
        buttonLayout.addWidget(closeMorphButton)
        buttonLayout.addStretch(1)

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(scrollArea)
        mainLayout.addLayout(buttonLayout)

        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)
        self.setGeometry(100, 100, 800, 600)

    def loadImage(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Load Image", "", "Images (*.png *.jpg *.bmp)", options=options)
        if fileName:
            self.image = QImage(fileName)
            self.originalImage = self.image.copy()
            self.imageLabel.setPixmap(
                QPixmap.fromImage(self.image).scaled(self.imageLabel.width(), self.imageLabel.height(),
                                                     Qt.KeepAspectRatio))

    def grayScale(self):
        if hasattr(self, 'image'):
            self.image = CoreUtils.greyTransformation(self.image)
            self.imageLabel.setPixmap(
                QPixmap.fromImage(self.image).scaled(self.imageLabel.width(), self.imageLabel.height(),
                                                     Qt.KeepAspectRatio))

    def binaryThreshold(self):
        if hasattr(self, 'image'):
            self.image = CoreUtils.binaryTransformation(self.image)
            self.imageLabel.setPixmap(
                QPixmap.fromImage(self.image).scaled(self.imageLabel.width(), self.imageLabel.height(),
                                                     Qt.KeepAspectRatio))

    def rotateImage(self):
        if hasattr(self, 'image'):
            transform = QTransform()
            transform.rotate(90)
            self.image = self.image.transformed(transform)
            self.imageLabel.setPixmap(
                QPixmap.fromImage(self.image).scaled(self.imageLabel.width(), self.imageLabel.height(),
                                                     Qt.KeepAspectRatio))

    def cropImage(self):
        if hasattr(self, 'image'):
            self.image = CoreUtils.cropImage(self.image)
            self.imageLabel.setPixmap(
                QPixmap.fromImage(self.image).scaled(self.imageLabel.width(), self.imageLabel.height(),
                                                     Qt.KeepAspectRatio))

    def zoomImage(self):
        if hasattr(self, 'image'):
            self.zoomFactor = 2
            newWidth = self.image.width() * self.zoomFactor
            newHeight = self.image.height() * self.zoomFactor
            self.imageLabel.setPixmap(QPixmap.fromImage(self.image).scaled(newWidth, newHeight, Qt.KeepAspectRatio))

    def unzoomImage(self):
        if hasattr(self, 'image'):
            minZoomFactor = 0.5
            if self.zoomFactor / 2 >= minZoomFactor:
                self.zoomFactor /= 2
                newWidth = int(self.image.width() * self.zoomFactor)
                newHeight = int(self.image.height() * self.zoomFactor)
                self.imageLabel.setPixmap(QPixmap.fromImage(self.image).scaled(newWidth, newHeight, Qt.KeepAspectRatio))

    def rgbToHsv(self):
        if hasattr(self, 'image'):
            self.image = CoreUtils.rgbToHsv(self.image)
            self.imageLabel.setPixmap(
                QPixmap.fromImage(self.image).scaled(self.imageLabel.width(), self.imageLabel.height(),
                                                     Qt.KeepAspectRatio))

    def resetImage(self):
        if self.originalImage:
            self.image = self.originalImage.copy()  # Restore the original image
            self.imageLabel.setPixmap(
                QPixmap.fromImage(self.image).scaled(self.imageLabel.width(), self.imageLabel.height(),
                                                     Qt.KeepAspectRatio))

    def histogram(self):
        if hasattr(self, 'image'):
            self.image, histogram_image = CoreUtils.histogram(self.image)
            self.imageLabel.setPixmap(
                QPixmap.fromImage(histogram_image).scaled(self.imageLabel.width(), self.imageLabel.height(),
                                                          Qt.KeepAspectRatio))

    def stretchHistogram(self):
        if hasattr(self, 'image'):
            self.image = CoreUtils.histogramStretching(self.image)
            self.imageLabel.setPixmap(
                QPixmap.fromImage(self.image).scaled(self.imageLabel.width(), self.imageLabel.height(),
                                                     Qt.KeepAspectRatio))

    def addImages(self):
        if hasattr(self, 'image'):
            options = QFileDialog.Options()
            fileName, _ = QFileDialog.getOpenFileName(self, "Load Second Image", "", "Images (*.png *.jpg *.bmp)",
                                                      options=options)
            if fileName:
                secondImage = QImage(fileName)
                max_width = self.image.width() + secondImage.width()
                max_height = max(self.image.height(), secondImage.height())
                resultImage = QImage(max_width, max_height, QImage.Format_RGB32)
                resultImage.fill(Qt.white)

                # Paste the original image on the left side
                for x in range(self.image.width()):
                    for y in range(self.image.height()):
                        resultImage.setPixelColor(x, y, self.image.pixelColor(x, y))

                # Paste the second image on the right side
                for x in range(secondImage.width()):
                    for y in range(secondImage.height()):
                        resultImage.setPixelColor(x + self.image.width(), y, secondImage.pixelColor(x, y))

                self.image = resultImage
                self.imageLabel.setPixmap(
                    QPixmap.fromImage(self.image).scaled(self.imageLabel.width(), self.imageLabel.height(),
                                                         Qt.KeepAspectRatio))

    def increaseContrast(self):
        if hasattr(self, 'image'):
            self.image = CoreUtils.increaseContrast(self.image)
            self.imageLabel.setPixmap(
                QPixmap.fromImage(self.image).scaled(self.imageLabel.width(), self.imageLabel.height(),
                                                     Qt.KeepAspectRatio))

    def meanConvolution(self):
        if hasattr(self, 'image'):
            self.image = CoreUtils.meanConvultion(self.image)
            self.imageLabel.setPixmap(
                QPixmap.fromImage(self.image).scaled(self.imageLabel.width(), self.imageLabel.height(),
                                                     Qt.KeepAspectRatio))

    def prewittEdgeDetection(self):
        if hasattr(self, 'image'):
            self.image = CoreUtils.prewittEdgeDetection(self.image)
            self.imageLabel.setPixmap(
                QPixmap.fromImage(self.image).scaled(self.imageLabel.width(), self.imageLabel.height(),
                                                     Qt.KeepAspectRatio))

    def addSaltPepperNoise(self):
        if hasattr(self, 'image'):
            self.image = CoreUtils.addSaltAndPepperNoise(self.image)
            self.imageLabel.setPixmap(
                QPixmap.fromImage(self.image).scaled(self.imageLabel.width(), self.imageLabel.height(),
                                                     Qt.KeepAspectRatio))

    def meanFilter(self):
        if hasattr(self, 'image'):
            self.image = CoreUtils.meanFilter(self.image)
            self.imageLabel.setPixmap(
                QPixmap.fromImage(self.image).scaled(self.imageLabel.width(), self.imageLabel.height(),
                                                     Qt.KeepAspectRatio))

    def medianFilter(self):
        if hasattr(self, 'image'):
            self.image = CoreUtils.medianFilter(self.image)
            self.imageLabel.setPixmap(
                QPixmap.fromImage(self.image).scaled(self.imageLabel.width(), self.imageLabel.height(),
                                                     Qt.KeepAspectRatio))

    def unsharpMask(self):
        if hasattr(self, 'image'):
            self.image = CoreUtils.unsharpMask(self.image)
            self.imageLabel.setPixmap(
                QPixmap.fromImage(self.image).scaled(self.imageLabel.width(), self.imageLabel.height(),
                                                     Qt.KeepAspectRatio))

    def dilate(self):
        if hasattr(self, 'image'):
            self.image = CoreUtils.dilate(self.image)
            self.imageLabel.setPixmap(
                QPixmap.fromImage(self.image).scaled(self.imageLabel.width(), self.imageLabel.height(),
                                                     Qt.KeepAspectRatio))

    def erode(self):
        if hasattr(self, 'image'):
            self.image = CoreUtils.erode(self.image)
            self.imageLabel.setPixmap(
                QPixmap.fromImage(self.image).scaled(self.imageLabel.width(), self.imageLabel.height(),
                                                     Qt.KeepAspectRatio))

    def openMorph(self):
        self.erode()
        self.dilate()

    def closeMorph(self):
        self.dilate()
        self.erode()

    def sliceImageInHalf(self):
        if hasattr(self, 'image'):
            left_half, right_half = CoreUtils.sliceImageInHalf(self.image)
            left_half_pixmap = QPixmap.fromImage(left_half)
            right_half_pixmap = QPixmap.fromImage(right_half)
            self.imageLabel.setPixmap(left_half_pixmap)

    def saveImage(self):
        if self.image:
            options = QFileDialog.Options()
            fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                      "Images (*.png *.xpm *.jpg *.jpeg *.bmp);;All Files (*)",
                                                      options=options)
            if fileName:
                self.image.save(fileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageApp()
    ex.show()
    sys.exit(app.exec_())
