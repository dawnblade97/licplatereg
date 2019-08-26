echo "----------------------------------License plate recognition---------------------------------"


echo 'enter the image name ...... must be in the same directory of the shell file..................'
read n
python usp.py $n
./darknet detector test cfg/obj.data cfg/tiny-yolo.cfg backup/tiny-yolo_8000.weights $n|tee -a log.txt

#mkdir plates
#mkdir processed
#mkdir borders
#mkdir resized
#mkdir results

#python try.py $n

python try3.py $n

rm log.txt
#rm -r plates/
#rm -r processed/
#rm -r borders/
#rm -r resized/
#rm -r results/
