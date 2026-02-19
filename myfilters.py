import math
from ufo2ft.filters import BaseFilter, BaseIFilter


class DumpAnchors(BaseFilter):
    def set_context(self, font, glyphSet):
        return super().set_context(font, glyphSet)

    def filter(self, glyph):
        glyph.clearAnchors()
        return True



