install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install: #просто запускаю из терминала python3 -m pip install --break-system-packages --user dist/*.whl вот такую команду из корня, т.к. pip без '--break-system-packages' выдает ошибку в Ubuntu 24 
	python3 -m pip install --user dist/*.whl
#для пересборки использовать команду python3 -m pip install --force-reinstall --break-system-packages --user dist/*.whl
#т.е. добавить ключ --force-reinstall. Эта команда, как и предыдущая работает только когда poetry shell уже exit