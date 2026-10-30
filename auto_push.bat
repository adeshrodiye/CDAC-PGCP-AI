@echo off
cd /d "E:\Vishal_Adesh\CDAC-PGCP-AI"

git add .
git commit -m "Auto backup on %date% at %time%"
git push origin main