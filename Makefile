init:
	docker run -p 6379:6379 -d redis:2.8

server:
	python manage.py runserver

client:
	python client.py
