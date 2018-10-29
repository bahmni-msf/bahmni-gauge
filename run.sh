#!/bin/sh
nohup Xvfb -ac :99 -screen 0 1280x1024x16 &
export DISPLAY=:99
mvn -pl "bahmni-gauge-commons,bahmni-gauge-default" clean install -DskipTests
echo "The env in run.sh $ENV $TAGS"
cd bahmni-gauge-default/ && mvn gauge:execute -Denv=$ENV -Dtags="$TAGS"