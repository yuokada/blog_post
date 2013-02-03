# hoge

## server

::

    % python2.7 dbindex.py

## client

::

    % curl  --header "Content-type: application/json"  \
        --request POST \
        --data '{"city": "Tokyo", "town":"new多摩", "prefecture":"東京都"}' \
        http://localhost:5000/zipcode/1000003.json

