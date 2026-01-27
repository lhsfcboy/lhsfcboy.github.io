#!/usr/bin/env bash

trap 'echo "A.sh exiting"; exit 0' SIGTERM SIGINT

msg="Hello, world"
delay_seconds=1 # 设置延迟时间，单位为秒

while true; do
  # 获取当前JST时间
  jst_time=$(TZ=Asia/Tokyo date '+%Y-%m-%d %H:%M:%S')

  # 构建完整的响应体
  response_body=$(printf "%s\n%s" "${msg}" "${jst_time}")

  {
    printf "HTTP/1.1 200 OK\r\n"
    printf "Content-Type: text/plain\r\n"
    printf "Content-Length: %d\r\n" "$((${#response_body} + 1))"
    printf "Connection: close\r\n" # 确保连接在响应后关闭
    printf "\r\n"
    printf "%s\n\n" "${response_body}"
  } | nc -l 8080 -q 1 # -q 1 (或在某些版本 nc 中是 -N 或 -c) 使得 nc 在 EOF 后等待1秒然后退出

  # 在处理完一个连接后，添加延迟
  echo "Request processed, sleeping for ${delay_seconds} seconds..."
  sleep "${delay_seconds}"
done
