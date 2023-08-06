# FDRParser

FDRParser packaged library is a Python library required to access the modules included in teh FDRParser script. The script is used to read binary data from an SD card, which is sorted and graphed utilizing a user interface.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install FDRParser.

```bash
pip install FDRParser
```
### Troubleshooting
Setuptools is typically included with Linux, macOS, and Windows installers. If it is not, you can install it by running

```bash
pip install setuptools
```

or 

```bash
sudo pip install setuptools
```

## Usage

In order to specify the data which is to be read, specify the file name or location under fname. Ensure the name is in quotations. Depending on the file location, this name could be long (ex "C:\\Users\Username\Downloads\.vscode\FDRParser\Block_0_.FDR") or it could be short("Block_0_.FDR) if the file is in the same location as the source code.

```python
import math
import numpy as np
import platform
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

#specify file name or location
fname="BLOCK_0_Example.FDR"
```

## License
[MIT](https://choosealicense.com/licenses/mit/)