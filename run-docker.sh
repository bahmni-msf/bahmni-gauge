#!/bin/sh

echo "The env is $1 $2 - in run-docker.sh"
sudo docker run -v /var/go/.m2:/root/.m2:rw -v $PWD:/gauge -e ENV=$1 -e TAGS=$2 -i anallytics/docker-gauge-chromedriver:latest -- sh run.sh
#docker run -v ~/.m2:/root/.m2:rw -v $PWD:/gauge -e ENV=$1 -e TAGS=$2 -i docker-gauge-chromedriver:2.42 -- sh run.sh
#Hack. The html-report executable is symlinked as a root user.  
#so, removing it so that the artifact is accessible from gocd server
rc=$?
if [[ $rc != 0 ]]; then
	rm -f bahmni-gauge-default/reports/html-report/html-report
	echo "The build is failed"
	exit $rc; 
fi
rm -f bahmni-gauge-default/reports/html-report/html-report
echo "The build is successful"