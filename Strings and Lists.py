{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "* \n",
      "* * \n",
      "* * * \n",
      "* * * * \n",
      "* * * * * \n",
      "* * * * \n",
      "* * * \n",
      "* * \n",
      "* \n"
     ]
    }
   ],
   "source": [
    "# Question 1\n",
    "n=5\n",
    "for i in range(n):\n",
    "    for j in range(i):\n",
    "        #print(i)\n",
    "        print ('* ', end=\"\")\n",
    "    print('')\n",
    "for i in range(n,0,-1):\n",
    "    for j in range(i):\n",
    "        print('* ', end=\"\")\n",
    "    print('')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your full nameGanesh\n",
      "hsenaG\n"
     ]
    }
   ],
   "source": [
    "#Question 2\n",
    "a= input(\"Enter your full name\")\n",
    "print(a[::-1])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
