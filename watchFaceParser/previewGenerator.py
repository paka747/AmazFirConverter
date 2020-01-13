from watchFaceParser.models.elements.watchFace import WatchFace


class PreviewGenerator:
    @staticmethod
    def createAnimation(descriptor, images, states):
        previewWatchFace = WatchFace(descriptor)
        for watchState in states:
            image = PreviewGenerator.createFrame(previewWatchFace, images, watchState)
            yield image


    @staticmethod
    def createImage(descriptor, images, state):
        previewWatchFace = WatchFace(descriptor)
        return PreviewGenerator.createFrame(previewWatchFace, images, state)


    @staticmethod
    def createFrame(watchFace, resources, state):
        from PIL import Image, ImageDraw

        graphics = Image.new('RGBA', (454, 454))
        watchFace.draw3(graphics, resources, state)
        return graphics
