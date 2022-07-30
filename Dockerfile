FROM python:3.8-slim

ADD game_of_life_cli.py .

CMD ["python", "./game_of_life_cli.py"]