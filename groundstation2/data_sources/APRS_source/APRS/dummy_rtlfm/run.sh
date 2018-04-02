#Repeatedly echo prerecorded data, pretending to be a live rtl_fm output for testing.

while :
do
	cat ${BASH_SOURCE%/*}/data.wav
	sleep 2
done
