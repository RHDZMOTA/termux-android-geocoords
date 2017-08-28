#!/bin/bash

i=1
while true
do
  echo ----------
  echo Recording Iteration: $i
  position=$(termux-location)
  day=$(date "+%d-%m-%Y")
  time=$(date "+%H:%M:%S")
  lat=$(echo $position | jq .latitude)
  lon=$(echo $position | jq .longitude)
  alt=$(echo $position | jq .altitude)
  speed=$(echo $position | jq .speed)
  datapoint=$(echo ${day},${time},${lon},${lat},${alt},${speed})
  echo $datapoint >> data/geo_data.csv
  echo {lat:$lat, lon:$lon, alt:$alt, speed:$speed}
  echo
  i=$((i+1))
done
