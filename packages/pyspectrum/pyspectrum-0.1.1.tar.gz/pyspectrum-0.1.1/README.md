# pyspectrum
### a small, multi-use color library for python
### supports RGB, Hexadecimal, Decimal, CMYK and most web colors (`red`, `seagreen`, `yellow`)
## Quickstart
### Installation & Upgrading
Using `pip` to install is highly reccomended</br>

`pip install -U pyspectrum`</br>

Upgrade to the latest stable version</br>

`pip install -U --upgrade pyspectrum`</br>

### Example
```py
import pyspectrum
# init colors
c = pyspectrum.Colors()
# creating color classes out of values
redRGB = c.RGB(255, 0, 0)
redHex = c.Hexadecimal("#ff0000")
redCMYK = c.CMYK(0, 100, 100, 0)
# html/css color name
convertedRGB = c.from_name("red")
# converting values
convertedCMYK = redRGB.to_cmyk()
convertedHex = redRGB.to_hex()
# accessing tuples and printing
print(f"Red RGB tuple: {redRGB.to_tuple()}")
print(f"Red Hex code: {redHex.to_string()}")
print(f"Red CMYK tuple: {redCMYK.to_tuple()}")
## printing colored text from RGB 
# prints'This is red text' in a red color
print(c.color_text("This is red text", redRGB))
```



