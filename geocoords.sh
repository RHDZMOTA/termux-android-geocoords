#!/bin/bash

i=1
while true
do
  echo ----------
  echo Recording Iteration: $i
  position=$(termux-location)
  day=$(date "+%d-%m-%Y")
  time=$(date "+%H:%M:%S")
  lat=$(echo $loc | jq .latitude)
  lon=$(echo $loc | jq .longitude)
  alt=$(echo $loc | jq .altitude)
  datapoint=$(echo ${day},${time},${lon},${lat},${alt})
  echo $datapoint >> data/geo_data.csv
  echo {lat:$lat, lon:$lon, alt:$alt}
  echo
  i=$((i+1))
done
