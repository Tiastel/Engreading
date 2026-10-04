@echo off
title ReadFlow Server
echo ====================================================
echo   ReadFlow 영어 독해 연습 사이트 실행기
echo   http://localhost:3000
echo ====================================================
start http://localhost:3000
python -m http.server 3000
