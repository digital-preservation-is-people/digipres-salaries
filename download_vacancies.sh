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
rss="https://www.dpconline.org/news/job-vacancies/all?format=feed&type=rss"
source="sources/"
rss_name="dpc-vacancies-rss.rss"

rm -f "${dir}";
mkdir -p "${dir}";

curl -s "${rss}" > "${sources}${rss_name}"

for i in $(seq 0 10 $END);
do
	output="${dir}"/"${fname}"$i.htm;
	echo "${url}"$i;
	curl -s "${url}"$i > "${output}";
done

