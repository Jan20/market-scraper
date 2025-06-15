curl --location 'http://localhost:8080/market' \
--header 'Content-Type: application/json' \
--data '{
    "market": "dax"
}' -o "$LOCAL_DAX_FILE_PATH"
