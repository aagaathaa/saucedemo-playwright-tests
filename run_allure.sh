#!/bin/bash

if [ -d "allure-report/history" ]; then
    cp -R allure-report/history allure-results/
fi

pytest --alluredir=allure-results

allure generate allure-results -o allure-report --clean

allure open allure-report