Analysis of main.py

from playwright.sync_api import Playwright, sync_playwright, expect - эти строки кода пишем с целью  чтобы получить доступ ко всем функциям, методам и классам playwright - это весело, хех. aiDoni учи моя дорогая!!!

Запускаем браузер, такое понятие есть оказывается запуск браузера. Только кликая не будешь умным. Смотри какая ты молодец знаешь запуск браузера
browser = playwright.chromium.launch(headless=False)

Последующие строки кода отвечают за создание в нем контекста
context = browser.new_context()
page = context.new_page()
