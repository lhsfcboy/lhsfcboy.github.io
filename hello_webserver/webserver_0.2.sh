#!/usr/bin/env bash

trap 'echo "webserver_0.2.sh exiting"; exit 0' SIGTERM SIGINT

# 确保 SSL 证书和密钥存在
if [[ ! -f "server.crt" || ! -f "server.key" ]]; then
    echo "Generating self-signed certificate..."
    openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes -subj "/CN=localhost" 2>/dev/null
fi

msg="Hello, world"
delay_seconds=1 # 设置延迟时间，单位为秒
port=8443

echo "Starting HTTPS server on port ${port}..."

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
  } | openssl s_server -accept "${port}" -cert server.crt -key server.key -naccept 1 -quiet 2>/dev/null

  # 在处理完一个连接后，添加延迟
  echo "Request processed, sleeping for ${delay_seconds} seconds..."
  sleep "${delay_seconds}"
done
