tail -n0 -F example.log | grep --line-buffered 11 |  xargs -I @ curl -s  \
https://hooks.slack.com/services/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 \
   -X POST \
   -H 'Content-type: application/json' \
    --data '{"username":"curl", "text":"@"}'
