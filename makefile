SHELL=/bin/bash


clean:
	@echo "Cleaning up..." &&\
	cd src &&\
	rm -rf db.sqlite3 &&\
	rm -rf */migrations/0* &&\
	rm -rf */__pycache__ &&\
	rm -rf */**/__pycache__ &&\
	rm -rf */**/migrations/*_initial.py &&\
	rm -rf */migrations/00*_*.py 
	@echo "Done."

migrations:
	@echo "Creating migrations..." &&\
	cd src &&\
	python manage.py makemigrations &&\
	python manage.py migrate 
	@echo "Done."
	

run:
	@echo "Running server..." &&\
	cd src &&\
	python manage.py runserver


superuser:
	@echo "Creating superuser..." &&\
	cd src &&\
	python manage.py createsuperuser 
	@echo "Done."


app:
	@echo "Creating app..." 
	@echo "Enter app name: " &&\
	read name &&\
	cd src && python manage.py startapp $$name
	@echo "Done."