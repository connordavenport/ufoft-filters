import math
from ufo2ft.filters import BaseFilter, BaseIFilter
import feaPyFoFum as feapy
import logging
from ufo2ft.util import _LazyFontName

logger = logging.getLogger(__name__)

## Dump anchors when compiling font
class DumpAnchors(BaseFilter):
    def set_context(self, font, glyphSet):
        return super().set_context(font, glyphSet)

    def filter(self, glyph):
        glyph.clearAnchors()
        return True
## --------------------------------


## Compile font features with feaPy 
FEAPY_LIB_KEY = "com.typesupply.feaPyFoFum.compileFeatures"

class FeaPyFoFilter(BaseFilter):

    def __call__(self, font, glyphSet=None):
        self.fontName = _LazyFontName(font)
        self.set_context(font, glyphSet)
        didCompile = self.compile_features()
        if didCompile:
            return True

    def compile_features(self):
        parsed = False
        font = self.context.font
        if FEAPY_LIB_KEY in font.lib.keys():
            logger.info(f"Running {self.name} on {self.fontName}")
            compiled = feapy.compileFeatures(font.features.text, font, verbose=True, compileReferencedFiles=True)
            font.features.text = compiled
            parsed = True
            logger.info(f"Compiled features with feaPyFoFum on {self.fontName}")
        return parsed
## --------------------------------