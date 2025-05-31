# Linux下脚本内容变化时自动重启

效果: 当脚本文件work.sh的内容变化时, 自动重启.

## 通过监视脚本实现

```sh
#!/bin/bash

# 配置部分
TARGET_SCRIPT="./your_script.sh"  # 要监控的目标脚本路径
CHECK_INTERVAL=2                  # 检查间隔（秒）
RESTART_DELAY=1                   # 重启前等待时间（秒）

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 日志函数
log() {
    echo -e "${BLUE}[$(date '+%Y-%m-%d %H:%M:%S')]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[$(date '+%Y-%m-%d %H:%M:%S')]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[$(date '+%Y-%m-%d %H:%M:%S')]${NC} $1"
}

log_error() {
    echo -e "${RED}[$(date '+%Y-%m-%d %H:%M:%S')]${NC} $1"
}

# 清理函数
cleanup() {
    log "接收到退出信号，正在清理..."
    if [ ! -z "$SCRIPT_PID" ] && kill -0 $SCRIPT_PID 2>/dev/null; then
        log "终止目标脚本 (PID: $SCRIPT_PID)"
        kill $SCRIPT_PID
        wait $SCRIPT_PID 2>/dev/null
    fi
    log "监控脚本退出"
    exit 0
}

# 启动目标脚本
start_script() {
    log "启动目标脚本: $TARGET_SCRIPT"
    
    # 确保脚本有执行权限
    chmod +x "$TARGET_SCRIPT"
    
    # 后台启动脚本
    bash "$TARGET_SCRIPT" &
    SCRIPT_PID=$!
    
    log_success "目标脚本已启动 (PID: $SCRIPT_PID)"
}

# 停止目标脚本
stop_script() {
    if [ ! -z "$SCRIPT_PID" ] && kill -0 $SCRIPT_PID 2>/dev/null; then
        log "停止目标脚本 (PID: $SCRIPT_PID)"
        kill $SCRIPT_PID
        wait $SCRIPT_PID 2>/dev/null
        log_success "目标脚本已停止"
    fi
    SCRIPT_PID=""
}

# 重启目标脚本
restart_script() {
    log_warning "重启目标脚本..."
    stop_script
    sleep $RESTART_DELAY
    start_script
}

# 检查脚本是否还在运行
is_script_running() {
    [ ! -z "$SCRIPT_PID" ] && kill -0 $SCRIPT_PID 2>/dev/null
}

# 获取文件修改时间
get_file_mtime() {
    if [ -f "$1" ]; then
        stat -c %Y "$1" 2>/dev/null || stat -f %m "$1" 2>/dev/null
    else
        echo "0"
    fi
}

# 主函数
main() {
    # 设置信号处理
    trap cleanup SIGINT SIGTERM
    
    log "=== 自动重启监控脚本启动 ==="
    log "目标脚本: $TARGET_SCRIPT"
    log "检查间隔: ${CHECK_INTERVAL}秒"
    log "重启延迟: ${RESTART_DELAY}秒"
    echo
    
    # 检查目标脚本是否存在
    if [ ! -f "$TARGET_SCRIPT" ]; then
        log_error "错误: 目标脚本 '$TARGET_SCRIPT' 不存在"
        exit 1
    fi
    
    # 获取初始修改时间
    LAST_MTIME=$(get_file_mtime "$TARGET_SCRIPT")
    
    # 启动目标脚本
    start_script
    
    # 主监控循环
    while true; do
        sleep $CHECK_INTERVAL
        
        # 检查文件是否被修改
        CURRENT_MTIME=$(get_file_mtime "$TARGET_SCRIPT")
        if [ "$CURRENT_MTIME" != "$LAST_MTIME" ]; then
            log_warning "检测到文件修改: $TARGET_SCRIPT"
            LAST_MTIME=$CURRENT_MTIME
            restart_script
            continue
        fi
        
        # 检查脚本是否还在运行
        if ! is_script_running; then
            log_warning "目标脚本已退出，准备重启..."
            start_script
        fi
    done
}

# 帮助信息
show_help() {
    echo "用法: $0 [选项] [目标脚本路径]"
    echo
    echo "选项:"
    echo "  -h, --help     显示此帮助信息"
    echo "  -i INTERVAL    设置检查间隔（秒，默认2）"
    echo "  -d DELAY       设置重启延迟（秒，默认1）"
    echo
    echo "示例:"
    echo "  $0 ./my_script.sh"
    echo "  $0 -i 5 -d 2 ./my_script.sh"
}

# 解析命令行参数
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_help
            exit 0
            ;;
        -i)
            CHECK_INTERVAL="$2"
            shift 2
            ;;
        -d)
            RESTART_DELAY="$2"
            shift 2
            ;;
        -*)
            log_error "未知选项: $1"
            show_help
            exit 1
            ;;
        *)
            TARGET_SCRIPT="$1"
            shift
            ;;
    esac
done

# 运行主函数
main
```

## 通过系统服务实现

## 通过第三方工具实现

1. [inotify-tools](https://github.com/rvoicilas/inotify-tools/wiki)
