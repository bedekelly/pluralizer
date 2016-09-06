#!/bin/bash

NAME=pluralizer
FUNCTION=pluralizer.pluralize
ZIP_NAME=""

createZip() {
    # Create a zip file with a unique name.
    export ZIP_NAME=build.zip
    mkdir -p build;
    zip build/$ZIP_NAME -r9 * >/dev/null;
}

createZip && echo Successfully built: build/$ZIP_NAME
