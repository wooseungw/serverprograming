{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Running on local URL:  http://127.0.0.1:7860\n",
      "\n",
      "To create a public link, set `share=True` in `launch()`.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div><iframe src=\"http://127.0.0.1:7860/\" width=\"100%\" height=\"500\" allow=\"autoplay; camera; microphone; clipboard-read; clipboard-write;\" frameborder=\"0\" allowfullscreen></iframe></div>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": []
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "IMPORTANT: You are using gradio version 4.28.3, however version 4.29.0 is available, please upgrade.\n",
      "--------\n"
     ]
    }
   ],
   "source": [
    "import gradio as gr\n",
    "from pytube import YouTube      \n",
    "\n",
    "def download_youtube_video(youtube_url):\n",
    "    yt = YouTube(youtube_url)\n",
    "    yt.streams.first().download()\n",
    "    return \"Done\"\n",
    "\n",
    "demo = gr.Interface(download_youtube_video, \"textbox\", \"label\")\n",
    "demo.launch()\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "pyserverprog",
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
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
