#!/bin/sh

echo "The env is $1 $2 - in run-docker.sh"
docker run -v ~/.m2:/root/.m2:rw -v ~/projects/bahmni/bahmni-gauge:/gauge -e ENV=$1 -e TAGS=$2 -e BAHMNI_GAUGE_APP_LOCATION=Registration -e BAHMNI_GAUGE_APP_URL=https://qa-reporting.ehealthunit.org -e BAHMNI_GAUGE_APP_PASSWORD=P@ssw0rd -e BAHMNI_GAUGE_APP_LOCALE=en -e BAHMNI_GAUGE_APP_USER=superman -e RUNS_IN_DOCKER=true -i anallytics/docker-gauge-chromedriver:latest -- sh run.sh
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