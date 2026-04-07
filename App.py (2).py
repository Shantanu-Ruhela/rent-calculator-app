{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "72929118-7bbc-4d2d-adfd-2282993da200",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "18056fa6-16ad-45d8-ab63-6c3ba73bddc3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "061f6487-f948-44c6-a76a-60e3f26ac102",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.title(\"Rent Calculator App\")\n",
    "\n",
    "# inputs\n",
    "rent = st.number_input(\"Enter your hostel/flat rent\",min_value=0)\n",
    "food = st.number_input(\"Enter the amount of food ordered\",min_value=0)\n",
    "electricity_spend = st.number_input(\"Enter electricity units spent\",min_value=0)\n",
    "charge_per_unit = st.number_input(\"Enter per unit charge\",min_value=0)\n",
    "\n",
    "persons = st.number_input(\"Enter number of persons\",min_value=0)\n",
    "\n",
    "# Calculation\n",
    "if st.button(\"calculation\"):\n",
    "    total_bill = electricity_spend * charge_per_unit\n",
    "    total = (rent + food + total_bill) // persons\n",
    "    st.success(f\"Each person should pay :Rs{total}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53ca40c2-8629-45a0-ab3f-ebc962558d1e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
