from PyQt5.QtGui import qRed, qGreen, qBlue, qRgb, qGray, QImage
from PyQt5.QtCore import Qt

import random


class CoreUtils:

    @staticmethod
    def greyTransformation(image):

        width = image.width()
        height = image.height()
        for x in range(width):
            for y in range(height):
                color = image.pixel(x, y)
                r = qRed(color)
                g = qGreen(color)
                b = qBlue(color)
                gray = int(0.299 * r + 0.587 * g + 0.114 * b)
                image.setPixel(x, y, qRgb(gray, gray, gray))
        return image

    @staticmethod
    def binaryTransformation(image):
        threshold = 128
        width = image.width()
        height = image.height()
        for x in range(width):
            for y in range(height):
                color = image.pixel(x, y)
                gray = qGray(color)
                binary = 255 if gray > threshold else 0
                image.setPixel(x, y, qRgb(binary, binary, binary))
        return image

    @staticmethod
    def rgbToHsv(image):
        width = image.width()
        height = image.height()
        for x in range(width):
            for y in range(height):
                color = image.pixel(x, y)
                r = qRed(color) / 255.0
                g = qGreen(color) / 255.0
                b = qBlue(color) / 255.0
                cmax = max(r, g, b)
                cmin = min(r, g, b)
                delta = cmax - cmin
                h = 0
                if delta != 0:
                    if cmax == r:
                        h = (60 * ((g - b) / delta) + 360) % 360
                    elif cmax == g:
                        h = (60 * ((b - r) / delta) + 120) % 360
                    else:
                        h = (60 * ((r - g) / delta) + 240) % 360
                s = 0 if cmax == 0 else (delta / cmax)
                v = cmax
                image.setPixel(x, y, qRgb(int(h * 255 / 360), int(s * 255), int(v * 255)))
        return image

    @staticmethod
    def cropImage(image):
        width = image.width()
        height = image.height()
        new_width = width // 2
        new_height = height // 2
        image = image.copy(0, 0, new_width, new_height)
        return image

    @staticmethod
    def histogram(image):
        width = image.width()
        height = image.height()
        histogram = [0] * 256
        for x in range(width):
            for y in range(height):
                color = image.pixel(x, y)
                gray = qGray(color)
                histogram[gray] += 1
        max_count = max(histogram)
        histogram_image = QImage(256, 256, QImage.Format_RGB32)
        histogram_image.fill(Qt.white)
        for i in range(256):
            height = histogram[i] * 256 / max_count
            for j in range(int(height)):
                histogram_image.setPixel(i, 255 - j, qRgb(0, 0, 0))
        return image, histogram_image

    @staticmethod
    def histogramStretching(image):
        width = image.width()
        height = image.height()
        min_gray = 255
        max_gray = 0
        for x in range(width):
            for y in range(height):
                gray = qGray(image.pixel(x, y))
                if gray < min_gray:
                    min_gray = gray
                if gray > max_gray:
                    max_gray = gray
        for x in range(width):
            for y in range(height):
                gray = qGray(image.pixel(x, y))
                stretched_gray = (gray - min_gray) * 255 / (max_gray - min_gray)
                stretched_gray = int(stretched_gray)
                image.setPixel(x, y, qRgb(stretched_gray, stretched_gray, stretched_gray))
        return image

    @staticmethod
    def increaseContrast(image):
        width = image.width()
        height = image.height()
        factor = 1.2
        for x in range(width):
            for y in range(height):
                color = image.pixel(x, y)
                r = min(max(int(qRed(color) * factor), 0), 255)
                g = min(max(int(qGreen(color) * factor), 0), 255)
                b = min(max(int(qBlue(color) * factor), 0), 255)
                image.setPixel(x, y, qRgb(r, g, b))
        return image

    @staticmethod
    def meanConvultion(image):
        width = image.width()
        height = image.height()
        resultImage = QImage(width, height, QImage.Format_RGB32)
        kernel = [
            [1 / 9, 1 / 9, 1 / 9],
            [1 / 9, 1 / 9, 1 / 9],
            [1 / 9, 1 / 9, 1 / 9]
        ]
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                r = 0
                g = 0
                b = 0
                for i in range(3):
                    for j in range(3):
                        color = image.pixel(x + i - 1, y + j - 1)
                        r += qRed(color) * kernel[i][j]
                        g += qGreen(color) * kernel[i][j]
                        b += qBlue(color) * kernel[i][j]
                resultImage.setPixel(x, y, qRgb(int(r), int(g), int(b)))

        return resultImage

    @staticmethod
    def prewittEdgeDetection(image):
        width = image.width()
        height = image.height()
        resultImage = QImage(width, height, QImage.Format_RGB32)
        kernelX = [
            [-1, 0, 1],
            [-1, 0, 1],
            [-1, 0, 1]
        ]
        kernelY = [
            [-1, -1, -1],
            [0, 0, 0],
            [1, 1, 1]
        ]
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                gx = 0
                gy = 0
                for i in range(3):
                    for j in range(3):
                        color = image.pixel(x + i - 1, y + j - 1)
                        gray = qGray(color)
                        gx += gray * kernelX[i][j]
                        gy += gray * kernelY[i][j]
                magnitude = min(int((gx ** 2 + gy ** 2) ** 0.5), 255)
                resultImage.setPixel(x, y, qRgb(magnitude, magnitude, magnitude))

        return resultImage

    @staticmethod
    def addSaltAndPepperNoise(image):
        width = image.width()
        height = image.height()
        noise_amount = 0.05
        for x in range(width):
            for y in range(height):
                rand = random.random()
                if rand < noise_amount:
                    image.setPixel(x, y, qRgb(0, 0, 0))
                elif rand > 1 - noise_amount:
                    image.setPixel(x, y, qRgb(255, 255, 255))

        return image

    @staticmethod
    def meanFilter(image):
        width = image.width()
        height = image.height()
        resultImage = QImage(width, height, QImage.Format_RGB32)
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                r = 0
                g = 0
                b = 0
                for i in range(3):
                    for j in range(3):
                        color = image.pixel(x + i - 1, y + j - 1)
                        r += qRed(color)
                        g += qGreen(color)
                        b += qBlue(color)
                r //= 9
                g //= 9
                b //= 9
                resultImage.setPixel(x, y, qRgb(r, g, b))
        return resultImage

    @staticmethod
    def medianFilter(image):
        width = image.width()
        height = image.height()
        resultImage = QImage(width, height, QImage.Format_RGB32)
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                pixels = []
                for i in range(3):
                    for j in range(3):
                        pixels.append(image.pixel(x + i - 1, y + j - 1))
                pixels.sort(key=lambda color: qGray(color))
                median_pixel = pixels[4]
                resultImage.setPixel(x, y, median_pixel)
        return resultImage

    @staticmethod
    def unsharpMask(image):
        width = image.width()
        height = image.height()
        blurredImage = QImage(width, height, QImage.Format_RGB32)
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                r = 0
                g = 0
                b = 0
                for i in range(3):
                    for j in range(3):
                        color = image.pixel(x + i - 1, y + j - 1)
                        r += qRed(color)
                        g += qGreen(color)
                        b += qBlue(color)
                r //= 9
                g //= 9
                b //= 9
                blurredImage.setPixel(x, y, qRgb(r, g, b))
        for x in range(width):
            for y in range(height):
                original = image.pixel(x, y)
                blurred = blurredImage.pixel(x, y)
                r = min(max(qRed(original) * 2 - qRed(blurred), 0), 255)
                g = min(max(qGreen(original) * 2 - qGreen(blurred), 0), 255)
                b = min(max(qBlue(original) * 2 - qBlue(blurred), 0), 255)
                image.setPixel(x, y, qRgb(r, g, b))
        return image

    @staticmethod
    def dilate(image):
        width = image.width()
        height = image.height()
        resultImage = QImage(width, height, QImage.Format_RGB32)
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                max_val = 0
                for i in range(3):
                    for j in range(3):
                        color = qGray(image.pixel(x + i - 1, y + j - 1))
                        if color > max_val:
                            max_val = color
                resultImage.setPixel(x, y, qRgb(max_val, max_val, max_val))
        return resultImage

    @staticmethod
    def erode(image):
        width = image.width()
        height = image.height()
        resultImage = QImage(width, height, QImage.Format_RGB32)
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                min_val = 255
                for i in range(3):
                    for j in range(3):
                        color = qGray(image.pixel(x + i - 1, y + j - 1))
                        if color < min_val:
                            min_val = color
                resultImage.setPixel(x, y, qRgb(min_val, min_val, min_val))
        return resultImage

    @staticmethod
    def sliceImageInHalf(image):
        width = image.width()
        height = image.height()
        left_half = QImage(width // 2, height, image.format())
        right_half = QImage(width // 2, height, image.format())

        for x in range(width // 2):
            for y in range(height):
                left_half.setPixel(x, y, image.pixel(x, y))
                right_half.setPixel(x, y, image.pixel(x + width // 2, y))

        return left_half, right_half
