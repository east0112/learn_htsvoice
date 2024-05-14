# Ubuntuベースイメージを使用
FROM ubuntu:22.04

# 環境変数の設定
ENV DEBIAN_FRONTEND=noninteractive

# パッケージリストの更新
RUN apt-get update

# 各パッケージを個別にインストール
RUN apt-get install -y build-essential
RUN apt-get install -y git
RUN apt-get install -y wget
RUN apt-get install -y unzip
RUN apt-get install -y python3
RUN apt-get install -y ffmpeg
RUN apt-get install -y sox
RUN apt-get install -y libsox-fmt-all
RUN apt-get install -y libpulse-dev
RUN apt-get install -y libasound-dev
RUN apt-get install -y hts-voice-nitech-jp-atr503-m001
RUN apt-get install -y cmake
RUN apt-get install -y curl
RUN apt-get install -y csh
RUN apt-get install -y libx11-dev
RUN apt-get install -y flac
RUN apt-get install -y jq
RUN apt-get install -y sudo
RUN apt-get install -y unzip
RUN apt-get install -y bc
RUN apt-get install -y python3-pip

RUN pip3 install google-cloud-speech pydub

WORKDIR /app
