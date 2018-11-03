#!/usr/bin/env bash
mvn -pl "bahmni-gauge-commons,bahmni-gauge-default" clean install -DskipTests
echo "The env in run.sh $1 $2"
cd bahmni-gauge-default/ && mvn gauge:execute -Denv=$1 -Dtags="$2"