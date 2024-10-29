{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "632191d4-daa8-4f1a-902d-9cec0f18d6d5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pyTelegramBotAPI in d:\\conda_1\\lib\\site-packages (4.23.0)\n",
      "Requirement already satisfied: requests in d:\\conda_1\\lib\\site-packages (from pyTelegramBotAPI) (2.32.2)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in d:\\conda_1\\lib\\site-packages (from requests->pyTelegramBotAPI) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in d:\\conda_1\\lib\\site-packages (from requests->pyTelegramBotAPI) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in d:\\conda_1\\lib\\site-packages (from requests->pyTelegramBotAPI) (2.2.2)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in d:\\conda_1\\lib\\site-packages (from requests->pyTelegramBotAPI) (2024.6.2)\n"
     ]
    }
   ],
   "source": [
    "!pip install pyTelegramBotAPI"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "f5b40d33-cad1-41d5-9820-b4ea09eb71c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: telebot in d:\\conda_1\\lib\\site-packages (0.0.5)\n",
      "Requirement already satisfied: pyTelegramBotAPI in d:\\conda_1\\lib\\site-packages (from telebot) (4.23.0)\n",
      "Requirement already satisfied: requests in d:\\conda_1\\lib\\site-packages (from telebot) (2.32.2)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in d:\\conda_1\\lib\\site-packages (from requests->telebot) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in d:\\conda_1\\lib\\site-packages (from requests->telebot) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in d:\\conda_1\\lib\\site-packages (from requests->telebot) (2.2.2)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in d:\\conda_1\\lib\\site-packages (from requests->telebot) (2024.6.2)\n"
     ]
    }
   ],
   "source": [
    "!pip install telebot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "7cefb5b1-9cfb-4b99-8343-57eefa35dea2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: python-dotenv in d:\\conda_1\\lib\\site-packages (0.21.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install python-dotenv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c797f3a3-d92a-4bc7-afab-bb58585306ec",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "from telebot import TeleBot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ce8033a-09dd-459d-90ba-998fa1b9f4e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "from telebot import TeleBot\n",
    "from dotenv import load_dotenv\n",
    "import os\n",
    "\n",
    "# Load environment variables from the .env file\n",
    "load_dotenv()\n",
    "\n",
    "bot = TeleBot(os.environ.get(\"TELEGRAM_BOT_TOKEN\"))\n",
    "\n",
    "@bot.message_handler(commands=[\"start\"])\n",
    "def send_welcome(message):\n",
    "    bot.reply_to(message, \"Welcome\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    bot.polling()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "859c6ccc-3d25-44b2-ac04-f194bac92bb1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# !pip freeze > requirements.txt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "7cc827c9-02e2-4aec-8844-f8aad116f617",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2772cb2f-2494-4a82-a0fa-7548df9de416",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
