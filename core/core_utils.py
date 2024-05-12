import cv2


class CoreUtils:
    @staticmethod
    def gridTransformation(image):
        # Placeholder function for Grid Transformation
        # Implement the grid transformation operation here
        if image is not None:
            return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return None

    @staticmethod
    def binaryTransformation(image):
        # Placeholder function for Binary Transformation
        # Implement the binary transformation operation here
        if image is not None:
            _, image = cv2.threshold(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
            return image
        return None

    @staticmethod
    def rotateImage(image):
        # Placeholder function for Rotate Image
        # Implement the image rotation operation here
        if image is not None:
            return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        return None

    @staticmethod
    def cropImage(image):
        # Placeholder function for Crop Image
        # Implement the image cropping operation here
        if image is not None:
            height, width, _ = image.shape
            return image[height // 4: height // 2, width // 4: width // 2]
        return None

    @staticmethod
    def zoomImage(image):
        # Placeholder function for Zoom Image
        # Implement the image zooming operation here
        if image is not None:
            return cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
        return None

    @staticmethod
    def colorSpaceTransform(image):
        # Placeholder function for Color Space Transformation
        # Implement the color space transformation operation here
        if image is not None:
            return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        return None

    @staticmethod
    def histogramStretching(image):
        # Placeholder function for Histogram Stretching
        # Implement the histogram stretching operation here
        if image is not None:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            return cv2.equalizeHist(image)
        return None
