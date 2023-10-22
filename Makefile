include .env

ZIP_FOLDER := zip_folder
UNZIPPED_FOLDER := unzipped_folder
BYTESCODE_FOLDER := bytescode_folder

all: download unzip unzip2bytescode

# Download the motif_reports.csv file from the MOTIF repository =============================================================
download:
	mkdir $(ZIP_FOLDER)
	curl -o motif_reports.csv https://raw.githubusercontent.com/boozallen/MOTIF/68525d4896f2ca33c8b0c27e8bfe9a52e8c93967/dataset/motif_reports.csv
	python vs.py --username $(USERNAME) --password $(PASSWORD) --output_folder $(ZIP_FOLDER) --family icedid
	python vs.py --username $(USERNAME) --password $(PASSWORD) --output_folder $(ZIP_FOLDER) --family maze
	python vs.py --username $(USERNAME) --password $(PASSWORD) --output_folder $(ZIP_FOLDER) --family azorult

unzip:
	mkdir $(UNZIPPED_FOLDER)
	unzip $(ZIP_FOLDER)/*.zip -d $(UNZIPPED_FOLDER)

unzip2bytescode:
	mkdir $(BYTESCODE_FOLDER)
	sudo apt-get install xxd -y
	for file in $(UNZIPPED_FOLDER)/*.; do
		xxd -b $$file > $(BYTESCODE_FOLDER)/$$(basename $$file).txt
	done