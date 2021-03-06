{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5fa4d1be",
   "metadata": {},
   "outputs": [],
   "source": [
    "#libraries\n",
    "from PIL import Image\n",
    "from pyzbar.pyzbar import decode"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b4c5d6d3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[Decoded(data=b'https://www.kpitb.gov.pk/projects/kp-citizen-facilitation-program', type='QRCODE', rect=Rect(left=41, top=41, width=368, height=368), polygon=[Point(x=41, y=41), Point(x=41, y=408), Point(x=409, y=409), Point(x=408, y=41)])]\n"
     ]
    }
   ],
   "source": [
    "result = decode(Image.open('Project.png'))\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21d49d0e",
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
   "version": "3.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
