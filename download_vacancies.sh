#!/bin/bash

# Script to download salary pages from the DPC website.
#
# TODO: the Internet archive might date back beyond 2017.
#
#

END=220
url="https://www.dpconline.org/news/job-vacancies?start="
dir="pages"
fname="dpc_page_"

rm -f "${dir}";
mkdir -p "${dir}";

for i in $(seq 0 10 $END);
do
	output="${dir}"/"${fname}"$i.htm;
	echo "${url}"$i;
	curl -s "${url}"$i > "${output}";
done
