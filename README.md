# ufoft-filters


### Current Filters

`DumpAnchors`: A convience filter to ignore anchors in a font before passing to fontmake

`FeaPyFoFilter`: Recompile your features using feaPyFoFum before compiling with fontmake *

** You must have the `com.typesupply.feaPyFoFum.compileFeatures` key set to `True` in your font lib.


### Installing

The easiest way to install the filters is to clone the repo and use pip to install in edit mode.


Installing feaPyFoFum:

```
git clone https://github.com/typesupply/feaPyFoFum.git

cd feaPyFoFum

pip3 install -e .

```

Installing filters:
```
git clone https://github.com/connordavenport/ufoft-filters.git

cd ufoft-filters

pip3 install -e .

```


### Usage

`fontmake --filter "myfilters::FeaPyFoFilter(pre=True)" -o otf -u ~/Desktop/my_font.ufo`