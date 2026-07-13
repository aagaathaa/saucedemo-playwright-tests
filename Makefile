.PHONY: test allure

test:
	pytest

allure:
	-pytest --alluredir=allure-results
	cp allure/environment.properties allure-results/
	cp allure/executor.json allure-results/
	allure generate allure-results --clean -o allure-report
	allure open allure-report