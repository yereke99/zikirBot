#!/usr/bin/env python
# -*- coding: utf-8 -*-
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from load import bot, dp
from aiogram import types
from forma import Forma
from keyboard import*
from database import*
import asyncio
from forma import*
from config import admin

db = Database()
btn = Button()

@dp.message_handler(commands=['admin'])
async def start_handler(message: types.Message):
    print(message.from_user.id)
    
    await bot.send_message(
        message.from_user.id,
        text="""*Құрметті Дәулет🙂\nСізге Алланың нұры жаусын ☀️\nТілеген дұға-тілектерңіз қабыл болсын 🤲*""",
        parse_mode="Markdown",
        reply_markup=btn.admin()
    ) 

@dp.message_handler(Text(equals="📦 Толықтыру"), content_types=['text'])
async def handler(message: types.Message, state: FSMContext):
    await Forma.s1.set()

    await bot.send_message(
        message.from_user.id,
        text="""*Толықтыратын тексті енгізіңіз ✍️*""",
        parse_mode="Markdown",
        reply_markup=btn.cancel()
    )  

@dp.message_handler(Text(equals="🔴 Жою"), content_types=['text'])
async def handler(message: types.Message, state: FSMContext):
    await Delete.s1.set()

    await bot.send_message(
        message.from_user.id,
        text="""Жойылатын текст ID енгізңіз!""",
        parse_mode="Markdown",
        reply_markup=btn.cancel()
    )  

@dp.message_handler(Text(equals="📃 Тізімді көру"), content_types=['text'])
async def handler(message: types.Message):

    data = db.FetchAll()

    if len(data) == 0:
        await bot.send_message(
        message.from_user.id,
        text="""*Әзірше мәліметтер қоры бос😕, толтырыңыз Алла разылығы үшін 🤲*""",
        parse_mode="Markdown"
    ) 
        
    for item in data:
            await bot.send_message(
                message.from_user.id,
                text="""*ID: %s\n\nМәтін 📨: %s*\n\nЖіберілетін уақыты 🕰: %s"""%(item[0], item[1], item[2]),
                parse_mode="Markdown",
                reply_markup=btn.delete()
            )     

    
    