#!/usr/bin/env python
# -*- coding: utf-8 -*-
from aiogram import types
import datetime
from load import bot
from database import Database

db = Database()

class Button:
    def __init__(self) -> None:
        pass

    def _create_keyboard(self, btns):
        button = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        for btn in btns:
            button.add(btn)

        return button
    
    def admin(self):
        return self._create_keyboard([
            "📦 Толықтыру",
            "📃 Тізімді көру",
            "🔴 Жою"
        ])
    
    def cancel(self):
        return self._create_keyboard([
            "🔕 Бас тарту"
        ])
    
    def delete(self):
        return self._create_keyboard([
            "🔴 Жою"
        ])
    
    def time(self):
        start_hour, end_hour = 8, 23
        
        intervals = [f"{hour:02d}:{minute:02d}" for hour in range(start_hour, end_hour + 1) for minute in [0, 30]]
        intervals += ["🔕 Бас тарту"]
    
        return self._create_keyboard(intervals)