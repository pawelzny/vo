#!/usr/bin/env bash

# Get absolute path to this script directory
bin_dir=$(dirname $(readlink -f "$0"))
package_dir=${bin_dir}/../
coverage_dir=${package_dir}/tests/coverage

# Run tests with nose test runner
nosetests --where=${package_dir} \
          --with-coverage --cover-erase --cover-branches \
          --cover-html --cover-html-dir=${coverage_dir} \
          --cover-xml --cover-xml-file=${package_dir}/coverage.xml \
          --stop
