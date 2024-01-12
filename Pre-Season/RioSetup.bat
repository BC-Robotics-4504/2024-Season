:: ------------------------------------------------------
:: REFERENCES:
:: https://github.com/robotpy/robotpy-meta
:: https://robotpy.readthedocs.io/en/stable/install/computer.html
:: ------------------------------------------------------
:: Install robotpy in native python distribution
:: ------------------------------------------------------
python -m pip install --upgrade pip
python -m pip install -U robotpy[all]
:: ------------------------------------------------------
:: Download and install python distribution onto roboRIO
:: ------------------------------------------------------
python -m pip install -U certifi
python -m robotpy_installer download-python --use-certifi
py -3 -m robotpy_installer install-python
:: ------------------------------------------------------
:: Download and install robotpy
:: ------------------------------------------------------
py -3 -m robotpy_installer download robotpy[all]
py -3 -m robotpy_installer install robotpy[all]

:: ------------------------------------------------------
:: Download and install robotpy-cscore
:: ------------------------------------------------------
:: py -3 -m robotpy_installer download robotpy[cscore]
:: py -3 -m robotpy_installer install robotpy[cscore]

:: ------------------------------------------------------
:: Download and install photonvision
:: ------------------------------------------------------
:: py -3 -m pip install -U robotpy[photonvision]
:: py -3 -m robotpy_installer download robotpy[photonvision]
:: py -3 -m robotpy_installer install robotpy[photonvision]
:: ------------------------------------------------------
:: Download and install pyfrc -- FIXME: dependency issue stops install
:: ------------------------------------------------------
:: py -3 -m robotpy_installer download pyfrc
:: py -3 -m robotpy_installer install pyfrc
:: ------------------------------------------------------
:: Display useful information
:: ------------------------------------------------------
py -3 -m robotpy_installer list
ECHO "[+] Installation of robotpy onto RoboRIO successful!"
PAUSE