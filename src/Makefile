ZIP_FILE_NAME=xklofe01_xszabo16_xsuman02_xrodak00
PY=python3
PIP=pip3
DUCK_CALC=duck_calc
PROFILE_TOOL=profile
DOC_TOOL=doxygen
WEB_BROWSER=firefox

.PHONY: all run	profile profile-stats-img doc tests cov-test open-cov-report requirements install-from-source build-deb-package

# Spusti aplikaci
all:
	$(PY) -m $(DUCK_CALC).main

# Spusti aplikaci na pozadi
run: 
	$(PY) -m $(DUCK_CALC).main &

# Spusti profiling
profile:
	$(PY) -m $(PROFILE_TOOL) profiler.py < ../profiling/100.txt

# Spusti profiling a vytvori obrazek z dat profileru
profile-stats-img:
	$(PY) -m $(PROFILE_TOOL) -o stats profiler.py < ../profiling/100.txt
	gprof2dot -f pstats stats | dot -Tpng -o output.png

# Vygeneruje  documentaci
doc:
	$(DOC_TOOL) Doxyfile

# Spusti celou test suite
tests: 
	tox

# Spusti coverage test suite
cov-test:
	$(PY) -m pytest --cov duck_calc --cov-report html --cov-branch

# Spusti coverage test suite a otevre vysledek
open-cov-report: cov-test
	$(WEB_BROWSER) htmlcov/index.html

# Nainstaluje requirements 
requirements:
	$(PIP) install -r requirements.txt

# Nainstaluje aplikaci primo se zdrojovych kodu
install-from-source:
	$(PIP) install .

# Vytvori deb balicek ve slozce installer
build-deb-package:
	./build.sh
	./build-clean.sh
	cp *.deb ../installer
	rm *.deb

# Zabali projekt k odevzdani 
pack: clean doc prepare-dir $(ZIP_FILE_NAME).zip

$(ZIP_FILE_NAME).zip:
	 zip -r ../../$(ZIP_FILE_NAME).zip ../../$(ZIP_FILE_NAME)

prepare-dir:
	mkdir -p ../../$(ZIP_FILE_NAME)/repo
	mkdir ../../$(ZIP_FILE_NAME)/installer
	mkdir ../../$(ZIP_FILE_NAME)/doc
	cp -a ../../ivs_calc/. ../../$(ZIP_FILE_NAME)/repo/
	cp -a ./doc/. ../../$(ZIP_FILE_NAME)/doc/
	cp -a ../installer/. ../../$(ZIP_FILE_NAME)/installer/
	rm -rf ../../$(ZIP_FILE_NAME)/repo/installer
	rm -rf ../../$(ZIP_FILE_NAME)/repo/src/doc	
	

# Odstrani nepotrebne soubory
clean:
	./build-clean.sh
	git clean -dfx
	rm -rf ../../$(ZIP_FILE_NAME)
