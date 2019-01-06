FROM mongo

COPY filmResult.json /filmResult.json
CMD mongoimport --host mongodb --db filmsdb --collection films --type json --file /filmResult.json --jsonArray