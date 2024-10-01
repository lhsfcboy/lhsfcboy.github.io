# youtube-dl

## 安装/升级

pip install -U youtube_dl

[GitHub地址](https://github.com/rg3/youtube-dl)

## 常用参数

```text
-i, --ignore-errors              Continue on download errors, for example to
                                 skip unavailable videos in a playlist
--get-filename                   Simulate, quiet but print output filename
--newline                        Output progress bar as new lines
--no-progress                    Do not print progress bar

# Video Selection:
--playlist-start NUMBER          Playlist video to start at (default is 1)
--playlist-end NUMBER            Playlist video to end at (default is last)
```

## 查看目标视频详情

```bash
youtube-dl -F http://www.bilibili.com/video/av3509380/
```

## 下载视频到当前文件夹，可以选择清晰度

youtube-dl -f 格式号 url

## mp4中的最佳视频

-f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'

## 下载youtube列表中的最佳分辨率, 且使用 列表名-文件名的格式命名

youtube-dl --format best -o "%(playlist)s-%(title)s.%(ext)s"  PLRCe1CegVgvjK4Qg-KZ_kQY2Sf8LQn511

## 直接嵌入字幕文件

youtube-dl.exe --embed-subs --write-sub url

## 通过文件名来指定目录

```bash
youtube-dl -o '%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/user/TheLinuxFoundation/playlists
```