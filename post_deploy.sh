#!/bin/bash

aws lambda update-function-code \
    --function-name pluralize \
    --s3-bucket pluralize-code-bede-io \
    --s3-key build.zip
