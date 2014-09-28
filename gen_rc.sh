#!/bin/env sh
SCRYPTNAME="$(basename "${0}")"
echo "start ${SCRYPTNAME} \"${1}\""

cd "${1}"

for IF in `find -name \*.ui`
do
	IF="$(basename ${IF})"
	OF="ui_${IF%.*}.py"
	echo "${IF} >> ${OF}"
	pyuic5 -o "${OF}" "${IF}"
done

for IF in `find -name \*.qrc`
do
	IF="$(basename ${IF})"
	OF="${IF%.*}_rc.py"
	echo "${IF} >> ${OF}"
	pyrcc5 -o "${OF}" "${IF}"
done

echo "stop ${SCRYPTNAME} \"${1}\""
