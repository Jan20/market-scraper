curl --location 'http://localhost:8080/market' \
--header 'Content-Type: application/json' \
--data '{
    "market": "nasdaq"
}' -o "$LOCAL_NASDAQ_FILE_PATH"
