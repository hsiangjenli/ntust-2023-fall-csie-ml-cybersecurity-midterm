include .env

ZIP_FOLDER := zip_folder
UNZIPPED_FOLDER := unzipped_folder
BYTESCODE_FOLDER := bytescode_folder

all: download unzip unzip2bytescode

# Download the motif_reports.csv file from the MOTIF repository =============================================================
download:
	mkdir -p $(ZIP_FOLDER)
	wget https://raw.githubusercontent.com/boozallen/MOTIF/68525d4896f2ca33c8b0c27e8bfe9a52e8c93967/dataset/motif_reports.csv
	python3 vs.py --username $(USERNAME) --password $(PASSWORD) --output_folder $(ZIP_FOLDER) --family icedid
	python3 vs.py --username $(USERNAME) --password $(PASSWORD) --output_folder $(ZIP_FOLDER) --family maze
	python3 vs.py --username $(USERNAME) --password $(PASSWORD) --output_folder $(ZIP_FOLDER) --family azorult

unzip:
	mkdir -p $(UNZIPPED_FOLDER)
	cd $(ZIP_FOLDER) && unzip -P infected "*.zip" -d ../$(UNZIPPED_FOLDER)/

unzip2bytescode:
	mkdir -p $(BYTESCODE_FOLDER)
	cd $(UNZIPPED_FOLDER) && for file in *; do xxd -b "$$file" > "../$(BYTESCODE_FOLDER)/$$(basename "$$file").txt"; done
