#!/usr/bin/env bash

trap 'echo "Server exiting"; exit 0' SIGTERM SIGINT

# HTTPS配置
CERT_FILE="/tmp/server.crt"
KEY_FILE="/tmp/server.key"
PORT=8443

msg="Hello, HTTPS world"
delay_seconds=1

# 生成自签名证书和密钥（如果不存在）
generate_cert() {
  if [[ ! -f "$CERT_FILE" ]] || [[ ! -f "$KEY_FILE" ]]; then
    echo "Generating self-signed certificate..."
    openssl req -x509 -newkey rsa:2048 -keyout "$KEY_FILE" -out "$CERT_FILE" \
      -days 365 -nodes -subj "/C=JP/ST=Tokyo/L=Tokyo/O=Test/CN=localhost" 2>/dev/null
    echo "Certificate generated at $CERT_FILE"
    echo "Key generated at $KEY_FILE"
  fi
}

# 验证依赖工具
check_dependencies() {
  if ! command -v openssl &> /dev/null; then
    echo "Error: openssl is not installed"
    exit 1
  fi
}

check_dependencies
generate_cert

while true; do
  # 获取当前JST时间
  jst_time=$(TZ=Asia/Tokyo date '+%Y-%m-%d %H:%M:%S')

  # 构建完整的响应体
  response_body=$(printf "%s\n%s" "${msg}" "${jst_time}")

  {
    printf "HTTP/1.1 200 OK\r\n"
    printf "Content-Type: text/plain\r\n"
    printf "Content-Length: %d\r\n" "$((${#response_body} + 1))"
    printf "Connection: close\r\n"
    printf "\r\n"
    printf "%s\n\n" "${response_body}"
  } | openssl s_server -cert "$CERT_FILE" -key "$KEY_FILE" -port $PORT -quiet 2>/dev/null

  # 在处理完一个连接后，添加延迟
  echo "Request processed, sleeping for ${delay_seconds} seconds..."
  sleep "${delay_seconds}"
done
