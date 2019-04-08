#!/usr/bin/env bash
mvn -pl "bahmni-gauge-commons,bahmni-gauge-amman"  clean install -DskipTests
echo "The env in run.sh $1 $2 $3"
cd bahmni-gauge-amman/ && mvn gauge:execute -Denv=$1 -Dtags="$2" -DinParallel=$3