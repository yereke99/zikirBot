from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types.message import Message
from load import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
import logging
from keyboard import*
from database import Database
import datetime
from main import*
import asyncio
from config import admin


btn= Button()
db = Database()

class Forma(StatesGroup):
    s1 = State()
    s2 = State()

class Delete(StatesGroup):
    s1 = State()

@dp.message_handler(state='*', commands='🔕 Бас тарту')
@dp.message_handler(Text(equals='🔕 Бас тарту', ignore_case=True), state='*')
async def cancell_handler(message: types.Message, state: FSMContext):
    """
    :param message: Бастартылды
    :param state: Тоқтату
    :return: finish
    """
    
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Бас тарту!')
    await state.finish()
    await message.reply('Сіз бас тарттыңыз.', reply_markup=btn.admin())

@dp.message_handler(state=Delete.s1)
async def handler(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['id'] = message.text  

    db.Delete(int(data['id']))    
    
    await bot.send_message(
        message.from_user.id,
        text="Сәтті жойылды", 
        reply_markup=btn.admin()
    ) 

    await state.finish()

@dp.message_handler(state=Forma.s1)
async def handler(message: types.Message, state: FSMContext):
    
    await Forma.next()
    
    async with state.proxy() as data:
        data['text'] = message.text  
    
    await bot.send_message(
        message.from_user.id,
        text="Уақытты енгізіңіз", 
        reply_markup=btn.time()
    ) 

@dp.message_handler(state=Forma.s2)
async def handler(message: types.Message, state: FSMContext):
   
    async with state.proxy() as data:
        data['time'] = message.text  

    db.InsertData(data['text'], data['time'])    
    
    await bot.send_message(
        message.from_user.id,
        text="Сәтті енгізілді 🙌", 
        reply_markup=btn.admin()
    ) 

    await state.finish()